"""
Quantum Fisher Information Matrix computation.
Implements efficient estimation of QFI for convergence analysis.
"""

import torch
import pennylane as qml
import numpy as np
from typing import List, Tuple, Optional

class QuantumFisherEstimator:
    def __init__(
        self,
        n_qubits: int,
        n_shots: int = 1000,
        device: str = "default.qubit"
    ):
        """
        Initialize Quantum Fisher estimator.
        
        Args:
            n_qubits: Number of qubits
            n_shots: Number of measurement shots
            device: Quantum device name
        """
        self.n_qubits = n_qubits
        self.n_shots = n_shots
        self.dev = qml.device(device, wires=n_qubits, shots=n_shots)
        
        # Initialize quantum circuit
        self.circuit = self._create_circuit()
        
    def _create_circuit(self) -> qml.QNode:
        """Create parameterized quantum circuit."""
        @qml.qnode(self.dev)
        def circuit(params):
            # State preparation
            for i in range(self.n_qubits):
                qml.RY(params[i], wires=i)
                
            # Entangling layer
            for i in range(self.n_qubits-1):
                qml.CNOT(wires=[i, i+1])
                
            # Measurement layer
            return [qml.expval(qml.PauliZ(i)) for i in range(self.n_qubits)]
            
        return circuit
        
    def compute_qfi(
        self,
        params: torch.Tensor,
        epsilon: float = 0.01
    ) -> torch.Tensor:
        """
        Compute Quantum Fisher Information matrix.
        
        Args:
            params: Circuit parameters
            epsilon: Small parameter shift
            
        Returns:
            QFI matrix
        """
        n_params = len(params)
        qfi = torch.zeros((n_params, n_params))
        
        # Compute diagonal elements
        for i in range(n_params):
            params_plus = params.clone()
            params_minus = params.clone()
            params_plus[i] += epsilon
            params_minus[i] -= epsilon
            
            # Compute expectation values
            exp_plus = torch.tensor(self.circuit(params_plus))
            exp_minus = torch.tensor(self.circuit(params_minus))
            
            # Diagonal element
            qfi[i,i] = torch.sum((exp_plus - exp_minus)**2) / (4 * epsilon**2)
            
        # Compute off-diagonal elements
        for i in range(n_params):
            for j in range(i+1, n_params):
                params_i_plus = params.clone()
                params_i_minus = params.clone()
                params_j_plus = params.clone()
                params_j_minus = params.clone()
                
                params_i_plus[i] += epsilon
                params_i_minus[i] -= epsilon
                params_j_plus[j] += epsilon
                params_j_minus[j] -= epsilon
                
                # Compute mixed derivatives
                exp_i_plus = torch.tensor(self.circuit(params_i_plus))
                exp_i_minus = torch.tensor(self.circuit(params_i_minus))
                exp_j_plus = torch.tensor(self.circuit(params_j_plus))
                exp_j_minus = torch.tensor(self.circuit(params_j_minus))
                
                # Off-diagonal element
                qfi[i,j] = torch.sum(
                    (exp_i_plus - exp_i_minus) * (exp_j_plus - exp_j_minus)
                ) / (4 * epsilon**2)
                qfi[j,i] = qfi[i,j]
                
        return qfi
        
    def compute_natural_gradient(
        self,
        params: torch.Tensor,
        grad: torch.Tensor,
        damping: float = 1e-4
    ) -> torch.Tensor:
        """
        Compute natural gradient using QFI.
        
        Args:
            params: Circuit parameters
            grad: Regular gradient
            damping: Regularization parameter
            
        Returns:
            Natural gradient
        """
        # Compute QFI
        qfi = self.compute_qfi(params)
        
        # Add damping for numerical stability
        qfi_damped = qfi + damping * torch.eye(len(params))
        
        # Compute natural gradient
        nat_grad = torch.linalg.solve(qfi_damped, grad)
        
        return nat_grad
        
    def get_metrics(
        self,
        params: torch.Tensor
    ) -> Dict:
        """
        Compute QFI-based metrics.
        
        Args:
            params: Circuit parameters
            
        Returns:
            Dictionary of metrics
        """
        qfi = self.compute_qfi(params)
        
        metrics = {
            "qfi_condition_number": torch.linalg.cond(qfi).item(),
            "qfi_trace": torch.trace(qfi).item(),
            "qfi_max_eigenvalue": torch.max(torch.linalg.eigvals(qfi).real).item()
        }
        
        return metrics 
"""
Dynamic batch size adjustment strategy implementation.
Adapts batch size based on gradient statistics and training dynamics.
"""

import torch
import numpy as np
from typing import Dict, Tuple, Optional

class DynamicBatchSizer:
    def __init__(
        self,
        b_min: int = 32,
        b_max: int = 512,
        alpha: float = 0.1,
        warmup_steps: int = 100
    ):
        """
        Initialize dynamic batch sizer.
        
        Args:
            b_min: Minimum batch size
            b_max: Maximum batch size
            alpha: Adaptation rate
            warmup_steps: Number of warmup steps
        """
        self.b_min = b_min
        self.b_max = b_max
        self.alpha = alpha
        self.warmup_steps = warmup_steps
        
        # Initialize tracking variables
        self.step_count = 0
        self.grad_history = []
        self.batch_history = []
        
    def compute_batch_size(
        self,
        grad_norm: float,
        loss_value: float,
        current_batch: int
    ) -> int:
        """
        Compute next batch size based on gradient statistics.
        
        Args:
            grad_norm: Current gradient norm
            loss_value: Current loss value
            current_batch: Current batch size
            
        Returns:
            Next batch size
        """
        self.step_count += 1
        self.grad_history.append(grad_norm)
        self.batch_history.append(current_batch)
        
        # During warmup, use linear schedule
        if self.step_count < self.warmup_steps:
            ratio = self.step_count / self.warmup_steps
            return int(self.b_min + (self.b_max - self.b_min) * ratio)
            
        # Compute gradient variance
        if len(self.grad_history) > 10:
            grad_var = np.var(self.grad_history[-10:])
        else:
            grad_var = 0
            
        # Adaptive batch size formula
        grad_factor = 2 / (1 + np.exp(-self.alpha * grad_norm)) - 1
        var_factor = np.exp(-grad_var)
        
        batch_size = self.b_min + (self.b_max - self.b_min) * grad_factor * var_factor
        
        # Ensure batch size is within bounds
        batch_size = int(np.clip(batch_size, self.b_min, self.b_max))
        
        return batch_size
        
    def get_metrics(self) -> Dict:
        """Get current metrics for monitoring."""
        if len(self.grad_history) > 0:
            metrics = {
                "avg_batch_size": np.mean(self.batch_history[-100:]),
                "grad_variance": np.var(self.grad_history[-100:]),
                "batch_efficiency": len(set(self.batch_history[-100:])) / 100
            }
        else:
            metrics = {
                "avg_batch_size": self.b_min,
                "grad_variance": 0.0,
                "batch_efficiency": 1.0
            }
            
        return metrics
        
    def reset_stats(self):
        """Reset tracking statistics."""
        self.step_count = 0
        self.grad_history = []
        self.batch_history = [] 
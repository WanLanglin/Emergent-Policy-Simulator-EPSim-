import torch
import pytest
import numpy as np
from src.manifolds.policy_manifold import PolicyManifold

def test_policy_manifold_init():
    """Test policy manifold initialization"""
    manifold = PolicyManifold(dim=3)
    assert manifold.dim == 3
    assert manifold.metric is not None

def test_parallel_transport():
    """Test parallel transport computation"""
    manifold = PolicyManifold(dim=2)
    
    # Create test tensors
    tensor = torch.tensor([1.0, 0.0])
    start = torch.tensor([0.0, 0.0])
    end = torch.tensor([1.0, 0.0])
    
    # Compute transport
    result = manifold.parallel_transport(tensor, start, end)
    
    # For flat manifold, parallel transport should preserve the vector
    assert torch.allclose(result, tensor, atol=1e-6)
    
def test_christoffel_symbols():
    """Test Christoffel symbols computation"""
    manifold = PolicyManifold(dim=2)
    point = torch.tensor([0.0, 0.0], requires_grad=True)
    
    # Compute symbols
    symbols = manifold._compute_christoffel_symbols(point)
    
    # Check shape
    assert symbols.shape == (2, 2, 2)
    
    # For flat manifold at origin, all symbols should be zero
    assert torch.allclose(symbols, torch.zeros_like(symbols)) 
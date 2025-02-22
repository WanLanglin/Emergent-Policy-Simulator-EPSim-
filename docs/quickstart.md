# Quick Start Guide

This guide will help you get started with EPSim quickly.

## Basic Usage

Here's a simple example to get you started:

```python
from epsim.core import PolicySimulator
from epsim.policies import BasicPolicy

# Create a simulator
sim = PolicySimulator(
    agents=100,    # Number of agents
    time_steps=100 # Simulation duration
)

# Define a policy
policy = BasicPolicy(
    intervention_time=50,  # When to apply policy
    strength=0.5          # Policy strength
)

# Run simulation
results = sim.run(policy)

# Plot results
sim.plot_results(results)
```

## Core Components

### 1. PolicySimulator

The main simulation engine:

```python
from epsim.core import PolicySimulator

sim = PolicySimulator(
    agents=100,
    time_steps=100,
    random_seed=42
)
```

### 2. Policies

Different types of policies:

```python
from epsim.policies import (
    BasicPolicy,
    AdaptivePolicy,
    MultiPolicy
)

# Simple policy
policy1 = BasicPolicy(strength=0.5)

# Adaptive policy
policy2 = AdaptivePolicy(
    learning_rate=0.1,
    target_value=0.7
)

# Combined policies
multi_policy = MultiPolicy([policy1, policy2])
```

### 3. Analysis

Analyzing results:

```python
from epsim.analysis import analyze_results

# Run analysis
metrics = analyze_results(results)

# Print summary
print(metrics.summary())

# Generate plots
metrics.plot_trends()
metrics.plot_distributions()
```

## Example Scenarios

### 1. Basic Simulation

```python
# Simple policy simulation
sim = PolicySimulator(agents=100)
policy = BasicPolicy(strength=0.5)
results = sim.run(policy)
```

### 2. Multiple Policies

```python
# Combine multiple policies
policies = [
    BasicPolicy(strength=0.3),
    AdaptivePolicy(learning_rate=0.1)
]
multi_policy = MultiPolicy(policies)
results = sim.run(multi_policy)
```

### 3. Custom Analysis

```python
# Custom analysis function
def custom_analysis(results):
    return {
        'mean_effect': results.mean(),
        'max_impact': results.max()
    }

# Apply custom analysis
analysis = custom_analysis(results)
```

## Next Steps

1. Read the [Core Theory](CORE_THEORY.md) for deeper understanding
2. Explore [Experiments](EXPERIMENTS.md) for more examples
3. Check [Contributing](CONTRIBUTING.md) if you want to contribute

## Tips

- Use `random_seed` for reproducible results
- Start with simple policies before complex ones
- Monitor system resources for large simulations
- Save results for later analysis 
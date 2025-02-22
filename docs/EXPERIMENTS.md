# Experiments

This document outlines the experimental setup and results for various policy simulations conducted using EPSim.

## Experiment Structure

Each experiment follows this general structure:

1. **Setup**
   - Initial conditions
   - Parameter settings
   - Policy configurations

2. **Execution**
   - Simulation steps
   - Data collection points
   - Intervention timing

3. **Analysis**
   - Data processing methods
   - Statistical analysis
   - Visualization techniques

## Example Experiments

### Basic Policy Response

This experiment demonstrates how a simple policy intervention affects system behavior:

```python
from epsim.core import PolicySimulator
from epsim.policies import BasicPolicy

# Setup simulation
sim = PolicySimulator(
    agents=100,
    time_steps=1000
)

# Define policy
policy = BasicPolicy(
    intervention_time=500,
    strength=0.5
)

# Run simulation
results = sim.run(policy)
```

### Complex Interaction Study

This experiment explores how multiple policies interact:

```python
from epsim.policies import MultiPolicy

# Define multiple policies
policies = [
    Policy1(param1=0.1),
    Policy2(param2=0.2),
    Policy3(param3=0.3)
]

# Create combined policy
multi_policy = MultiPolicy(policies)

# Run simulation with multiple policies
results = sim.run(multi_policy)
```

## Running Experiments

To run these experiments:

1. Install EPSim
2. Configure parameters in `config.yaml`
3. Execute the experiment script:
   ```bash
   python -m epsim.experiments.run
   ```

## Results Analysis

Results are analyzed using standard statistical methods:

- Time series analysis
- Statistical significance tests
- Effect size calculations

For detailed results, see the `results/` directory in each experiment folder. 
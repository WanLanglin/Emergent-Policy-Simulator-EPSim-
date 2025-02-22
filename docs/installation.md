# Installation Guide

This guide will help you set up EPSim on your system.

## Prerequisites

Before installing EPSim, ensure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation Methods

### Method 1: Using pip

```bash
pip install epsim
```

### Method 2: From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/WanLanglin/Emergent-Policy-Simulator-EPSim-.git
   cd Emergent-Policy-Simulator-EPSim-
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements/base.txt
   ```

4. For development, install additional dependencies:
   ```bash
   pip install -r requirements/dev.txt
   ```

## Verification

To verify the installation:

```python
import epsim
print(epsim.__version__)
```

## Common Issues

### Missing Dependencies

If you encounter missing dependencies:

```bash
pip install -r requirements/base.txt --upgrade
```

### Version Conflicts

If you have version conflicts:

1. Create a new virtual environment
2. Install EPSim in the clean environment

### Platform-Specific Issues

#### Windows

- Ensure you have Visual C++ build tools installed
- Use Windows PowerShell or Command Prompt

#### Linux

- Install required system packages:
  ```bash
  sudo apt-get update
  sudo apt-get install python3-dev
  ```

#### MacOS

- Install required tools:
  ```bash
  xcode-select --install
  ```

## Next Steps

After installation:

1. Check out the [Quick Start Guide](quickstart.md)
2. Review the [Core Theory](CORE_THEORY.md)
3. Try running some [Experiments](EXPERIMENTS.md) 
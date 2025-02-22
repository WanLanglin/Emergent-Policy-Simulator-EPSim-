# Contributing to EPSim

Thank you for your interest in contributing to EPSim! This document provides guidelines and instructions for contributing.

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Emergent-Policy-Simulator-EPSim-.git
   cd Emergent-Policy-Simulator-EPSim-
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements/dev.txt
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Mathematical Notation Standards

| Symbol | Meaning | Usage Context |
|--------|---------|---------------|
| $\theta$ | Policy parameters | Core theory chapter |
| $\mathcal{M}_\pi$ | Policy manifold | Algorithm derivations |
| $\nabla$ | Gradient operator | Throughout |
| $\Gamma_{ij}^k$ | Christoffel symbols | Manifold calculations |
| $H(s)$ | Hamiltonian | Quantum annealing |

## Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings in Google style
- Keep functions focused and under 50 lines
- Use meaningful variable names

## Pull Request Process

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "feat: add your feature"
   ```

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request on GitHub

## Documentation

- Update documentation for any new features
- Include docstrings for all public functions
- Add examples in `examples/` directory
- Update mathematical derivations in `docs/`

## Testing

- Write unit tests for new features
- Ensure all tests pass locally
- Maintain test coverage above 80%
- Run tests with:
  ```bash
  pytest tests/
  ```

## Common Issues

### Math Rendering Issues
- [ ] LaTeX formulas show as source code
- [ ] Symbols display incorrectly
- [ ] Alignment problems in equations

**Screenshot**:
Attach a screenshot of the rendering issue

**Browser Information**:
- Name/Version:
- Installed plugins:

## Questions?

Feel free to open an issue or contact the maintainers. 
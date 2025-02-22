# Mathematical Formula Rendering Guide

## Quick Start

### Browser Plugin Method
1. Install [MathJax Plugin for GitHub](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima)
2. Refresh the page to see rendered LaTeX formulas

### Local Preview Method
```bash
# Install mkdocs and required plugins
pip install -r requirements/docs.txt

# Start local server
mkdocs serve

# Visit http://localhost:8000 for perfect formula rendering
```

## Writing Formulas

### Inline Formulas
Use single dollar signs for inline math: `$E = mc^2$` renders as $E = mc^2$

### Display Formulas
Use double dollar signs for display math:
```latex
$$
\mathcal{M}_\pi = \left\{ \theta \in \mathbb{R}^d \ \bigg| \ \frac{\partial^2 \mathcal{L}}{\partial \theta_i \partial \theta_j} = \sum_{k=1}^K \lambda_k \frac{\partial \phi_k}{\partial \theta_i} \otimes \frac{\partial \phi_k}{\partial \theta_j} \right\}
$$
```

### Common Symbols
| Symbol | LaTeX Code | Description |
|--------|------------|-------------|
| $\theta$ | `\theta` | Greek letter theta |
| $\mathcal{M}$ | `\mathcal{M}` | Script M |
| $\nabla$ | `\nabla` | Nabla/gradient |
| $\otimes$ | `\otimes` | Tensor product |
| $\sum$ | `\sum` | Summation |
| $\int$ | `\int` | Integral |
| $\infty$ | `\infty` | Infinity |
| $\partial$ | `\partial` | Partial derivative |

### Matrix and Vector Notation
```latex
$$
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
b_1 \\
b_2
\end{bmatrix}
$$
```

### Equation Alignment
```latex
$$
\begin{align}
\nabla_X Y &= X(Y) + \Gamma_{ij}^k X^i Y^j \frac{\partial}{\partial x^k} \\
\Gamma_{ij}^k &= \frac{1}{2}g^{kl}\left(\frac{\partial g_{jl}}{\partial x^i} + \frac{\partial g_{il}}{\partial x^j} - \frac{\partial g_{ij}}{\partial x^l}\right)
\end{align}
$$
```

## Troubleshooting

### Common Issues
1. **Formulas not rendering**
   - Check if MathJax is properly loaded
   - Verify formula syntax
   - Clear browser cache

2. **Alignment problems**
   - Use `align` environment
   - Check for missing `\\` line breaks
   - Verify matching braces

3. **Symbol size issues**
   - Use `\displaystyle` for full-size symbols
   - Check for proper delimiter sizing

### Getting Help
- Open an issue with the "math-rendering" label
- Include your browser information
- Attach screenshots of the problem
- Share the LaTeX source code 
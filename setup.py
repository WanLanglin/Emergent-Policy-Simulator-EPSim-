from setuptools import setup, find_packages

setup(
    name="epsim",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.3",
        "torch>=2.0.1",
        "geometric-algebra>=0.7.2",
        "scipy>=1.24.0",
        "networkx>=3.1.0",
        "matplotlib>=3.7.1",
        "tqdm>=4.65.0",
        "pandas>=2.0.3",
        "scikit-learn>=1.3.0",
        "pennylane>=0.31.0",
        "qiskit>=0.44.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.1",
            "pre-commit>=3.3.3",
            "jupyter>=1.0.0",
            "ipykernel>=6.25.1",
            "nbformat>=5.9.2"
        ],
        "docs": [
            "mkdocs-material>=9.1.21",
            "mkdocs-mermaid2-plugin>=0.6.0",
            "mkdocstrings>=0.22.0",
            "mkdocstrings-python>=1.1.2",
            "pymdown-extensions>=10.1",
            "pygments>=2.16.1"
        ]
    },
    python_requires=">=3.8",
    author="WanLanglin",
    author_email="wanlanglin@example.com",
    description="A quantum-classical hybrid optimization framework for policy manifold learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WanLanglin/Emergent-Policy-Simulator-EPSim-",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
) 
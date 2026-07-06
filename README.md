# LambertWCopula

A Python package for constructing, estimating, validating, and visualizing the **Lambert W Copula**, a novel copula family developed for flexible dependence modeling.

---

## Overview

LambertWCopula provides a complete workflow for copula analysis, including

- Maximum Likelihood Estimation (MLE)
- Empirical Copula Construction
- Theoretical Copula Surface
- Goodness-of-Fit Evaluation
- Bootstrap Inference
- Cross Validation
- Likelihood Profile Analysis
- Residual Diagnostics
- Dependence Diagnostics
- Automatic Statistical Interpretation
- HTML Report Generation
- Publication-Quality Figures

The package was developed as part of the research on the Lambert W Copula and is intended for statistical dependence modeling, applied probability, and multivariate data analysis.

---

## Installation

Clone the repository

```bash
git clone https://github.com/ontolanj-cell/LambertWCopula.git
```

Move into the project

```bash
cd LambertWCopula
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Analysis

Simply execute

```bash
python run_analysis.py
```

The program automatically

- imports the dataset
- preprocesses observations
- estimates the Lambert W Copula
- evaluates goodness-of-fit
- performs bootstrap inference
- performs cross-validation
- compares benchmark copulas
- generates publication-quality figures
- exports HTML, JSON, CSV, and text reports

---

## Project Structure

```text
LambertWCopula/

├── data/
├── figures/
├── reports/
├── lambertwcopula/
│   ├── analysis.py
│   ├── bootstrap.py
│   ├── comparison.py
│   ├── context.py
│   ├── cross_validation.py
│   ├── figure_manager.py
│   ├── html_report.py
│   ├── interpretation.py
│   ├── mle.py
│   ├── report_builder.py
│   ├── simulation.py
│   └── ...
│
└── run_analysis.py
```

---

## Current Features

- Empirical Copula
- Lambert W Copula
- Maximum Likelihood Estimation
- Fisher Information
- Wald Test
- Confidence Intervals
- Likelihood Profile
- Bootstrap Inference
- Cross Validation
- Residual Analysis
- Goodness-of-Fit Statistics
- Simulation
- Automatic Interpretation
- HTML Reports
- Publication Figures

---

## Planned Features

- Clayton Copula
- Frank Copula
- Gumbel Copula
- Student t Copula
- Joe Copula
- BB1 Copula
- Vine Copulas
- Automatic Model Selection
- PDF Report Generator
- Dashboard Interface

---

## Citation

If you use this software in academic research, please cite the associated Lambert W Copula publication.

Citation information will be added after publication.

---

## Author

Jay Ontolan
Cebu Normal University

---

## License

This project is currently released for academic research.

A formal open-source license will be added in a future release.
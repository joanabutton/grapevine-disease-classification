# Grapevine Disease Classification with Deep Learning

## Business Problem

Vineyard managers and agronomists need practical ways to identify potentially diseased vines from field observations so that limited inspection time can be focused where it is most useful.

## Project Objective

This project is a two-week university Deep Learning proof of concept. The goal is to explore whether a convolutional neural network (CNN) can classify visible grapevine disease symptoms from photographs taken in real vineyard conditions.

The intended use is decision support: helping prioritise vineyard inspection and follow-up by a human expert. This is not a production diagnostic system.

## Model Scope

The final proof-of-concept model will be a CNN image classifier for five target classes:

- healthy
- downy mildew
- powdery mildew
- Esca complex
- erineum mite

No production deployment, extensive hyperparameter optimisation, or automated diagnosis is in scope for this repository.

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_cnn_model.ipynb
│   └── 03_evaluation.ipynb
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── model.py
│   └── evaluation.py
├── figures/
├── results/
├── presentation/
└── docs/
```

## Environment Setup

Create and activate a Python virtual environment, then install the project dependencies:

```bash
python -m venv .venv
pip install -r requirements.txt
```

For VS Code, select the virtual environment as the notebook kernel after installing dependencies.

For Google Colab, upload or clone the repository, install any missing packages with `pip`, and mount external storage only when needed. Avoid absolute file paths so notebooks remain portable between local work and Colab GPU sessions.

## Running Notebooks

Run the notebooks in order:

1. `notebooks/01_eda.ipynb`
2. `notebooks/02_cnn_model.ipynb`
3. `notebooks/03_evaluation.ipynb`

All modelling should use the same train, validation, and test split so results remain comparable across the team.

## Team Workflow

- Keep the `main` branch stable.
- Each person should work on a feature branch.
- Use pull requests to merge work back into `main`.
- All modelling must use the same train/validation/test split.
- Avoid editing the same notebook simultaneously.

Suggested branch responsibilities:

- `business-research`
- `data-eda`
- `cnn-model`
- `evaluation`
- `integration`

## Future Work

Potential extensions after the proof of concept include:

- data augmentation
- transfer learning
- more diverse vineyard data
- confidence thresholds with human review
- geospatial disease mapping
- temporal monitoring
- disease severity prediction

These items are future possibilities and are not implemented in the current project scaffold.

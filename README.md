# Grapevine Disease Classification with Deep Learning

## Business Problem

Vineyard managers and agronomists need practical ways to identify potentially diseased vines from field observations so that limited inspection time can be focused where it is most useful.

## Project Objective

This project is a Deep Learning proof of concept. The goal is to explore whether a convolutional neural network (CNN) can classify visible grapevine disease symptoms from photographs taken in real vineyard conditions.

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

## Dataset

This project uses the **Grapevine Leaves RGB Images of Disease Symptoms**
dataset by Portela et al. (2026), collected under natural vineyard
conditions in northern Portugal.

- Dataset: https://zenodo.org/records/17343473
- DOI: https://doi.org/10.5281/zenodo.17343473
- Dataset paper: https://doi.org/10.1016/j.dib.2026.112743

The dataset contains five classes:
- Healthy
- Downy Mildew
- Powdery Mildew
- Esca Complex
- Erineum Mite


## Work distribution

**Person 1:** Business & Research
- Define the business problem and intended user.
- Explain what decision the system would support.
- Research the five grapevine conditions and relevant existing work.
- Explain why image classification and CNNs are appropriate.
- Develop the proposed next pilots: augmentation, transfer learning, confidence - thresholds, geospatial mapping, temporal monitoring, etc.
- Help shape the final presentation narrative.

**Person 2:** Data & EDA
- Download and document the dataset.
- Check number of images, classes, image sizes and data quality.
- Analyse class balance.
- Explore variation in lighting, backgrounds, orientation and disease appearance.
- Produce representative image grids and EDA visualisations.
- Summarise what the EDA implies for modelling.

**Person 3:** Preprocessing & Data Pipeline
- Define the train/validation/test split.
- Make the split reproducible using a fixed random seed.
- Implement image resizing and normalisation.
- Encode the five target classes.
- Build the data-loading pipeline used by the CNN.
- Check that there is no leakage between train, validation and test sets.
- Document the final model input shape and preprocessing steps.

**Person 4:** CNN Modelling
- Design a simple CNN appropriate for the images.
- Explain the Conv2D, pooling and Dense/output architecture.
- Choose loss function, optimiser and relevant training parameters.
- Train the model using Person 3's pipeline.
- Track training and validation loss/accuracy.
- Save the trained model, training history and predictions.
- Identify obvious signs of underfitting or overfitting.

**Person 5:** Evaluation & Integration
- Define the evaluation metrics.
- Calculate accuracy and per-class precision/recall/F1.
- Produce the confusion matrix and training curves.
- Examine examples of correct and incorrect predictions.
- Analyse why the CNN may be struggling with particular diseases/images.
- Translate results into business implications with Person 1.
- Act as technical integrator: keep the GitHub project coherent and make sure - everyone's work fits together.
- Coordinate the final technical conclusions.

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

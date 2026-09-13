# Grapevine Disease Classification with Deep Learning

## Business Problem

Vineyard managers and agronomists need practical ways to identify potentially diseased vines from field observations so that limited inspection time can be focused where it is most useful.

## Project Objective

This project is a Deep Learning proof of concept. The goal is to explore whether a convolutional neural network (CNN) can classify visible grapevine disease symptoms from photographs taken in real vineyard conditions.

The intended use is decision support: helping prioritise vineyard inspection and follow-up by a human expert. This is not a production diagnostic system.

## Model Scope

The final proof-of-concept model will be a CNN image classifier for four target classes:

- healthy
- black rot
- esca
- leaf blight

No production deployment, extensive hyperparameter optimisation, or automated diagnosis is in scope for this repository.

## Repository Structure

```text
.
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- data/
|   |-- README.md
|   |-- raw/
|   `-- processed/
|-- notebooks/
|   |-- 01_eda.ipynb
|   |-- 02_cnn_model.ipynb
|   `-- 03_evaluation.ipynb
|-- src/
|   |-- __init__.py
|   |-- preprocessing.py
|   |-- model.py
|   `-- evaluation.py
|-- figures/
|-- results/
|-- presentation/
`-- docs/
    |-- project_brief.md
    `-- ai_canvas.md
```

## Environment Setup

Create and activate a Python virtual environment for local work:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

For local EDA, preprocessing, evaluation, documentation, and notebook editing, install the lightweight dependencies:

```powershell
pip install numpy pandas matplotlib scikit-learn pillow jupyter ipykernel
```

For VS Code or Jupyter, select the virtual environment as the notebook kernel after installing dependencies. The local kernel for this project is:

```text
Python (.venv grapevine disease)
```

`requirements.txt` includes TensorFlow for Colab/model-training reproducibility. TensorFlow does not need to be installed locally unless you want to train or run the CNN on your own machine.

## Development Workflow

This project uses a hybrid workflow so that development stays manageable while CNN training can use GPU resources:

- **GitHub:** single source of truth for code, notebooks, documentation, and results.
- **VS Code/local `.venv`:** notebook editing, EDA, preprocessing, evaluation, documentation, and Git collaboration.
- **Google Colab:** CNN training using the notebook from this repository.
- **Google Drive:** temporary storage for the image dataset when running notebooks in Colab.

The CNN notebook in this repository is the same notebook used in Colab. Separate local and Colab versions should not be created.

Avoid absolute file paths so notebooks remain portable between local work and Colab GPU sessions.

## Running Notebooks

Run the notebooks in order:

1. `notebooks/01_eda.ipynb`
2. `notebooks/02_cnn_model.ipynb`
3. `notebooks/03_evaluation.ipynb`

All modelling should use the same train, validation, and test split so results remain comparable across the team.

## Project Brief and AI Canvas

The assignment brief is stored in `docs/project_brief.md`.

The project's AI Canvas is stored in `docs/ai_canvas.md`. It frames the model as a decision-support proof of concept for prioritising human vineyard inspection.

## Dataset

This project uses version 5 of the **GVLiD: GrapeVine Leaf identification of the Diseases** dataset by Shikalgar et al. (2026). It contains 3,477 high-resolution grape-leaf photographs captured during field visits from different angles.

- Dataset: https://data.mendeley.com/datasets/wkymf8bhcg/5
- DOI: https://doi.org/10.17632/wkymf8bhcg.5
- Licence: Creative Commons Attribution 4.0 (CC BY 4.0)

The dataset contains four classes:

- Healthy
- Black rot
- Esca
- Leaf blight

## Google Colab Training

CNN training is intended to be run in Google Colab when GPU access is useful. Open or upload the repository notebook in Colab, install any missing dependencies with `pip`, and save outputs that should be shared back into the repository.

### Dataset in Colab

The dataset is not stored in GitHub. When training in Colab, it can be stored in Google Drive and mounted with:

```python
from google.colab import drive
drive.mount('/content/drive')
```

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

## Work Distribution

**Person 1:** Business & Research

- Define the business problem and intended user.
- Explain what decision the system would support.
- Research the four grapevine conditions and relevant existing work.
- Explain why image classification and CNNs are appropriate.
- Develop the proposed next pilots: augmentation, transfer learning, confidence thresholds, geospatial mapping, temporal monitoring, etc.
- Help shape the final presentation narrative.

**Person 2:** Dataset Understanding & Problem Justification

- Download and document the dataset source, citation, class labels and image structure.
- Summarise only the EDA needed to support modelling: class counts, image dimensions, representative samples, image quality and split implications.
- Use the dataset documentation and relevant literature to explain why the problem matters in viticulture and why field-condition RGB images are appropriate.
- Identify dataset limitations that affect model interpretation, especially class imbalance, variation in capture angle and field conditions, possible similarity between visible symptoms, and uncertain generalisation to other vineyards, cultivars or seasons.
- Connect EDA findings to the AI Canvas and final business decision: prioritising human vineyard inspection, not automated diagnosis.

**Person 3:** Preprocessing & Data Pipeline

- Define the train/validation/test split.
- Make the split reproducible using a fixed random seed.
- Implement image resizing and normalisation.
- Encode the four target classes.
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
- Act as technical integrator: keep the GitHub project coherent and make sure everyone's work fits together.
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

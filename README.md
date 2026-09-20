# Grapevine Disease Classification with Deep Learning

## Business Problem

Wine is an important Portuguese industry, particularly in the North, where vineyards are widespread. Vineyard workers, managers and agronomists must monitor vines for visible signs of disease so that suspicious cases can receive timely expert assessment. The challenge is to help teams identify disease symptoms and prioritise which grapevines need expert inspection.

## Project Objective

This project evaluates whether a convolutional neural network (CNN) can use grapevine-leaf photographs to help prioritise which vines require expert inspection.

The intended use is human decision support. The CNN provides a triage signal; qualified agronomists retain responsibility for in-person inspection, diagnosis and treatment decisions. The project does not propose autonomous diagnosis.

## Model Scope

The selected proof-of-concept model classifies 128 x 128 RGB images into four folder-derived target classes:

- Black Rot
- Esca
- Healthy
- Leaf Blight

The model was evaluated both as a four-class classifier and as a binary decision-support view that groups the three diseases together. No production deployment or automated treatment recommendation is in scope.

## Repository Structure

```text
.
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- AI Value Sprint Canvas.pdf
|-- AI_DISCLOSURE.md
|-- data/
|   |-- README.md
|   |-- raw/                         # local GVLiD images; ignored by Git
|   `-- processed/
|       `-- dataset_split.csv        # fixed clean split used by Steps 5 and 6
|-- notebooks/
|   |-- step_1_brainstorming
|   |-- step_2_canvas.ipynb
|   |-- step_3_eda v2.ipynb
|   |-- step_4_dl_rationale.ipynb
|   |-- step_5_cnn_model_v2.ipynb
|   |-- step_6_evaluation_v2.ipynb
|   `-- step_7_conclusions.ipynb
|-- src/
|   |-- __init__.py
|   |-- preprocessing.py
|   |-- model.py
|   `-- evaluation.py
|-- results/
|   |-- cnn_v2_*_training_log.csv
|   |-- cnn_v2_*_training_history.pkl
|   `-- evaluation_v2/
`-- archive/                       # superseded notebook versions
```

## Environment Setup

Create and activate a Python virtual environment for local work:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Notebook 6 also uses Seaborn. If it is not already installed in the active environment, run:

```powershell
python -m pip install seaborn
```

Launch Jupyter from the project environment and select the `.venv` kernel:

```powershell
.\.venv\Scripts\jupyter-notebook.exe
```

TensorFlow is required for both model training and evaluation. A GPU is helpful for Step 5 training, but Step 6 evaluates only 362 test images and can run on a CPU.

## Development Workflow

The project supports a hybrid workflow:

- **GitHub:** single source of truth for code, notebooks, documentation, and results.
- **Local `.venv`:** EDA, notebook editing and CPU evaluation.
- **Google Colab:** optional GPU environment for CNN training or evaluation.
- **Google Drive:** storage for the raw dataset and `.keras` model when using Colab.

The raw images and trained `.keras` models are deliberately excluded from Git. In Colab, mount Drive and set the optional path overrides in the notebook configuration cells.

The notebooks discover the repository root and otherwise use relative paths so the same files can run locally or in Colab.

## Running Notebooks

Review or run the project steps in order:

1. [`step_1_brainstorming`](notebooks/step_1_brainstorming)
2. [`step_2_canvas.ipynb`](notebooks/step_2_canvas.ipynb)
3. [`step_3_eda v2.ipynb`](notebooks/step_3_eda%20v2.ipynb)
4. [`step_4_dl_rationale.ipynb`](notebooks/step_4_dl_rationale.ipynb)
5. [`step_5_cnn_model_v2.ipynb`](notebooks/step_5_cnn_model_v2.ipynb)
6. [`step_6_evaluation_v2.ipynb`](notebooks/step_6_evaluation_v2.ipynb)
7. [`step_7_conclusions.ipynb`](notebooks/step_7_conclusions.ipynb)

Steps 5 and 6 use the fixed [`dataset_split.csv`](data/processed/dataset_split.csv): 1,684 training images, 361 validation images and 362 test images. The test subset is not used for model fitting or model selection.

## AI Value Sprint Canvas

The final business canvas is provided as a notebook (step_2_canvas). It frames the model as a decision-support proof of concept for prioritising human vineyard inspection in Portugal.

## Dataset

This project uses version 5 of the **GVLiD: GrapeVine Leaf identification of the Diseases** dataset by Shikalgar et al. (2026). It contains 3,477 1080 x 1080 grape-leaf photographs captured in Indian vineyards.

- Dataset: https://data.mendeley.com/datasets/wkymf8bhcg/5
- DOI: https://doi.org/10.17632/wkymf8bhcg.5
- Licence: Creative Commons Attribution 4.0 (CC BY 4.0)

The dataset contains four classes:

- Healthy
- Black rot
- Esca
- Leaf blight

### Data integrity and modelling sample

SHA-256 hashing identified substantial exact duplication and two hashes assigned to conflicting classes. The raw dataset remains unchanged. The modelling workflow excludes redundant copies and the two conflicting hash groups, producing 2,407 usable unique images.

The supplied metadata also conflicts systematically with the Healthy and Leaf Blight folders. The modelling target is therefore derived consistently from the resolved class folder. This is a provisional label decision, not expert-verified ground truth, and is treated as a limitation throughout the project.

## Selected CNN

The baseline CNN uses three convolution and max-pooling blocks, global average pooling, a dense layer and a four-class softmax output. Training images receive moderate geometric augmentation and class weights address the remaining imbalance.

Four controlled experiments changed one choice at a time: batch size, class weighting, learning rate and dropout. The dropout-0.40 configuration achieved the lowest validation loss (0.4251) and was selected for final evaluation. The required model file is:

```text
results/cnn_v2_dropout040_best.keras
```

The `.keras` model is ignored by Git because it is a generated binary artifact. Obtain it from the Step 5 training run or the team storage location before running Step 6.

## Final Evaluation Results

The selected checkpoint was evaluated on the untouched 362-image test subset.

| Metric | Result |
| --- | ---: |
| Test accuracy | 82.04% |
| Majority-class baseline | 45.30% |
| Macro F1 | 68.05% |
| Weighted F1 | 81.59% |

Class-level performance was uneven:

| Class | Recall | F1-score | Test support |
| --- | ---: | ---: | ---: |
| Black Rot | 46.67% | 50.00% | 15 |
| Esca | 88.72% | 81.66% | 133 |
| Healthy | 92.68% | 95.60% | 164 |
| Leaf Blight | 40.00% | 44.94% | 50 |

For the proposed inspection-triage decision, the four classes were also grouped into Healthy versus Disease:

| Triage metric | Result |
| --- | ---: |
| Disease precision | 94.23% |
| Disease recall | 98.99% |
| Disease F1 | 96.55% |
| Images flagged for expert review | 57.46% |

The model flagged 196 of 198 diseased test images, missed two and unnecessarily flagged 12 healthy images. It made 65 four-class errors, including seven with confidence of at least 80%. High softmax confidence is therefore not treated as diagnostic certainty.

Detailed outputs are stored in [`results/evaluation_v2`](results/evaluation_v2), including the classification report, confusion matrices, test predictions, triage metrics and error-analysis figure.


## Business Interpretation

The model is more reliable at distinguishing Healthy from Disease than at naming the specific disease. The evidence supports a limited, expert-supervised triage pilot, not stand-alone diagnosis or production deployment.

In the proposed workflow, vineyard workers collect photographs through systematic sampling, the CNN prioritises potential disease cases, and agronomists inspect flagged vines in situ. Routine monitoring continues regardless of the prediction, and agronomists retain all diagnosis and treatment decisions.

Before operational use, the workflow should be tested using expert-validated Portuguese vineyard images. A parallel pilot should compare inspection time, missed disease, false alarms, class-level recall and agronomist workload with the existing manual process.

## Limitations

- The cleaned images come from Indian vineyards; performance in Portuguese vineyards is untested.
- Folder-derived targets are provisional because the supplied metadata and folders conflict.
- Black Rot and Leaf Blight have limited test support and weak recall.
- Some incorrect predictions receive high confidence.
- The current results do not demonstrate time savings, cost savings or improved field detection rates.

## AI Use Disclosure

Permitted AI assistance used during the project is documented in [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md). Final problem framing, modelling choices, interpretation, conclusions and submission decisions remain the responsibility of the project team.

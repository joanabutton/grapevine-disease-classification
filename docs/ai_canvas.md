# AI Canvas

This canvas connects the grapevine disease classification model to the business and operational decision required by the project brief.

## Prediction

Which visible condition is most likely shown in a grapevine leaf image?

Target classes:

- healthy
- downy mildew
- powdery mildew
- Esca complex
- erineum mite

## Judgment

The model is intended to support inspection priorities, so errors do not have equal consequences.

- False negatives may leave potentially diseased vines without timely follow-up.
- False positives may use agronomist or vineyard manager time unnecessarily.
- Confusion between disease types matters because different conditions may require different expert follow-up.
- Low-confidence predictions should be treated as cases for human review.

## Action

The model output should help decide which vines or images deserve earlier human inspection.

It should not automatically diagnose disease, recommend treatment or trigger spraying without expert confirmation.

## Outcome

Success should be judged by whether the model can support better triage in a proof-of-concept setting.

Relevant measures:

- overall accuracy
- per-class precision, recall and F1-score
- confusion matrix patterns
- examples of correct and incorrect classifications
- practical interpretation of which classes are reliable enough for decision support

## Input

At use time, the input would be RGB photographs of grapevine leaves captured in field conditions, ideally using a consistent image capture process.

## Training

The proof of concept uses the Grapevine Leaves RGB Images of Disease Symptoms dataset by Portela et al. (2026).

Dataset source: https://zenodo.org/records/17343473

Dataset paper: https://doi.org/10.1016/j.dib.2026.112743

The dataset is appropriate because it contains labelled RGB leaf images collected under natural vineyard conditions, which is closer to the intended operational setting than laboratory images with controlled backgrounds.

## Feedback

A future pilot would need feedback from agronomists or vineyard managers after field inspection.

Useful feedback would include:

- whether the predicted class was confirmed by an expert
- whether the image was too ambiguous for reliable classification
- whether a different disease, pest or abiotic stress was present
- whether the prediction changed inspection or monitoring decisions
- whether new vineyards, cultivars or seasons introduce patterns not represented in the training data

## Main Limitations

The current model should be interpreted as a proof of concept because the dataset labels are based on visible symptoms rather than laboratory-confirmed diagnoses. The dataset also has uneven temporal and spatial coverage, limited cultivar coverage, natural lighting variation and possible overlap between symptoms.

These limitations mean the model is best framed as inspection support, not automated disease diagnosis.

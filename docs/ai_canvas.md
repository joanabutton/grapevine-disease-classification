# AI Canvas

This canvas connects the grapevine disease classification model to the business and operational decision required by the project brief.

## Prediction

Which visible condition is most likely shown in a grapevine leaf image?

Target classes:

- healthy
- black rot
- esca
- leaf blight

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

The proof of concept uses version 5 of the GVLiD: GrapeVine Leaf identification of the Diseases dataset by Shikalgar et al. (2026).

Dataset source: https://data.mendeley.com/datasets/wkymf8bhcg/5

Dataset DOI: https://doi.org/10.17632/wkymf8bhcg.5

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

The current model should be interpreted as a proof of concept. The local dataset has unequal class sizes, and field-acquired images may vary in angle, lighting, background and symptom visibility. Similar visible symptoms may be difficult to distinguish, and performance on this dataset may not generalise to other vineyards, cultivars, devices or seasons.

These limitations mean the model is best framed as inspection support, not automated disease diagnosis.

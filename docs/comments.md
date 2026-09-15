- **Business canvas:** we are still referring to the old dataset in Evidence from Reality. DONE
- **Eval:** Evaluation is using the original metadata column and not the reconstructed test labels - we need to fix it. DONE

## **General comments CODEX beginning of 20260915 meeting:**

Overall verdict
The corrected V2 evaluation now uses the right labels and runs consistently. The model shows a promising disease-triage signal, but the dataset contains extensive duplicate-image leakage across training, validation, and test sets. Therefore, the reported 73.5% accuracy cannot yet be presented as reliable performance on genuinely unseen images.
My recommendation is: continue the proof of concept, but No-Go for operational use—and ideally deduplicate, retrain, and reevaluate before submission.
What now looks correct
The executed [V2 evaluation notebook](C:\\Users\\joani\\Projects\\EXEC MASTERS IN BUSINESS ANALYTICS AND AI\\Deep_Learning\\grapevine_disease_classification\\notebooks\\step_6_evaluation_v2.ipynb) passed its safeguards:
- All 3,477 manifest records resolved to images.
- The folder-derived target used in Notebook 5 was used consistently.
- Disease_Type was retained only for auditing.
- Model shape and four-class output were verified.
- The test set was not shuffled.
- model.evaluate() and independently calculated accuracy agreed.
- Predictions, probabilities, metrics and figures were saved correctly.
The corrected headline results are:
- Accuracy: 73.5%
- Majority baseline: 32.2%
- Macro F1: 69.9%
- Weighted F1: 74.1%
These are internally correct for the current split.
Model interpretation
The per-class results tell a more useful story than overall accuracy:
- Healthy: excellent—94.8% recall and 98.0% precision.
- Esca: good detection—79.0% recall, although precision is lower at 63.6%.
- Black Rot: predictions are usually correct when made, but recall is only 57.5%.
- Leaf Blight: weakest class—47.4% recall and 38.5% precision.
The largest errors are:
- 39 Black Rot images classified as Leaf Blight.
- 36 Leaf Blight images classified as Esca.
- 20 Esca images classified as Leaf Blight.
So the CNN is considerably better at separating healthy from diseased leaves than at distinguishing the individual diseases.
The triage results illustrate that:
- 319 of 322 diseased images were flagged as disease.
- Only three diseased images were incorrectly classified as Healthy.
- Eight Healthy images were unnecessarily flagged.
- 68.8% of images would be sent for expert review.
That supports your Step 7 concept—but only as a preliminary dataset result, not yet evidence of field readiness.
Major problem: duplicate-image leakage
Exact SHA-256 hashing found:
- 3,477 records but only 2,409 unique image contents.
- 1,068 records are redundant copies.
- Black Rot: 808 records but only 99 unique images.
- Leaf Blight: 672 records but only 331 unique images.
- 236 duplicate groups cross dataset splits.
- 182 of 475 test records have an exact copy in training.
- All 120 Black Rot test records have an exact duplicate in training.
- Validation is also contaminated, so training decisions based on validation loss are not completely independent.
- Two identical-image hashes even appear under different class folders.
This is more serious than the earlier metadata issue. The vineyard split did not prevent leakage because identical photographs were assigned different filenames and sometimes different vineyards.
It does not automatically mean that every metric is inflated—the duplicated test records actually performed worse in this particular run—but it means the test set is not an independent test of generalisation. The Black Rot result is particularly difficult to interpret.
The correct technical remedy is:
1. Hash every image.
2. Remove exact duplicates or group identical hashes together.
3. Remove or manually resolve hashes appearing under conflicting classes.
4. Create new train/validation/test splits with no hash overlap.
5. Retrain the CNN from scratch.
6. Run V2 evaluation again.
Simply reevaluating the existing model after removing leaked test images is insufficient because the remaining subset contains no Black Rot cases and only 16 Leaf Blight cases.
Documentation issues before submission
Several artifacts still contradict one another:
- The committed canvas PDF still describes the obsolete five-class Portela dataset from northern Portugal. It is visually clear, but factually inconsistent with the four-class GVLiD model. AI Value Sprint Canvas Group 4.pdf
- docs/comments.md currently says that the canvas correction is “DONE,” but the PDF has not been corrected.
- The README still lists the old notebook filenames and omits Steps 4, 6 V2, and 7.
- The original invalid Step 6 and original results remain beside V2, which could confuse the teacher.
- The project brief and task-distribution document disagree about who owns Steps 3 and 7.
- Step 1 currently contains five ideas in bullets; the instructions request two or three ideas summarised as a paragraph.
- [Step 7](C:\\Users\\joani\\Projects\\EXEC MASTERS IN BUSINESS ANALYTICS AND AI\\Deep_Learning\\grapevine_disease_classification\\notebooks\\step_7) is still a rough outline, contains typos, and introduces automatic in-situ cameras without those being part of the tested workflow.
- “Treatment as the agronomist sees fit” should be rephrased so it is clear that treatment is determined independently by the expert, not recommended by the CNN.
A defensible final conclusion would be:
The CNN demonstrated a promising ability to distinguish apparently healthy from diseased images in the current dataset, but its disease-specific classification was uneven, particularly for Leaf Blight. In addition, metadata conflicts and exact duplicate images crossing the dataset splits limit the reliability of the reported test performance. The model should therefore be treated as an exploratory proof of concept. The next stage should deduplicate and relabel the data, retrain using leakage-free splits, and validate the workflow with vineyard professionals before any controlled field pilot.

No project files were edited during this review. I also noticed concurrent local changes to docs/comments.md and a new untracked docs/20260915_group_work; I left both untouched.
- Fix duplicate leakage
- Polish Step 7
- Audit submission artifacts

## Solution for duplicates:

A safe workflow would be:
1. Preserve the original dataset unchanged.
2. Calculate a SHA-256 hash for every image.
3. Group rows with the same hash.
4. Keep one representative image from each duplicate group.
5. If identical images appear under different classes, manually review or exclude that entire group.
6. Create a new train/validation/test split from the deduplicated data.
7. Confirm that no hash occurs in more than one split.
8. Retrain the CNN from scratch.
9. Evaluate the newly trained model on the new test set.
Conceptually:
```
3,477 records
      ↓ calculate SHA-256
2,409 unique image groups
      ↓ resolve conflicting labels
deduplicated dataset
      ↓ create new split
train / validation / test with zero hash overlap
      ↓
retrain and reevaluate
```
For this project, I would recommend creating a new auditable manifest such as:
```
image_filename
sha256
target_class
vineyard
duplicate_group_size
keep_for_modelling
exclusion_reason
split_v2
```
Important decisions:
- For duplicates with the same class, keep one copy.
- For identical content assigned different classes, exclude the group unless an expert can confirm the correct label.
- Do not delete the original files; simply mark which records are included.
- Preserve the current model and results as the original comparison, clearly labelled as using the contaminated split.
- Do not reuse the current trained model: it has already learned from the duplicate-containing training set.

There is also a complication with the vineyard metadata. Identical photographs have sometimes been assigned to different vineyards. That means the current vineyard field cannot be trusted blindly for those duplicate groups. For a short coursework project, a defensible approach would be:
- deduplicate by SHA-256;
- exclude conflicting-label groups;
- make a reproducible class-stratified split of the unique images;
- clearly explain why the original vineyard-based split was abandoned.

After exact deduplication, you could optionally check for resized or edited duplicates using perceptual hashing. Given the deadline, exact SHA-256 deduplication plus a transparent limitation statement would be a reasonable minimum.
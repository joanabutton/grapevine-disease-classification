# Data Directory

Do not commit dataset files to GitHub.

Place original dataset files in `data/raw/`. Raw data should remain unchanged so the source material can always be traced.

Place derived data in `data/processed/` only if needed, such as resized images, cleaned metadata, or train/validation/test split folders.

The expected target classes are:

- healthy
- downy mildew
- powdery mildew
- Esca complex
- erineum mite

Document the public dataset source here once it has been selected, including the dataset name, URL, licence or usage terms, download date, and any relevant citation.

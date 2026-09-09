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

Selected dataset:

- Name: Grapevine Leaves RGB Images of Disease Symptoms
- Authors: Portela et al. (2026)
- Dataset URL: https://zenodo.org/records/17343473
- DOI: https://doi.org/10.5281/zenodo.17343473
- Dataset paper: https://doi.org/10.1016/j.dib.2026.112743
- Usage note: do not commit dataset files to GitHub. Check the Zenodo record for the current dataset licence or usage terms before any redistribution.

Recommended citation:

Portela, F., Carneiro, G., Ferreira, L., Paredes, C. A., Sousa, J. J., Peres, E., Morais, R., & Padua, L. (2026). Dataset of RGB images of healthy grapevine leaves and with downy mildew, powdery mildew, Esca complex, and erineum mite symptoms. Data in Brief, 66, 112743. https://doi.org/10.1016/j.dib.2026.112743

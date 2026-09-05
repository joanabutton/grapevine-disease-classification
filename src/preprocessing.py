"""Preprocessing helpers for grapevine disease image data."""

from pathlib import Path
from typing import Iterable

from . import RANDOM_SEED


def load_images(data_dir: Path | str, class_names: Iterable[str] | None = None) -> list[Path]:
    """Return image paths from a dataset directory.

    Parameters
    ----------
    data_dir:
        Directory containing image files, usually organised by class folder.
    class_names:
        Optional class folder names to include.

    Returns
    -------
    list[Path]
        Image file paths discovered in the requested directory.
    """
    raise NotImplementedError("Image loading will be implemented during the EDA stage.")


def preprocess_image(image_path: Path | str, image_size: tuple[int, int]) -> object:
    """Prepare one image for model input.

    Parameters
    ----------
    image_path:
        Path to the source image.
    image_size:
        Target image size as ``(height, width)``.

    Returns
    -------
    object
        Preprocessed image array or tensor, depending on the modelling workflow.
    """
    raise NotImplementedError("Image preprocessing will be implemented during modelling.")


def create_dataset_split(
    image_paths: Iterable[Path | str],
    labels: Iterable[str],
    test_size: float = 0.2,
    validation_size: float = 0.2,
    random_seed: int = RANDOM_SEED,
) -> object:
    """Create reproducible train, validation, and test splits.

    Parameters
    ----------
    image_paths:
        Image paths to split.
    labels:
        Class labels aligned with ``image_paths``.
    test_size:
        Proportion of examples reserved for testing.
    validation_size:
        Proportion of remaining training examples reserved for validation.
    random_seed:
        Fixed seed used for reproducibility across the team.

    Returns
    -------
    object
        Split data structure to be defined during the EDA stage.
    """
    raise NotImplementedError("Dataset splitting will be implemented after data review.")

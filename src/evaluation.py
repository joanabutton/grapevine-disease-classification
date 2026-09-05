"""Evaluation helpers for grapevine disease classification outputs."""

from typing import Iterable


def evaluate_predictions(y_true: Iterable[str], y_pred: Iterable[str]) -> dict[str, object]:
    """Calculate classification metrics from true and predicted labels.

    Parameters
    ----------
    y_true:
        Ground-truth class labels.
    y_pred:
        Predicted class labels.

    Returns
    -------
    dict[str, object]
        Metric outputs such as accuracy and per-class precision, recall, and F1.
    """
    raise NotImplementedError("Prediction metrics will be implemented during evaluation.")


def plot_confusion_matrix(
    y_true: Iterable[str],
    y_pred: Iterable[str],
    class_names: Iterable[str],
) -> object:
    """Plot a confusion matrix for the classifier output.

    Parameters
    ----------
    y_true:
        Ground-truth class labels.
    y_pred:
        Predicted class labels.
    class_names:
        Ordered class labels for the matrix axes.

    Returns
    -------
    object
        Plot object or axes to be defined during evaluation.
    """
    raise NotImplementedError("Confusion matrix plotting will be implemented during evaluation.")

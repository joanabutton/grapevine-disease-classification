"""Model-building helpers for the grapevine disease classification PoC."""


def build_cnn_model(
    input_shape: tuple[int, int, int],
    num_classes: int = 5,
) -> object:
    """Build a CNN image classifier.

    Parameters
    ----------
    input_shape:
        Input image shape as ``(height, width, channels)``.
    num_classes:
        Number of disease classes to predict.

    Returns
    -------
    object
        Compiled or uncompiled model object, depending on the modelling workflow.
    """
    raise NotImplementedError("CNN architecture will be implemented in the modelling stage.")

# check if pytorch is installed
try:
    import torch
except ImportError:
    raise ImportError(
        "PyTorch is not installed and cannot be installed automatically. "
        "Please find your respective installation command at https://pytorch.org/get-started/locally/"
    )

__all__ = []

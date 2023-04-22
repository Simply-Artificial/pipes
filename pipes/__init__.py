# check if pytorch is installed
try:
    import torch
except ImportError:
    raise ImportError(
        "PyTorch is not installed and cannot be installed automatically. "
        "Please find your respective installation command at https://pytorch.org/get-started/locally/"
    )

from pipes.BetterConversations import BetterConversation
from pipes.SADispatch import (
    SADispatchPathway,
    SADispatchPathingCollection,
    SADispatchKeywordDetection,
    SADispatchQuestionDetection,
    get_synonyms,
    SADispatchPipeline
)

__all__ = [
    "BetterConversation",
    "SADispatchPathway",
    "SADispatchPathingCollection",
    "SADispatchKeywordDetection",
    "SADispatchQuestionDetection",
    "get_synonyms",
    "SADispatchPipeline"
]

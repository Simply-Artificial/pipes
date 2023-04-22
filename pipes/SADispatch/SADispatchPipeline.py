from pipes.SADispatch.SADispatchPathing import SADispatchPathway, SADispatchPathingCollection
from pipes.SADispatch.SADispatchKeywordDetection import SADispatchKeywordDetection
from pipes.SADispatch.SADispatchQuestionDetection import SADispatchQuestionDetection
from pipes.SADispatch.SADispatchSynonymFetcher import get_synonyms
from pipes.NLTKPipeline import NLTKPipeline

__all__ = ["SADispatchPipeline"]

#   NOTICE
# This is not complete yet, this is a working prototype without AI capabilities, just simple keyword matching.


class SADispatchPipeline(NLTKPipeline):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._kw = None
        self._qd = None
        self._nodes = None

    def _sanitize_parameters(self, **kwargs):
        preprocess_kwargs = {}
        forward_kwargs = {}
        postprocess_kwargs = {}

        if "nodes" in kwargs:
            if isinstance(kwargs["nodes"], SADispatchPathingCollection):
                preprocess_kwargs["nodes"] = kwargs["nodes"]
            else:
                raise TypeError(f"Expected SADispatchPathingCollection, got {type(kwargs['nodes'])}")

        return preprocess_kwargs, forward_kwargs, postprocess_kwargs

    def preprocess(self, inputs, nodes: SADispatchPathingCollection = None):
        self._kw = SADispatchKeywordDetection()
        self._qd = SADispatchQuestionDetection()

        self._nodes = nodes

        return {"model_input": inputs}

    def _forward(self, model_inputs):
        model_outputs = {
            "inputs": model_inputs["model_input"],
            "path": [
                self._nodes.get("SATextClassification")
            ]
        }

        kw = self._kw.keywords(model_inputs["model_input"])
        qd = self._qd.classify(model_inputs["model_input"])
        path_discovered = False

        if qd != "Statement":
            model_outputs["path"].append(self._nodes.get("SAQuestionAnswering"))
            path_discovered = True

        if kw:
            for i in kw:
                if i[0] in get_synonyms("summarise") and i[1] >= 0.5:
                    model_outputs["path"].append(self._nodes.get("SASummarization"))
                    path_discovered = True
                    break

        if not path_discovered:
            model_outputs["path"].append(self._nodes.get("SAConversation"))


        return model_outputs

    def postprocess(self, model_outputs):
        return model_outputs

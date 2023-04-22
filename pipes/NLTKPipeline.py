from abc import abstractmethod


class NLTKPipeline:
    @abstractmethod
    def _sanitize_parameters(self, **call_params):
        raise NotImplementedError

    @abstractmethod
    def preprocess(self, inputs, **preprocess_params) -> dict:
        raise NotImplementedError

    @abstractmethod
    def _forward(self, inputs, **forward_params) -> dict:
        raise NotImplementedError

    @abstractmethod
    def postprocess(self, outputs, **postprocess_params) -> dict:
        raise NotImplementedError

    def __call__(self, inputs, **kwargs):
        preprocess_params, forward_params, postprocess_params = self._sanitize_parameters(**kwargs)

        model_inputs = self.preprocess(inputs, **preprocess_params)
        model_outputs = self._forward(model_inputs, **forward_params)
        return self.postprocess(model_outputs, **postprocess_params)



import yake

__all__ = ["SADispatchKeywordDetection"]


class SADispatchKeywordDetection:
    def __init__(self, max_ngram_size=1) -> None:
        self.kw: yake.KeywordExtractor = yake.KeywordExtractor(n=max_ngram_size)

    def keywords(self, inputs: str) -> list[tuple]:
        return self.kw.extract_keywords(inputs)

from nltk.corpus import wordnet

__all__ = ['get_synonyms']


def get_synonyms(word: str) -> list[str]:
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    return synonyms

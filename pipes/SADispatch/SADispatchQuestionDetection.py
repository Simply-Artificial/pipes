import nltk

__all__ = ['SADispatchQuestionDetection']


class SADispatchQuestionDetection:
    def __init__(self) -> None:
        try:
            self.posts = nltk.corpus.nps_chat.xml_posts()[:10000]
        except LookupError:
            nltk.download('nps_chat')
            self.posts = nltk.corpus.nps_chat.xml_posts()[:10000]

        self._featuresets = [(_dialogue_act_features(post.text), post.get('class')) for post in self.posts]
        self._size = int(len(self._featuresets) * 0.1)
        self._train_set, self._test_set = self._featuresets[self._size:], self._featuresets[:self._size]
        self.classifier = nltk.NaiveBayesClassifier.train(self._train_set)

    @property
    def accuracy(self) -> float:
        return nltk.classify.accuracy(self.classifier, self._test_set)

    def classify(self, inputs: str) -> str:
        return self.classifier.classify(_dialogue_act_features(inputs))


def _dialogue_act_features(post) -> dict[str, bool]:
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features


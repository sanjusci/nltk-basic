
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


import random
from nltk import FreqDist
from nltk.corpus import movie_reviews


class TextClassificationFeature(object):
    """
    we're going to be building off the previous video and compiling feature lists of words from positive
    reviews and words from the negative reviews to hopefully see trends in specific types of words in positive
    or negative reviews.
    """
    word_features = []

    def __init__(self):
        self.documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

    def process_content(self):
        """

        :return:
        """
        random.shuffle(self.documents)
        all_words = []
        for w in movie_reviews.words():
            all_words.append(w.lower())
        all_words = FreqDist(all_words)
        self.word_features = list(all_words.keys())[:3000]

    def find_features(self, document):
        words = set(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)
        return features


if __name__ == "__main__":

    tk = TextClassificationFeature()
    tk.process_content()
    print((tk.find_features(movie_reviews.words('neg/cv000_29416.txt'))))


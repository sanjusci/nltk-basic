
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


import random
from nltk import FreqDist
from nltk.corpus import movie_reviews


class TextClassification(object):
    """
     We're going to start by trying to use the movie reviews database that is part of the NLTK corpus. From there
     we'll try to use words as "features" which are a part of either a positive or negative movie review.
     The NLTK corpus movie_reviews data set has the reviews, and they are labeled already as positive or negative.
    """

    def __init__(self):
        self.documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

    def process_content(self):
        """

        :return:
        """
        random.shuffle(self.documents)
        print(self.documents[1])
        all_words = []
        for w in movie_reviews.words():
            all_words.append(w.lower())
        all_words = FreqDist(all_words)
        print(all_words.most_common(15))
        print(all_words["stupid"])


if __name__ == "__main__":

    tk = TextClassification()
    tk.process_content()


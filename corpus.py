
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg


class Corpus(object):
    """
     We're going to talk about accessing these documents via NLTK.
     As you can see, these are mostly text documents, so you could just use normal Python code to open and read
     documents. That said, the NLTK module has a few nice methods for handling the corpus, so you may find it useful
     to use their methology.
    """

    def __init__(self, file_name):
        self.sample = gutenberg.raw(file_name)

    def process_content(self):
        """

        :return:
        """
        tok = sent_tokenize(self.sample)
        for x in range(5):
            print(tok[x])


if __name__ == "__main__":

    tk = Corpus("bible-kjv.txt")
    tk.process_content()



__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


from nltk.stem import WordNetLemmatizer


class Lemmatization(object):
    """
     A very similar operation to stemming is called lemmatizing.
     The major difference between these is, as you saw earlier, stemming can often create non-existent words,
      whereas lemmas are actual words.
    """

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def process_content(self):
        """

        :return:
        """
        print(self.lemmatizer.lemmatize("cats"))
        print(self.lemmatizer.lemmatize("cacti"))
        print(self.lemmatizer.lemmatize("geese"))
        print(self.lemmatizer.lemmatize("rocks"))
        print(self.lemmatizer.lemmatize("python"))
        print(self.lemmatizer.lemmatize("better", pos="a"))
        print(self.lemmatizer.lemmatize("best", pos="a"))
        print(self.lemmatizer.lemmatize("run"))
        print(self.lemmatizer.lemmatize("run", 'v'))


if __name__ == "__main__":

    tk = Lemmatization()
    tk.process_content()


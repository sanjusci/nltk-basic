__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


# I was taking a ride in the car.
# I was riding in the car.

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()


class Stemming(object):
    def __init__(self, example_words):
        self.example_words = example_words

    def stemm(self):
        for w in self.example_words:
            print(ps.stem(w), end='\n')
        print(end='---------------\n')
if __name__ == '__main__':
    example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
    s = Stemming(example_words)
    s.stemm()

    eg_text = "This is an obviously massive challenge, but there are steps to doing it that anyone can follow." \
              " The main idea, however, is that computers simply do not, and will not, ever understand words" \
              " directly. Humans don't either *shocker*. In humans, memory is broken down into electrical signals" \
              " in the brain, in the form of neural groups that fire in patterns. There is a lot about the brain " \
              "that remains unknown, but, the more we break down the human brain to the basic elements, we find " \
              "out basic the elements really are. Well, it turns out computers store information in a very similar " \
              "way! We need a way to get as close to that as possible if we're going to mimic how humans read and " \
              "understand text. Generally, computers use numbers for everything, but we often see directly in" \
              " programming where we use binary signals (True or False, which directly translate to 1 or 0," \
              " which originates directly from either the presence of an electrical signal (True, 1), or not" \
              " (False, 0)). To do this, we need a way to convert words to values, in numbers, or signal patterns." \
              " The process of converting data to something a computer can understand is referred to as " \
              " One of the major forms of pre-processing is going to be filtering out useless data. In natural" \
              " language processing, useless words (data), are referred to as stop words."

    s.__init__(word_tokenize(eg_text))
    s.stemm()

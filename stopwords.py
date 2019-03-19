__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
# tokenizing - word tokenizer. .... sentence tokenizer
# lexicon and corporas


class Stopwords(object):

    def __init__(self, text):
        self.text = text

    def sent_tokenizer(self):
        return sent_tokenize(self.text)

    def word_tokenizer(self):
        return word_tokenize(self.text)


if __name__ == "__main__":
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

    sw = Stopwords(eg_text)
    stop_words = set(stopwords.words('english'))
    # filtered_words = []
    # for w in sw.word_tokenizer():
    #     if w not in stop_words:
    #         filtered_words.append(w)
    filtered_words = [w for w in sw.word_tokenizer() if w not in stop_words]
    print(stop_words)
    print(filtered_words)


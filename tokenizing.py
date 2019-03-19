__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

from nltk.tokenize import word_tokenize, sent_tokenize
from helper import Helper
# tokenizing - word tokenizer. .... sentence tokenizer
# lexicon and corporas


class Tokenizer(object):

    def __init__(self, text):
        self.text = text

    def sent_tokenizer(self):
        return sent_tokenize(self.text)

    def word_tokenizer(self):
        return word_tokenize(self.text)


if __name__ == "__main__":
    eg_text = "Lorem Ipsum छपाई और अक्षर योजन उद्योग का एक साधारण डमी पाठ है." \
              " Lorem Ipsum सन १५०० के बाद से अभी तक इस उद्योग का मानक डमी पाठ मन गया, जब एक अज्ञात मुद्रक ने नमूना लेकर एक " \
              "नमूना किताब बनाई. यह न केवल पाँच सदियों से जीवित रहा बल्कि इसने इलेक्ट्रॉनिक मीडिया में छलांग लगाने के बाद भी मूलतः अपरिवर्तित" \
              " रहा. यह 1960 के दशक में Letraset Lorem Ipsum अंश युक्त पत्र के रिलीज के साथ लोकप्रिय हुआ, और हाल ही में Aldus" \
              " PageMaker Lorem Ipsum के संस्करणों सहित तरह डेस्कटॉप प्रकाशन सॉफ्टवेयर के साथ अधिक प्रचलित हुआ."

    tk = Tokenizer(eg_text)
    for st in tk.sent_tokenizer():
        print(st)
    for w in tk.word_tokenizer():
        print(w)


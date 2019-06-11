
__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


from nltk import pos_tag, RegexpParser
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


class Chinking(object):

    def __init__(self, train_text, sample_text):
        self.train_text = state_union.raw(train_text)
        self.sample_text = state_union.raw(sample_text)
        self.custom_sent_tokenizer = PunktSentenceTokenizer(self.train_text)
        self.tokenized = self.custom_sent_tokenizer.tokenize(self.sample_text)

    def process_content(self):
        try:
            for i in self.tokenized:
                words = word_tokenize(i)
                tagged = pos_tag(words)
                chunkGram = r"""Chunk: {<.*>+}
                            }<VB.?|IN|DT|TO>+{"""
                chunkParser = RegexpParser(chunkGram)
                chunked = chunkParser.parse(tagged)
                for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                    print(subtree)
                chunked.draw()
        except Exception as e:
            print(str(e))


if __name__ == "__main__":

    tk = Chinking("2005-GWBush.txt", "2006-GWBush.txt")
    tk.process_content()


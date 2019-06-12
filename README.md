#
NLTK basic learning for beginners.
# Natural Language  Processing (Python)

## Index
* [Topics](https://github.com/sanjusci/nltk-basic#topics)
  * [Tokenizing](https://github.com/sanjusci/nltk-basic#tokenizing)
  * [Stopwords](https://github.com/sanjusci/nltk-basic#stopwords)
  * [Stemming](https://github.com/sanjusci/nltk-basic#stemming)
  * [Chunking](https://github.com/sanjusci/nltk-basic#chunking)
  * [Chinking](https://github.com/sanjusci/nltk-basic#chinking)
  * [NamedEntityRecognization](https://github.com/sanjusci/nltk-basic#namedentityrecognization)
  * [Lemmatization](https://github.com/sanjusci/nltk-basic#lemmatization)
  * [Corpus](https://github.com/sanjusci/nltk-basic#corpus)
  * [TextClassification](https://github.com/sanjusci/nltk-basic#TextClassification)
  * [TextClassificationfeature](https://github.com/sanjusci/nltk-basic#TextClassificationfeature)
  * [How to run?](https://github.com/sanjusci/nltk-basic#how-to-run)

## Topics

### Tokenizing
* [Words/Sentences Tokenizing](https://github.com/sanjusci/nltk-basic/blob/master/tokenizing.py)

### Stopwords
* [Stop Words](https://github.com/sanjusci/nltk-basic/blob/master/stopwords.py)

### Stemming
* [Stemming](https://github.com/sanjusci/nltk-basic/blob/master/stemming.py)

### Chunking
* [Chunking](https://github.com/sanjusci/nltk-basic/blob/master/chunking.py)

### Chinking
* [Chinking](https://github.com/sanjusci/nltk-basic/blob/master/chinking.py)

### NamedEntityRecognization
* [NamedEntityRecognization](https://github.com/sanjusci/nltk-basic/blob/master/ner.py)

### Lemmatization
* [Lemmatization](https://github.com/sanjusci/nltk-basic/blob/master/lemmatization.py)

### Corpus accessing documents via NLTK
* [Corpus](https://github.com/sanjusci/nltk-basic/blob/master/corpus.py)

### TextClassification via NLTK
* [TextClassification](https://github.com/sanjusci/nltk-basic/blob/master/text_classification.py)

### TextClassification via NLTK
* [TextClassificationfeature](https://github.com/sanjusci/nltk-basic/blob/master/text_classification_features.py)

## How to run?
1. Move to ```<project-dir>```, create virtual environment and then activate it as

```sh
$ cd <project-dir>
$ virtualenv .environment
$ source .environment/bin/activate
$ pip3 install -r requirements.txt
```
>Note: Step-1 is optional but recommended.

2. Add project to ```PYTHONPATH``` as 

```sh 
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
```

> If you are using PyCharm then it can be done under `run configuration`.

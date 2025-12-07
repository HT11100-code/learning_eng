import nltk
import re
import csv
import pathlib
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class textExtractor:
    def __init__(self, text):
        self.text = text

    def extract_sentences(self):
        for sent in nltk.sent_tokenize(self.text):
            yield sent

    def extract_words(self):
        row_wordlist = nltk.word_tokenize(self.text)
        for word in row_wordlist:
            if re.match(r'[a-zA-Z]', word):
                yield word
 
    def normalize_words(self):
        wordLower = (word.lower() for word in self.extract_words())
        uniqueWords = set(wordLower)
        return sorted(uniqueWords)
    
    def get_tagged_words(self, sentence):
        # 文字列をトークン化してから品詞タグ付けを行う
        tokens = nltk.word_tokenize(sentence)
        tagged_tokens = nltk.pos_tag(tokens)
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        results = []
        for word, tag in tagged_tokens:
            wn_tag = tag_dict.get(tag[0].upper(),wordnet.NOUN)
            results.append((word, wn_tag))
        return results
        
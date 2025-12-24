import spacy
import pathlib
from nltk.corpus import wordnet

class QuizGenerator:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    
    def get_wordnet_definition(self, word, pos_tag):
        
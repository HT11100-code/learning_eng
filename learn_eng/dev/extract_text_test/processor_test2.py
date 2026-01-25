import nltk
import pathlib

class textExtractor:
    def __init__(self, text):
        self.text = text

    def extract_sentences(self):
        for sent in nltk.sent_tokenize(self.text):
            yield sent

text = pathlib.Path("text_files/ironman.txt").read_text()
extractor = textExtractor(text)
for sentence in extractor.extract_sentences():
    print(f"{sentence}")
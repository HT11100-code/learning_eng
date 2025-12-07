import spacy
import pathlib

nlp = spacy.load('en_core_web_sm')

text = pathlib.Path("text_files/ironman.txt").read_text()
doc = nlp(text)

print(doc.text)

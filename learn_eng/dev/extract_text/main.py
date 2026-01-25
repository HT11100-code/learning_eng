import pathlib
from processor import textExtractor
import nltk


nltk.download("punkt")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")


text = pathlib.Path("text_files/ironman.txt").read_text()
extractor = textExtractor(text)

sentences = []
for sentence in extractor.extract_sentences():
    sentences.append(sentence)
print(sentences)
print('----------------------------------------------')
sorted_wordlist = sorted(extractor.extract_words())
print(f'Words: {sorted_wordlist}\nNum of words: {len(sorted_wordlist)}')
print('----------------------------------------------')
normalized_words = extractor.normalize_words()
print(f'Normalized Words: {normalized_words}\nNum of words: {len(normalized_words)}')
print('----------------------------------------------')
tagged_words = extractor.get_tagged_words(sentences)
print(tagged_words)
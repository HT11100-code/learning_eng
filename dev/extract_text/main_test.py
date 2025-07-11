import nltk
import re

nltk.download("punkt")

path = "text_files/ironman.txt"

with open(path)as f:
    text = f.read()
    
sentences = nltk.sent_tokenize(text)

for sent in sentences:
        print(f'{sent}')

    
eng_pattern1 = re.compile(r'[a-zA-Z]+')

row_word = nltk.word_tokenize(text)
    
unique_word = set(row_word)
print(f'Words: {sorted(unique_word)}\n Num of words: {len(unique_word)}')
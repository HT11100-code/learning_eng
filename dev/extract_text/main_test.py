import nltk
import re

nltk.download("punkt")

path = "text_files/ironman.txt"

with open(path)as f:
    text = f.read()    
sentences = nltk.sent_tokenize(text)

for sent in sentences:
        print(f'{sent}')
print('----------------------------------------------')

row_wordlist = nltk.word_tokenize(text)
eng_wordlist = []
for word in row_wordlist:
      if re.match(r'[a-zA-Z]', word):
            eng_wordlist.append(word)
    
unique_wordlist = sorted(set(eng_wordlist))
print(f'Words: {unique_wordlist}\nNum of words: {len(unique_wordlist)}')
import nltk
import re

nltk.download("punkt")

path = "text_files/ironman.txt"

with open(path)as f:
    text = f.read()

row_wordlist = nltk.word_tokenize(text)
sorted_row_wordlist = sorted(set(row_wordlist))

uniques_wordlist = []
for wordlist in row_wordlist:
    if  re.match(r'[a-zA-Z]+', wordlist):
        uniques_wordlist.append(wordlist)

sorted_uniques_wordlist = sorted(set(uniques_wordlist))

print(f'{sorted_row_wordlist}\nNum of words: {len(sorted_row_wordlist)}')
print(f'{sorted_uniques_wordlist}\nNum of words: {len(sorted_uniques_wordlist)}')
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re


nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
lemmatizer = WordNetLemmatizer()

path = "text_files/ironman.txt"

with open(path)as f:
    text = f.read()

row_wordlist = nltk.word_tokenize(text)
sorted_row_wordlist = sorted(set(row_wordlist))

uniques_wordlist = []
for wordlist in row_wordlist:
    if  re.match(r'[a-zA-Z]+', wordlist):
        uniques_wordlist.append(wordlist)

sorted_uniques_wordlist = sorted(uniques_wordlist)

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

word = ["running", "better", "ate", "cats"]
print(get_wordnet_pos(word))

print(f'{sorted_row_wordlist}\nNum of words: {len(sorted_row_wordlist)}')
print(f'{sorted_uniques_wordlist}\nNum of words: {len(sorted_uniques_wordlist)}')
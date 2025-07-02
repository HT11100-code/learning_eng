import fitz
import nltk
import re
nltk.download("all")#3機能一括download（2回目はdownloadされない）(nltk_data容量が3GBになる)

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text()

words = nltk.word_tokenize(text)
sentences = nltk.sent_tokenize(text)
eng_words_pattern = re.compile(r'\w{2,}', flags=re.ASCII)

def sorted_list(word_list):
    return sorted(set(word.lower() for word in word_list))

eng_words = []
for word in words:
    if eng_words_pattern.fullmatch(word) and not word.isdigit():
        eng_words.append(word)


eng_sentences = []



print(f'Words: {sorted_list(eng_words)}\nNumber of Eng words: {len(sorted_list(eng_words))}')



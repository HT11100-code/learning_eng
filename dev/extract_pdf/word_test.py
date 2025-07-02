import fitz
import nltk
import re
nltk.download("all")#3機能一括download（2回目はdownloadされない）(nltk_data容量が3GBになる)

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text()

pattern1 = r'[a-zA-Z]{2,}(?!\b\'\b)'
row_words_list = re.findall(pattern1, text)
unique_words_list = sorted(set(word.lower() for word in row_words_list))




#print(f'row_Words: {row_words_list}\nNum of row_words: {len(row_words_list)}')
print(f'unique_Words: {unique_words_list}\nNum of unique_words: {len(unique_words_list)}')


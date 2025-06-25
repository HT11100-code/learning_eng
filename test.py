import fitz
import re

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text()
pattern1 = r'[a-zA-Z]+'
patern2 = r'[^\']'
words = re.findall(pattern1, text)
found_words = sorted(set(word.lower() for word in words))

print(f'英単語リスト: {found_words[:]}')
print(f'単語数: {len(found_words)}')
import fitz
import re

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text()
words = re.findall(r'[a-zA-Z]+', text)

# 小文字化して重複排除
found_words = sorted(set(word.lower() for word in words))

print("英単語リスト（最初の20個）:", found_words[:])
print("単語数:", len(found_words))
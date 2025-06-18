import fitz
import re

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text()
words = re.findall(r'([a-zA-Z]+)', text)

print("すべての英語の単語（最初の10個）:", words[:10])
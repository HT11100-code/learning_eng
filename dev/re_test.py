import fitz
import re
import requests

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text()

pattern1 = r'[a-zA-Z]{2,}(?!\b\'\b)'
patern2 = r''
words = re.findall(pattern1, text)
found_words = sorted(set(word.lower() for word in words))

file_path = "output_file.txt"
with open(file_path, "w") as file:
    for word in found_words:
        file.write(word + "\n")

print(f'英単語リスト: {found_words[:]}')
print(f'単語数: {len(found_words)}') 
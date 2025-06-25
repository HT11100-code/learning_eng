import fitz
import re

doc = fitz.open("./ironman.pdf")
page = doc[0]
text = page.get_text()
print(text)
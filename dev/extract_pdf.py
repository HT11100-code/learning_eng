import fitz
import re
import requests

doc = fitz.open("./ironman.pdf")
page = doc[0]
text = page.get_text()
print(text)
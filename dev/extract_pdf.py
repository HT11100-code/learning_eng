import fitz
import re
import requests

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text("text")
print(text)
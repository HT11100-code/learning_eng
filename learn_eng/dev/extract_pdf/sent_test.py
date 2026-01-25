import re
import fitz
import nltk

nltk.download('punkt')

doc = fitz.open("text_files/ironman.pdf")
page = doc[0]
text = page.get_text()
text = text.replace('\n', ' ')
text = re.sub(r'\s+', ' ', text)

sentences = nltk.sent_tokenize(text)

eng_sentences = []
for sent in sentences:
    if re.search(r'[a-zA-Z]', sent, flags=re.ASCII) and not re.search(r'[ぁ-んァ-ン一-龥]', sent):
        eng_sentences.append(sent.strip())

for sent in eng_sentences:
    print(sent)
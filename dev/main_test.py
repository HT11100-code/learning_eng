import fitz
import nltk
import re
nltk.download("all")#3機能一括download（2回目はdownloadされない）(nltk_data容量が3GBになる)

doc = fitz.open("pdf/ironman.pdf")
page = doc[0]
text = page.get_text()

tokens = nltk.word_tokenize(text)
sentences = nltk.sent_tokenize(text)
#tagged = nltk.pos_tag(tokens)
#entities = nltk.chunk.ne_chunk(tagged)

english_words_pattern = re.compile(r'\w+', flags=re.ASCII)

english_words = []
for token in tokens:
    if re.fullmatch(english_words_pattern, token):
        english_words.append(token)

english_sentences = []
for sentence in sentences:
    tokens = tokens
    is_english_sentence = True

    for token in tokens:
        if english_words_pattern.fullmatch(token):
            continue
    else:
        if not re.fullmatch(r'[^\w\s]', token) and not token.isdigit:
            is_english_sentence = False
            break
    
    if is_english_sentence:
        english_sentences.append(sentence)

print(f'Tokenized words: {set(english_words)}\nNumber of words: {len(set(english_words))}\nSentences: {english_sentences}')
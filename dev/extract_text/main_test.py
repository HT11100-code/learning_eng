import nltk

nltk.download("punkt")

path = "text_files/ironman.txt"

with open(path)as f:
    text = f.read()
    sentences = nltk.sent_tokenize(text)

    for sent in sentences:
        print(sent)

    row_word = nltk.word_tokenize(text)
    unique_word = set(row_word)
    print(f'Words: {unique_word}\n Num of words: {len(unique_word)}')
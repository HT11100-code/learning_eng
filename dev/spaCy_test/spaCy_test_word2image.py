from spaCy_test_source import Learningtextprocessor
import pathlib

if __name__ == "__main__":
    text = pathlib.Path("text_files/ironman.txt").read_text()
    processor = Learningtextprocessor()
    structured_data = processor.process_text(text)

    def noun_words(data):
        nouns = []
        for sentence in data:
            for word in sentence['words']:
                if word['pos'] == 'NOUN':
                    nouns.append(word['text'])
        return nouns
    
    nouns = noun_words(structured_data)
    print(nouns)
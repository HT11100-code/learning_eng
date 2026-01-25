import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")

lemmatizer = WordNetLemmatizer()
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

word = "running"
print(get_wordnet_pos(word))
print(lemmatizer.lemmatize(word, get_wordnet_pos(word)))
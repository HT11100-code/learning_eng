import pathlib
import json
import random
from typing import Optional
#import streamlit as st

text = pathlib.Path("JSON_files/structured_data.json").read_text()
#st.title("Word2ImageApp")

def get_random_noun_word(self) -> Optional[str]:
    try:
        structured_data = json.loads(text)
        noun_words = []

        for sentence in structured_data:
            for word in sentence["words"]:
                if word["pos"] == "NOUN" and not word["is_stop"]:
                    noun_words.append(word["text"])
                    
                if not noun_words:
                    return None
                return random.choice(noun_words)
    except json.JSONDecodeError:
        return None
    
nounWordslist = get_random_noun_word(text)
print(nounWordslist)
                

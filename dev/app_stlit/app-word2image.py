import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
import json
import random
from dev.spaCy_test.spaCy_test_source import Learningtextprocessor
from typing import Optional
#import streamlit as st

if __name__ == "__main__":
    text = pathlib.Path("text_files/ironman.txt").read_text()
    processor = Learningtextprocessor()
    structured_data = processor.process_text(text)

    print(structured_data)
 
                
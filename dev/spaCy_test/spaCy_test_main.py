import pathlib
from spaCy_test_source import Learningtextprocessor
import json

if __name__ == "__main__":
    text = pathlib.Path("text_files/ironman.txt").read_text()
    processor = Learningtextprocessor()
    structured_data = processor.process_text(text)

    with open("JSON_files/structured_data.json", "w", encoding="utf-8") as f:
        json.dump(structured_data, f, ensure_ascii=False, indent=4)

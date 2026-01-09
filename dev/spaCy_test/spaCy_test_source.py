import spacy
import pathlib
import uuid
from typing import List, Dict, Any
from dataclasses import dataclass, asdict

@dataclass
class WordDate:
    text: str #単語
    lemma: str #原形
    pos: str #品詞大分類
    tag: str #詳細な品詞タグ
    is_stop: bool #学習対象外判定時に使用

@dataclass
class SentenceData:
    id : str
    original_text: str
    words : List[WordDate]

class Learningtextprocessor:
    def __init__(self, model_name: str = "en_core_web_sm"):
        self.nlp = spacy.load(model_name)

    def process_text(self, text: str) -> List[Dict[str, Any]]:

        if not text:
            return []

        doc = self.nlp(text)
        structured_data = []

        for sent in doc.sents:
            clean_text = sent.text.strip()
            if not clean_text:
                continue
            
            word_list = []
            for token in sent:
                word_info = WordDate(
                    text=token.text,
                    lemma=token.lemma_,
                    pos=token.pos_,
                    tag=token.tag_,
                    is_stop=token.is_stop
                )
                word_list.append(word_info)

            sent_data = SentenceData(
                id=str(uuid.uuid4()),
                original_text=clean_text,
                words=word_list
            )

            structured_data.append(asdict(sent_data))

        return structured_data
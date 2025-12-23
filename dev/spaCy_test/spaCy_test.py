import spacy
from spacy import displacy
import pathlib

nlp = spacy.load('en_core_web_sm')

text = pathlib.Path("text_files/ironman.txt").read_text()
doc = nlp(text)

for sent_i, sentence in enumerate(doc.sents):
    print(f"\n[{sent_i + 1}] --------------------------------")
    print(f"文全体: {sentence.text}")
    print("-" * 60)
    print(f"{'単語リスト':<15} {'原形':<12} {'品詞':<8} {'役割(dep)':<12} {'係り先(head)'}")
    print("-" * 60)

for token in doc:
    print(f"{token.text:<15} {token.lemma_:<12} {token.pos_:<8} {token.dep_:<12} {token.head.text}")

docs_to_visualize = list(doc.sents)[:3]
displacy.serve(docs_to_visualize, style='dep', auto_select_port=True)
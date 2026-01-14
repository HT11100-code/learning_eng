---
marp : true
---
# 映像コンテンツを基にした英語学習法と対話型学習
---
## spaCy Text Processing
---
### 概要
自然言語処理とテキスト分析のために **spaCy** を使用した
### Data Classes

#### WordDate
- **text** (str): 単語（単語テキスト）
- **lemma** (str): 原形（基本形）
- **pos** (str): 品詞大分類（Part of Speech）
- **tag** (str): 詳細な品詞タグ
- **is_stop** (bool): 学習対象外判定時に使用
---
#### SentenceData
- **id** (str): ユニークID (UUID)
- **original_text** (str): 元の文章
- **words** (List[WordDate]): 単語情報のリスト
---
### Learningtextprocessor Class

#### Constructor
```python
def __init__(self, model_name: str = "en_core_web_sm")
```
- spaCyモデルを読み込んで初期化
- デフォルトモデル: `en_core_web_sm`
---
#### process_text Method
```python
def process_text(self, text: str) -> List[Dict[str, Any]]
```
---
**処理フロー:**
1. テキストが空の場合は空リストを返す
2. spaCyドキュメント解析を実行
3. 文単位で解析（`doc.sents`）
4. 各文に含まれる単語をトークン化
5. 単語情報（WordDate）を構築
6. SentenceData構造化データを作成
7. 辞書形式で返す（`asdict`）
---
**特徴:**
- 空の文はスキップ
- 各単語の詳細情報（原形、品詞、タグ、ストップワード判定）を抽出
- 構造化された辞書形式で処理結果を返す
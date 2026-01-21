from spaCy_test_source import Learningtextprocessor
import pathlib
import requests
import io
from PIL import Image
import random

# Learningtextprocessorクラスの定義またはインポートが必要です
# from your_module import Learningtextprocessor 

def noun_words(data):
    """データから名詞を抽出"""
    nouns = []
    for sentence in data:
        for word in sentence['words']:
            if word['pos'] == 'NOUN':
                nouns.append(word['text'])
    return nouns


def search_unplash_image(query):
    """Unsplash APIで画像を検索する"""
    ACCESS_KEY = "OkXOm10V7my1zp7npccYKr5dBQpgWoHlK2KqBT3SJMg"
    url = "https://api.unsplash.com/search/photos"

    params = {
        "query": query,
        "client_id": ACCESS_KEY,
        "per_page": 1,
        "orientation" : "landscape"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data['results']:
            return data['results'][0]['urls']['regular']
        else:
            print("画像が見つかりませんでした。")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"APIエラーが発生しました: {e}")
        return None


def display_image(url):
    """URLから画像を取得して表示する"""
    if not url:
        return
    
    try:
        image_response = requests.get(url)
        image_response.raise_for_status()

        image_data = io.BytesIO(image_response.content)
        image = Image.open(image_data)

        print("画像を表示します...")
        image.show()

    except Exception as e:
        print(f"画像の取得または表示中にエラーが発生しました: {e}")


def word_quiz(word):#wordquiz
    user_input = input("画像の英単語を入力: " )
    if user_input.lower() ==word.lower():
        print("正解!!")
    else:
        print(f"不正解!! 正しい単語は '{word}' でした")


def main():
    """メインの実行処理"""
    # 1. テキスト処理の実行
    # try-exceptでファイル読み込みエラーをケアしても良いでしょう
    try:
        text = pathlib.Path("text_files/ironman.txt").read_text(encoding='utf-8')
    except FileNotFoundError:
        print("ファイルが見つかりません。")
        return

    # Learningtextprocessorが定義されている前提
    processor = Learningtextprocessor()
    structured_data = processor.process_text(text)
    
    # 2. 名詞の抽出
    nouns_list = noun_words(structured_data)
    print(f"抽出された名詞: {nouns_list[:5]}...") # 確認用に出力

    # 3. 画像検索と表示
    # ここでは例として "ocean" を検索していますが、
    # 抽出したnouns_listの中身を使うことも可能です
    query = random.choice(nouns_list) 
    
    image_url = search_unplash_image(query)

    if image_url:
        print(f"取得した画像のURL: {image_url}")
        display_image(image_url) # 関数名を修正しました

    # 4. 単語クイズ
    word_quiz(query)

if __name__ == "__main__":
    main()

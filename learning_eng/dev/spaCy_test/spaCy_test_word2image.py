from spaCy_test_source import Learningtextprocessor
import pathlib
import requests
import io
from PIL import Image
import random
import json


def get_sentences_with_nouns(data):
    filtered_data = [
        sentence for sentence in data
        if any(word['pos']== 'NOUN' for word in sentence['words'])
    ]

    return filtered_data


def search_unsplash_image(query):
    """Unsplash APIで画像を検索する"""
    ACCESS_KEY = "OkXOm10V7my1zp7npccYKr5dBQpgWoHlK2KqBT3SJMg"
    url = "https://api.unsplash.com/search/photos"

    params = {
        "query": query,
        "client_id": ACCESS_KEY,
        "per_page": 1,
        #"orientation" : "landscape",
        "order_by": "relevant"
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


def word_quiz(word):
    user_input = input("画像の英単語を入力: " )
    if user_input.lower() ==word.lower():
        print("正解!!")
    else:
        print(f"不正解!! 正しい単語は '{word}' でした")


def main():
    """メインの実行処理"""
    # テキスト処理の実行
    try:
        text = pathlib.Path("text_files/ironman.txt").read_text(encoding='utf-8')
    except FileNotFoundError:
        print("ファイルが見つかりません。")
        return

    processor = Learningtextprocessor()
    structured_data = processor.process_text(text)
    
    sentences_with_nouns = get_sentences_with_nouns(structured_data)

    if not sentences_with_nouns:
        print("名詞を含む文が見つかりませんでした。")
        return 
    
    selected_sentence = random.choice(sentences_with_nouns)
    nouns = [word for word in selected_sentence['words'] if word['pos'] == 'NOUN']
    selected_noun = random.choice(nouns)
    noun_text = selected_noun['text']

    print(f"選択された文: {selected_sentence['original_text']}")
    print(f"選択された名詞: {noun_text}")
    image_url = search_unsplash_image(noun_text)
    display_image(image_url)
    word_quiz(noun_text)




if __name__ == "__main__":
    main()

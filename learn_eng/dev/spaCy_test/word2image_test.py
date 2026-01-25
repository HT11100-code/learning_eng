import json



def noun_words(data):
    """データから名詞を抽出"""
    nouns = []
    for sentence in data:
        for word in sentence['words']:
            if word['pos'] == 'NOUN':
                nouns.append(word['text'])
    return nouns

def main():
    try:
        with open('JSON_files/demo_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("JSONファイルが見つかりません。")
        return
    
    nouns = noun_words(data)
    print("抽出された名詞:", nouns)




if __name__ == "__main__":
    main()
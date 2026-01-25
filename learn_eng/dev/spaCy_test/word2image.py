import json
import random
import streamlit as st

def extract_nouns_with_context(data):
    """
    データから名詞を抽出し、元の文脈情報（逆探知用）と共にリスト化する
    """
    nouns_info = []
    
    for sentence in data:
        # 元の文の情報を取得（IDや原文）
        source_id = sentence.get('id')
        original_text = sentence.get('original_text')
        
        for word in sentence['words']:
            if word['pos'] == 'NOUN':
                # 単なる文字列ではなく、辞書として情報をまとめる
                image_path = word.get('image_path')
                if image_path:
                    # 画像パスを正しい相対パスに調整（spaCy_test/ から見たパス）
                    image_path = image_path.replace('learning_eng/images/', '../../images/')
                noun_entry = {
                    "word": word.get('lemma', word['text']),  # 名詞の原型（lemma）を使用
                    "image": image_path, # 画像パス（あれば）
                    "source_id": source_id,        # ★逆探知用のID
                    "source_text": original_text   # ★逆探知用の元の文
                }
                nouns_info.append(noun_entry)
                
    return nouns_info

def display_quiz(nouns_info):
    """
    nouns_info からランダムに名詞を選んでクイズ形式で表示する関数
    """
    if not nouns_info:
        st.write("名詞情報がありません。")
        return
    
    # セッション状態で問題を保持
    if 'current_noun' not in st.session_state or 'used_nouns' not in st.session_state:
        st.session_state.used_nouns = []
        st.session_state.checked = False
        available = nouns_info
    else:
        available = [n for n in nouns_info if n not in st.session_state.used_nouns]
        if not available:
            st.session_state.used_nouns = []
            available = nouns_info
            st.rerun()
            st.rerun()
    
    if 'current_noun' not in st.session_state:
        st.session_state.current_noun = random.choice(available)
        st.session_state.used_nouns.append(st.session_state.current_noun)
    
    noun = st.session_state.current_noun
    word = noun['word']
    image_path = noun.get('image')
    
    if image_path:
        st.image(image_path, caption="この画像の名詞は何でしょう？")
    else:
        st.write("画像なし: この単語の名詞は何でしょう？（テキストのみ）")
    
    # クイズフォーム
    with st.form(key=f"quiz_form_{noun['source_id']}"):
        # 答え入力
        user_answer = st.text_input("答えを入力してください:", key=f"answer_{noun['source_id']}", autocomplete="off")
        
        # フォーム送信ボタン（エンターキーでも動作）
        submitted = st.form_submit_button("答えを確認")
        
        if submitted:
            st.session_state.checked = True
            if user_answer.strip().lower() == word.lower():
                st.success("正解！")
            else:
                st.error(f"不正解。正解は '{word}' です。")
    
    # チェック済みの場合、次の問題ボタンを表示
    if st.session_state.checked:
        if st.button("次の問題", key=f"next_{noun['source_id']}"):
            st.session_state.current_noun = random.choice(available)
            st.session_state.used_nouns.append(st.session_state.current_noun)
            st.session_state.checked = False
            st.rerun()

def main():
    try:
        with open('../../JSON_files/demo_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("JSONファイルが見つかりません。")
        return
    
    # 名詞リスト（詳細情報付き）を取得
    nouns_list = extract_nouns_with_context(data)
    
    # ---------------------------------------------------------
    # 使用例：抽出したリストから「逆探知」してみる
    # ---------------------------------------------------------
    # print("--- 抽出結果の確認 ---")
    # for item in nouns_list:
    #     print(f"名詞: {item['word']}")
    #     print(f"  └─ 元の文: {item['source_text']}")
    #     print(f"  └─ 画像パス: {item['image']}")
    #     print("-" * 30)

    # 特定の単語（例: yesterday）がどこで使われているかフィルタリングする例
    # target = "mage"
    # print(f"\n--- '{target}' の逆探知結果 ---")
    # found_items = [x for x in nouns_list if x['word'] == target]
    
    # for item in found_items:
    #     print(f"ID: {item['source_id']} | 文: {item['source_text']}")

    # ランダムに名詞の画像を表示（Streamlit用）
    display_quiz(nouns_list)

if __name__ == "__main__":
    main()
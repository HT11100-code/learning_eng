import json
import random
import streamlit as st
import os

def extract_nouns_with_context(data):
    """
    データから名詞を抽出し、元の文脈情報と共にリスト化する
    """
    nouns_info = []
    
    for sentence in data:
        # 元の文の情報を取得
        source_id = sentence.get('id')
        original_text = sentence.get('original_text')
        
        for word in sentence['words']:
            if word['pos'] == 'NOUN':
                image_path = word.get('image_path')
                camption = word.get('caption')
                if image_path:
                    image_path = image_path.replace('learn_eng/images/', '../../images/')
                noun_entry = {
                    "word": word.get('lemma', word['text']),
                    "image": image_path,
                    "caption": camption,
                    "source_id": source_id,
                    "source_text": original_text
                }   
                nouns_info.append(noun_entry)
                
    return nouns_info



def display_quiz(nouns_info):
    if not nouns_info:
        st.write("名詞情報がありません。")
        return
    
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

    
    if 'current_noun' not in st.session_state:
        st.session_state.current_noun = random.choice(available)
        st.session_state.used_nouns.append(st.session_state.current_noun)
    
    noun = st.session_state.current_noun
    word = noun['word']
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = noun.get('image')
    
    if raw_path:
        image_path = os.path.join(current_dir, raw_path)
    else:
        image_path = None

    col1, col2 = st.columns([30, 20])

    with col1:
        if image_path:
            st.image(image_path, use_container_width=True)
            caption_text = noun.get("caption")
            st.markdown(
                f"""
                <div style="text-align: center; font-size: 18px; color: #555; margin-top: 10px;">
                    {caption_text}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.write("画像がありませんでした。")

    with col2:
        st.write("英単語クイズ")
        
        user_answer = st.text_input("答えを入力してください:", key=f"answer_{noun['source_id']}", autocomplete="off")
        
        btn_col1, btn_col2 = st.columns([1, 1])
        
        with btn_col1:
            if st.button("答えを確認", key=f"check_{noun['source_id']}"):
                st.session_state.checked = True

        with btn_col2:
            if st.session_state.checked:
                if st.button("次の問題", key=f"next_{noun['source_id']}"):
                    st.session_state.current_noun = random.choice(available)
                    st.session_state.used_nouns.append(st.session_state.current_noun)
                    st.session_state.checked = False
                    st.rerun()

        if st.session_state.checked:
            if user_answer.strip().lower() == word.lower():
                st.markdown(":white_check_mark: <span style='color: green; font-weight:bold;'>正解！</span>", unsafe_allow_html=True)
            else:
                st.markdown(f":x: <span style='color: red; font-weight:bold;'>不正解。正解は <span style='font-size: 24px; color:#000; '> {word} </span> です。</span>", unsafe_allow_html=True)

def main():
    try:
        with open('../../JSON_files/demo_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("JSONファイルが見つかりません。")
        return
    
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
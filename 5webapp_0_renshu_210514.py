import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title("Streamlit 超入門")

# st.write("Interactive Widgets")

st.write("プレグレスバー")
"Start!!"

Latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    Latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.3)

"Done!!"

left_column,right_column=st.beta_columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1=st.beta_expander("問い合わせ1")
expander1.write("問い合わせ内容を書く")
expander2=st.beta_expander("問い合わせ2")
expander2.write("問い合わせ内容を書く")
expander3=st.beta_expander("問い合わせ3")
expander3.write("問い合わせ内容を書く")

# text=st.text_input("あなたの趣味を教えて下さい")
# "あなたの趣味：",text,"です。"

# condition=st.slider("あなたの今の調子は？",0,100,50)
# "コンディション:",condition

# st.write("Interactive Widgets")

# text=st.text_input("あなたの趣味を教えて下さい")
# "あなたの趣味：",text,"です。"

# option=st.selectbox(
#     "あなたが好きな数字を教えて下さい",
#     list(range(1,11)))

# "あなたが好きな数字は,",option,"です。"

# if st.checkbox("Show Image"):
#     img=Image.open("広瀬すず01.jpg")
#     st.image(img,caption=("広瀬すず"),use_column_width=True)




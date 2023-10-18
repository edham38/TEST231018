from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI

from langchain.chat_models import ChatOpenAI

import streamlit as st

# OpenAI()는 일반적인 Completion모드임. 서로 대화를 하는것이 아님

# llm = OpenAI()

# result = llm.predict("내가 좋아하는 동물은 ")

# print(result)

  

# ChatOpenAI()는 대화형 모델임. 서로 대화를 하는것이 가능함

from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('챗봇 테스트')

Question = st.text_input('Movie title', '입력하시오')

if st.button('해결해줘'):

    result = chat_model.predict(Question)

    print(result)

    st.write(result)
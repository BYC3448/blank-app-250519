import streamlit as st
import openai

# 1. OpenAI API 키 설정
openai.api_key = st.secrets["openai_api_key"]

# 2. 페이지 제목
st.title("💬 GPT 챗봇 with Context (Multi-turn)")

# 3. 모델 선택 (옵션)
model = st.selectbox("모델 선택", ["gpt-3.5-turbo"], index=0)

# 4. 대화 기록 세션 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# 5. 기존 대화 표시
for msg in st.session_state.messages[1:]:  # system 메시지 제외
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. 사용자 입력 받기
user_input = st.chat_input("질문을 입력하세요")

if user_input:
    # 7. 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 8. GPT 응답 요청
    with st.chat_message("assistant"):
        with st.spinner("답변 생성 중..."):
            response = openai.chat.completions.create(
                model=model,
                messages=st.session_state.messages
            )
            assistant_reply = response.choices[0].message.content
            st.markdown(assistant_reply)

    # 9. 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

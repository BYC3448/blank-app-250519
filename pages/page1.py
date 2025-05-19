import streamlit as st
import pandas as pd
from datetime import date
import random

# 1. 가상 학생 20명 생성
first_names = ['김', '이', '박', '최', '정', '한', '조', '윤', '장', '오']
last_names = ['하늘', '준서', '지우', '서연', '민준', '서윤', '예준', '지민', '도윤', '가은']
students = [random.choice(first_names) + random.choice(last_names) for _ in range(20)]

# 2. 오늘 날짜 및 사용자 입력 제목
today = date.today().strftime('%Y-%m-%d')
st.title("📝 학생 출석/과제 체크 앱")

task_title = st.text_input("✅ 오늘의 활동 제목을 입력하세요 (예: 소풍, 사진제출 등)", "소풍")
st.write(f"### 📌 활동: {task_title} ({today})")

# 3. 출석 및 과제 상태 저장
attendance = {}
assignments = {}

st.write("### 👩‍🎓 학생 체크")

# 4. 체크박스 UI 생성
for student in students:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(student)
    with col2:
        attendance[student] = st.checkbox("출석", key=f"att_{student}")
    with col3:
        assignments[student] = st.checkbox("과제", key=f"ass_{student}")

# 5. 결과 저장 및 표 출력
if st.button("✅ 결과 저장"):
    data = {
        "이름": students,
        "출석": [attendance[s] for s in students],
        "과제제출": [assignments[s] for s in students]
    }
    df = pd.DataFrame(data)
    st.success(f"활동 [{task_title}] 결과가 저장되었습니다!")
    st.dataframe(df)

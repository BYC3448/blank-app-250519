import streamlit as st
import pandas as pd
from datetime import date

# 1. 가상 학생 리스트
students = ['김하늘', '이준서', '박지우', '최서연', '정민준']

# 2. 오늘 날짜 표시
today = date.today().strftime('%Y-%m-%d')
st.title(f"📝 출석 및 과제 제출 체크 ({today})")

# 3. 출석 및 과제 상태 저장용 딕셔너리
attendance = {}
assignments = {}

st.write("### 👨‍🏫 학생 출석/과제 체크")

# 4. 학생별 체크박스 UI 생성
for student in students:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(student)
    with col2:
        attendance[student] = st.checkbox("출석", key=f"att_{student}")
    with col3:
        assignments[student] = st.checkbox("과제", key=f"ass_{student}")

# 5. 저장 버튼 클릭 시 결과 표로 출력
if st.button("✅ 결과 저장"):
    data = {
        "이름": students,
        "출석": [attendance[s] for s in students],
        "과제제출": [assignments[s] for s in students]
    }
    df = pd.DataFrame(data)
    st.success("결과가 저장되었습니다!")
    st.dataframe(df)

import streamlit as st

# 페이지 구성
st.set_page_config(page_title="엄마쌤 알림장", layout="centered")

st.title("🌱 엄마쌤의 영유아 알림장 도우미")

# 사용자 입력
name = st.text_input("아이 이름 (예: OO는)")
age = st.selectbox("연령", ["만0세", "만1세", "만2세", "만3세", "만4세", "만5세"])
content = st.text_area("오늘의 놀이와 활동 내용을 입력하세요.")

# 알림장 생성 버튼
if st.button("알림장 작성하기"):
    if name and content:
        # 선생님께서 주신 작성 규칙을 시스템 프롬프트로 적용
        prompt = f"""
        당신은 10년 차 보육교사입니다. 아래 내용을 바탕으로 따뜻하고 자연스러운 알림장을 작성하세요.
        - 대상: {name}, 연령: {age}
        - 활동: {content}
        - 규칙: 과거시제 사용, 직접화법 포함, 15문장 내외, 교육과정 및 출처 언급 금지, 이모지 금지.
        """
        
        # 실제 환경에서는 AI 응답 결과를 출력합니다.
        result = "선생님, 이곳에 생성된 알림장 결과값이 출력됩니다." 
        st.success("알림장이 완성되었습니다!")
        st.text_area("결과 확인", value=result, height=300)
    else:
        st.warning("이름과 활동 내용을 모두 입력해주세요.")
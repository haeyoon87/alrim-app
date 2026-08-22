import streamlit as st

# 페이지 설정
st.set_page_config(page_title="엄마쌤의 알림장 프롬프트 도우미", layout="centered")

st.title("🌱 엄마쌤의 알림장 프롬프트 생성기")
st.markdown("아이의 활동 메모를 입력하면, ChatGPT나 Claude에 바로 복사해 붙여넣어 완벽한 알림장을 만들 수 있는 전문 프롬프트가 생성됩니다.")

# 입력 폼 구성
with st.form("prompt_form"):
    name_input = st.text_input("아이 이름", value="현우")
    age_group = st.selectbox("연령 선택", ["만0세", "만1세", "만2세", "만3세", "만4세", "만5세"])
    
    st.markdown("---")
    play_input = st.text_area("1️⃣ 오늘의 놀이 및 상호작용 메모", placeholder="예: 자동차 모형을 밀고 당김. 친구가 다가오자 '하지마!'라고 표현함.")
    routine_input = st.text_area("2️⃣ 일상생활 메모 (식사, 배변, 낮잠 등)", placeholder="예: 식사 보통, 파프리카 깍두기 먹기 성공. 화장실 소변 성공.")
    notice_input = st.text_area("3️⃣ 꼭! 읽어주세요 (선택)", placeholder="예: 여벌 팬티 5개 정도 보내주세요.")
    
    submitted = st.form_submit_button("알림장 프롬프트 생성하기")

if submitted:
    if not play_input.strip() and not routine_input.strip():
        st.warning("놀이 또는 일상생활 내용을 입력해 주세요!")
    else:
        name = name_input.strip()
        play = play_input.strip()
        routine = routine_input.strip()
        notice = notice_input.strip()

        # AI(ChatGPT/Claude)에게 던질 고품격 프롬프트 조합
        prompt_result = f"""다음 조건과 작성 원칙에 맞춰 어린이집 학부모님께 보낼 {age_group} {name}의 알림장을 작성해줘.

[입력된 오늘의 기록]
- 이름: {name} ({age_group})
- 놀이 및 상호작용: {play}
- 일상생활: {routine}
- 공지사항([꼭! 읽어주세요.]로 표시): {notice if notice else "없음"}

[작성 원칙]
1. 계절감이 느껴지는 따뜻한 인사말로 시작할 것.
2. 입력된 메모를 단순 나열하지 말고, 보육교사의 전문적인 관찰이 담긴 자연스럽고 유창한 복문 중심의 서술형 문장으로 완전히 새롭게 윤문할 것.
3. 아이 이름은 '{name}는' 또는 '{name}가' 등의 조사가 자연스럽게 어우러지도록 할 것.
4. 마지막 마무리는 보호자와 아이의 저녁을 축복하는 따뜻한 인사로 끝맺을 것.
5. 교육과정 이름이나 문서명, 이모지는 절대 사용하지 말 것."""

        st.success("✨ AI용 프롬프트가 성공적으로 생성되었습니다!")
        st.markdown("아래의 프롬프트를 복사하여 평소 사용하시는 **ChatGPT나 Claude 대화창에 그대로 붙여넣어 주세요.** 매번 완전히 새롭고 자연스러운 알림장이 완성됩니다!")
        st.text_area("AI 복사·붙여넣기 전용 프롬프트", value=prompt_result, height=350)
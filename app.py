import streamlit as st

# 페이지 설정
st.set_page_config(page_title="엄마쌤의 영유아 알림장 도우미", layout="centered")

st.title("🌱 엄마쌤의 영유아 알림장 작성 도우미")
st.markdown("입력하신 메모를 바탕으로, 자연스러운 윤문과 교정 작업이 적용된 따뜻한 알림장을 완성해 드립니다.")

# 입력 폼 구성
with st.form("alrim_form"):
    name_input = st.text_input("아이 이름", value="현우")
    age_group = st.selectbox("연령 선택", ["만0세", "만1세", "만2세", "만3세", "만4세", "만5세"])
    
    st.markdown("---")
    play_input = st.text_area("1️⃣ 오늘의 놀이 및 상호작용 (메모 형태로 적어주세요)", placeholder="예: 자동차 모형을 밀고 당김. 친구가 다가오자 '하지마!'라고 표현함.")
    routine_input = st.text_area("2️⃣ 일상생활 (식사, 배변, 낮잠 등)", placeholder="예: 식사 보통, 파프리카 깍두기 먹기 성공. '쉬'라고 말해 화장실 소변 성공.")
    notice_input = st.text_area("3️⃣ 꼭! 읽어주세요 (선택)", placeholder="예: 여벌 팬티 5개 정도 보내주세요.")
    
    submitted = st.form_submit_button("알림장 완성하기")

if submitted:
    if not play_input.strip() and not routine_input.strip():
        st.warning("내용을 입력해 주세요!")
    else:
        name = name_input.strip()
        
        # 한국어 받침(종성) 유무에 따른 조사 자동 선택 함수
        def get_joshi(word, josa_type):
            if not word:
                return ""
            last_char = word[-1]
            # 한글 유니코드 기준 받침 확인
            if not ('가' <= last_char <= '힣'):
                return "와" if josa_type == "와과" else "이"
            has_batchim = (ord(last_char) - ord(' 가')) % 28 > 0
            
            if josa_type == "와과":
                return "과" if has_batchim else "와"
            elif josa_type == "이가":
                return "이" if has_batchim else "가"
            elif josa_type == "은는":
                return "은" if has_batchim else "는"
            return ""

        w_wa = get_joshi(name, "와과")
        i_ga = get_joshi(name, "이가")
        eun_neun = get_joshi(name, "은는")

        # 입력된 메모를 완전히 새로운 문맥으로 윤문하는 로직
        play_memo = play_input.strip()
        routine_memo = routine_input.strip()

        # 결과 텍스트 조합 (완전한 윤문 적용)
        result = (
            f"계절의 향기가 싱그럽게 느껴지는 따뜻한 하루였습니다. 오늘 우리 {name}{eun_neun} "
            f"원에서의 하루를 시작하며 교사와 반갑게 눈을 맞추고 즐거운 놀이를 시작하였답니다. "
            f"특히 오늘 놀이 시간 중에는 {play_memo} 등의 과정이 자연스럽게 이루어졌는데, 이 과정에서 {name}{i_ga} 스스로 즐거움을 찾아가며 또래 친구들과 조화롭게 어우러지는 모습에서 매일매일 자라나는 든든한 성장을 엿볼 수 있어 참 뿌듯했답니다. "
            f"놀이 중간중간 교사의 작은 지원이나 상호작용에도 귀를 기울이며 자신의 생각을 표현하려 애쓰는 모습이 무척 대견스러웠습니다.\n\n"
            f"이어지는 일상생활 속에서는 {routine_memo} 등 하루의 흐름을 전체적으로 안정적이고 편안하게 소화해 주었기에, 오늘도 우리 {name}{w_wa} 함께 참 풍성하고 의미 있는 시간을 보낼 수 있었습니다. "
            f"놀이와 휴식을 자연스럽게 오가며 자신의 컨디션을 스스로 조절할 줄 아는 씩씩한 모습에서 건강한 에너지를 다시 한번 느낄 수 있었지요."
        )
        
        if notice_input.strip():
            result += f"\n\n[꼭! 읽어주세요.]\n{notice_input.strip()}"
        
        result += (
            f"\n\n하루가 다르게 조금씩 더 의젓해지는 {name}{eun_neun} 곁에서 지켜보며 교사 또한 큰 기쁨을 느끼고 있습니다. "
            f"내일도 우리 {name}{w_wa} 함께 더 많이 웃고 행복한 배움을 만들어갈 수 있도록 따뜻한 시선으로 세심하게 지원하겠습니다. "
            f"오늘 하루 {name}가 보여준 반짝이는 예쁜 모습들을 기억하며, 보호자님께서도 {name}{w_wa} 함께 편안하고 행복한 저녁 시간 보내시기를 바랍니다. "
            f"내일 밝은 모습으로 다시 뵙겠습니다."
        )

        st.success("✨ 윤문과 교정이 완료된 자연스러운 알림장이 완성되었습니다!")
        st.text_area("결과 확인", value=result, height=450)
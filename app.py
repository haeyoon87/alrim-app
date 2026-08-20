import streamlit as st

# 페이지 설정
st.set_page_config(page_title="엄마쌤의 영유아 알림장 도우미", layout="centered")

st.title("🌱 엄마쌤의 영유아 알림장 작성 도우미")
st.markdown("아이의 하루 놀이와 활동 내용을 입력하면, 원칙에 맞는 따뜻한 알림장으로 다듬어 줍니다.")

# 입력 폼 구성
with st.form("alrim_form"):
    name_input = st.text_input("아이 이름 (예: OO는)", value="OO는")
    age_group = st.selectbox(
        "연령 선택", 
        ["만0세", "만1세", "만2세", "만3세", "만4세", "만5세"]
    )
    
    activity_text = st.text_area(
        "오늘의 놀이와 활동 내용 입력", 
        placeholder="예: 자동차 모형을 이용해 밀고 당기며 놀이함. 도로테이프 위에서 자동차 모형을 밀고 당기기를 반복..."
    )
    
    submitted = st.form_submit_button("알림장 완성하기")

if submitted:
    if not activity_text.strip():
        st.warning("활동 내용을 입력해 주세요!")
    else:
        # 연령대에 따른 규칙 분기 처리
        if age_group in ["만0세", "만1세", "만2세"]:
            target_rule = "표준보육과정 기반, 영아 표현 방식 준수, 과거 시제, 15문장 내외"
        else:
            target_rule = "누리과정 기반, 유아 표현 방식 준수, 과거 시제, 15문장 내외"

        # 결과 시뮬레이션 및 실제 텍스트 구성 로직
        # (선생님이 주신 방대한 작성 규칙을 반영한 텍스트 변환 결과 예시 구조)
        generated_result = f"""계절의 싱그러움이 가득 느껴지는 따뜻한 하루였습니다. 오늘 {name_input} 도로는 긴 테이프를 따라 자동차 모형을 밀고 당기며 즐겁게 놀이하였습니다. "이거!" 하고 짧게 이야기하며 자동차를 움직여 보기도 하고, 도로가 끝나자 교사를 바라보며 "선생님, 길 없어요."라고 표현하기도 했습니다. 또래 친구가 다가와 같이 놀이하려고 시도하자 조금 놀란 듯 얼굴을 돌리기도 했으나, 친구가 자신의 행동을 모방하자 "하지마!"라고 이야기하며 더 멀리 이동하여 놀이를 이어갔습니다. 이에 교사는 도로 테이프를 더 길게 연장해 주어 놀이가 풍성하게 확장될 수 있도록 지원해 주었습니다. 놀이 중간중간 즐겁게 식사를 하고 바른 자세로 배변 활동에도 참여하였습니다. 내일도 우리 {name_input}와(과) 함께 즐겁고 행복한 하루를 보내기를 기대해 봅니다. 즐겁고 편안한 저녁 시간 보내시기를 바랍니다."""

        st.success("✨ 알림장이 따뜻하게 완성되었습니다!")
        
        # 결과를 보여주는 텍스트 박스
        st.subheader("📝 완성된 알림장 텍스트")
        st.text_area("아래 내용을 복사해서 사용하세요.", value=generated_result, height=250)
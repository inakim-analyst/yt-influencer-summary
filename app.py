# app.py (Colab에서 작성할 기본 코드 예시)
import streamlit as st

st.set_page_config(page_title="유튜브 인플루언서 영상 요약기", layout="wide")

st.title("유튜브 영상 요약 보기")
st.markdown("5인의 인플루언서 채널에서 최근 7일 업로드된 롱폼 영상을 요약합니다.")

# 예시 UI: 왼쪽에 썸네일 목록, 오른쪽에 요약 정보
col1, col2 = st.columns([1, 2])

with col1:
    st.header("영상 리스트")
    st.image("https://img.youtube.com/vi/abc123/default.jpg", caption="예시 영상 제목")
    st.image("https://img.youtube.com/vi/def456/default.jpg", caption="예시 영상 제목")

with col2:
    st.header("영상 요약 결과")
    st.subheader("영상명: [예시]")
    st.write("요약 내용: 이 영상에서는 000 제품이 소개되고, 000 기능이 강조됨...")
    st.markdown("**소개된 상품 정보**")
    st.markdown("1) 브랜드명 모델명 - 주요 특징\n2) ...")

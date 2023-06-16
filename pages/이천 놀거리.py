import streamlit as st

st.title("이천 놀거리")

st.header("이천 별빛정원우주")
st.video("https://www.youtube.com/watch?v=PK6WJVr5hrA")  # 유튜브 링크

def get_play_detail():
    st.header(st.session_state['detail'])

    # link = "link = "https://naver.com""
    link = st.session_state['link']
    st.write(f"[**🔗 네이버플레이스링크**]({link}")


st.header("이천 카페투어")
st.header("이천 설봉공원")
st.header("이천 예스파크")
st.header("이천 테르메덴")
st.header("이천 케르비안")

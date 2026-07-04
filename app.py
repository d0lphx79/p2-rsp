import streamlit as st
import random

st.set_page_config(page_title="가위바위보", page_icon="✊", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp{
    background-color:#ffb6d9;
}

h1,h2,h3,p,div{
    color:white !important;
    font-weight:bold !important;
    text-align:center;
}

.stButton>button{
    width:100%;
    height:80px;
    font-size:30px;
    border-radius:20px;
    background-color:white;
    color:#ff4fa3;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Session ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

if "user" not in st.session_state:
    st.session_state.user = ""

if "computer" not in st.session_state:
    st.session_state.computer = ""

# ---------------- 승패판정 ----------------
def judge(user, com):
    if user == com:
        return "draw"

    if (user=="✊" and com=="✌️") or \
       (user=="✌️" and com=="✋") or \
       (user=="✋" and com=="✊"):
        return "win"

    return "lose"

# ---------------- 메인화면 ----------------
if st.session_state.page == "main":

    st.markdown("<h1>선택하세요 ╰(*°▽°*)╯</h1>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    if c1.button("✊"):
        st.session_state.user="✊"
        st.session_state.computer=random.choice(["✊","✌️","✋"])
        st.session_state.page="result"
        st.rerun()

    if c2.button("✌️"):
        st.session_state.user="✌️"
        st.session_state.computer=random.choice(["✊","✌️","✋"])
        st.session_state.page="result"
        st.rerun()

    if c3.button("✋"):
        st.session_state.user="✋"
        st.session_state.computer=random.choice(["✊","✌️","✋"])
        st.session_state.page="result"
        st.rerun()

# ---------------- 결과화면 ----------------
else:

    result = judge(st.session_state.user,
                   st.session_state.computer)

    st.markdown(f"## 당신 : {st.session_state.user}")
    st.markdown(f"## 상대 : {st.session_state.computer}")

    st.write("")

    if result=="draw":
        st.markdown("# 🤝 DRAW!")

    elif result=="win":

        st.balloons()

        st.markdown("""
        <h1 style="font-size:60px;">
        🎉 YOU WIN 🎉
        </h1>
        """, unsafe_allow_html=True)

        # 춤추는 고양이 GIF
        st.image(
            "https://media.tenor.com/5ry-200hErMAAAAC/cat-dance.gif",
            width=350
        )

    else:

        st.markdown("""
        <h1 style="font-size:60px;">
        😭 YOU LOSE 😭
        </h1>
        """, unsafe_allow_html=True)

        st.markdown(
            "<div style='font-size:120px;'>😢</div>",
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    if st.button("처음으로 돌아가기"):
        st.session_state.page="main"
        st.rerun()

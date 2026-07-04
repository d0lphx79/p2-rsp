import streamlit as st
import random

st.set_page_config(
    page_title="가위바위보",
    page_icon="✊",
    layout="centered"
)

# ================= CSS =================

st.markdown("""
<style>

.stApp{
    background:#ffb6d9;
}

h1,h2,h3,p{
    color:white;
    text-align:center;
    font-weight:bold;
}

div{
    color:white;
}

.stButton>button{
    width:100%;
    height:170px;
    font-size:90px;
    font-weight:bold;
    border-radius:25px;
    border:none;
    background:white;
    color:#ff4f9d;
    transition:0.2s;
}

.stButton>button:hover{
    transform:scale(1.08);
    background:#fff3f9;
}

.result{
    text-align:center;
    font-size:60px;
    color:white;
    font-weight:bold;
}

.big{
    font-size:120px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ================= Session =================

if "page" not in st.session_state:
    st.session_state.page="main"

if "user" not in st.session_state:
    st.session_state.user=""

if "computer" not in st.session_state:
    st.session_state.computer=""

# ================= 승패판정 =================

def judge(user, computer):

    if user==computer:
        return "draw"

    if (
        (user=="✊" and computer=="✌️")
        or
        (user=="✌️" and computer=="✋")
        or
        (user=="✋" and computer=="✊")
    ):
        return "win"

    return "lose"

# ================= 메인 =================

if st.session_state.page=="main":

    st.markdown(
        "<h1 style='font-size:55px;'>선택하세요 ╰(*°▽°*)╯</h1>",
        unsafe_allow_html=True
    )

    c1,c2,c3=st.columns(3)

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

# ================= 결과 =================

else:

    result=judge(
        st.session_state.user,
        st.session_state.computer
    )

    st.markdown(
        f"<h2>😊 당신 : {st.session_state.user}</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h2>🤖 컴퓨터 : {st.session_state.computer}</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    if result=="win":

        st.balloons()

        st.markdown(
            "<div class='result'>🎉 YOU WIN! 🎉</div>",
            unsafe_allow_html=True
        )

        # 춤추는 고양이 GIF
        st.markdown(
            """
            <div style="display:flex;justify-content:center;">
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTF5d2J0bnl5eDljMWQ0bjA2a2M2dGRwMG9qYjRvdTRzNG11ZXN2NyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lJNoBCvQYp7nq/giphy.gif" width="350">
            </div>
            """,
            unsafe_allow_html=True
        )

    elif result=="lose":

        st.markdown(
            "<div class='result'>😭 YOU LOSE 😭</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='big'>😢</div>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            "<div class='result'>🤝 DRAW 🤝</div>",
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    if st.button("🔄 처음으로 돌아가기"):
        st.session_state.page="main"
        st.rerun()

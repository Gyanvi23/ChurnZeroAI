import streamlit as st
from layout import show_layout


st.set_page_config(
layout="wide",
initial_sidebar_state=
"collapsed"
)
show_layout()
st.markdown(
"""
<style>

.main{
background:
linear-gradient(
135deg,
#0B1120,
#1E293B,
#2563EB
);
}

.login{

background:
rgba(
255,
255,
255,
0.05
);

padding:40px;

border-radius:20px;

backdrop-filter:
blur(15px);

width:450px;

margin:auto;

margin-top:120px;

text-align:center;
}

</style>
""",

unsafe_allow_html=True
)

st.markdown(
"""
<div class="login">

<h1>
🚀 ChurnZero AI
</h1>

<h3>
Predict • Explain • Retain
</h3>

</div>
""",

unsafe_allow_html=True
)

user = st.text_input(
"Username"
)

password = st.text_input(
"Password",
type="password"
)

role = st.selectbox(

"Role",

[
"Manager",
"Analyst",
"Executive"
]
)
if role=="Executive":

    st.info(
    "Executive Dashboard Enabled"
    )

if st.button(
"Login"
):

    with st.spinner(
    "Loading AI Engine..."
    ):

        import time

        time.sleep(2)

    st.success(
    "Welcome"
    )
    st.info(
    f"""
    Role :

    {role}

    AI Banking System Ready
    """
    )
    st.switch_page(
    "pages/1_🏠_Home.py"
    )
    st.markdown(
    """
    <div style='
    text-align:center;
    font-size:70px;
    '>
    🤖
    </div>
    """,
    unsafe_allow_html=True
    )
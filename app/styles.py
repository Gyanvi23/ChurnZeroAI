import streamlit as st

def load_css():

    dark = st.session_state.get(
        "dark_mode",
        True
    )

    if dark:

        bg = """
        linear-gradient(
        135deg,
        #0B1120,
        #111827,
        #1E293B
        )
        """

        sidebar = """
        linear-gradient(
        180deg,
        #111827,
        #1E293B
        )
        """

        text = "white"

    else:

        bg = """
        linear-gradient(
        135deg,
        #F8FAFC,
        #E2E8F0,
        #FFFFFF
        )
        """

        sidebar = """
        linear-gradient(
        180deg,
        #FFFFFF,
        #E5E7EB
        )
        """

        text = "black"

    st.markdown(
f"""
<style>

/* APP */

.stApp {{
background:{bg};
color:{text};
}}

[data-testid="stAppViewContainer"]{{
background:{bg};
}}

[data-testid="stHeader"]{{
background:transparent;
}}

/* SIDEBAR */

section[data-testid="stSidebar"]{{
background:{sidebar};
}}

/* TITLES */

h1,h2,h3,h4,h5,h6,p,label{{
color:{text} !important;
}}

/* BUTTON */

.stButton button{{
background:linear-gradient(
90deg,
#06B6D4,
#2563EB
) !important;

color:white !important;

border:none !important;

border-radius:14px !important;
}}

/* DOWNLOAD */

.stDownloadButton button{{
background:linear-gradient(
90deg,
#06B6D4,
#2563EB
) !important;

color:white !important;

border:none !important;
}}

/* SELECTBOX */

div[data-baseweb="select"]{{
background:#1F2937 !important;
border-radius:12px;
}}

div[data-baseweb="select"] span{{
color:white !important;
}}

div[role="listbox"]{{
background:white !important;
}}

div[role="option"]{{
color:black !important;
background:white !important;
}}

div[role="option"]:hover{{
background:#E5E7EB !important;
}}

/* TABLE */

table{{
background:white;
color:black;
}}
.navbar{{

display:flex;

justify-content:center;

gap:20px;

padding:15px;

background:rgba(
255,
255,
255,
0.05
);

backdrop-filter:blur(15px);

border-radius:20px;

margin-bottom:25px;

}}

.navbtn{{

padding:12px 22px;

border-radius:15px;

background:
linear-gradient(
90deg,
#06B6D4,
#2563EB
);

color:white;

font-weight:bold;

text-decoration:none;

}}
.ai{{

position:fixed;

bottom:25px;

right:25px;

width:70px;

height:70px;

border-radius:50%;

background:
linear-gradient(
90deg,
#06B6D4,
#7C3AED
);

display:flex;

justify-content:center;

align-items:center;

font-size:34px;

box-shadow:
0 0 25px #06B6D4;

z-index:9999;

}}
.topbar{{

display:flex;

justify-content:space-between;

align-items:center;

padding:18px;

background:rgba(
255,
255,
255,
0.05
);

backdrop-filter:
blur(20px);

border-radius:20px;

margin-bottom:25px;

}}

.hero-card{{

padding:35px;

border-radius:25px;

background:
linear-gradient(

135deg,

rgba(37,99,235,.2),

rgba(124,58,237,.2)

);

backdrop-filter:
blur(15px);

margin-bottom:25px;

}}
.ai-float{{

position:fixed;

bottom:18px;

right:18px;

width:52px;

height:52px;

border-radius:50%;

background:

linear-gradient(

90deg,

#06B6D4,

#2563EB

);

display:flex;

justify-content:center;

align-items:center;

font-size:20px;

box-shadow:

0 0 15px

#2563EB;



}}
</style>
""",
unsafe_allow_html=True
)

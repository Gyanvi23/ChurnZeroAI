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

</style>
""",
unsafe_allow_html=True
)
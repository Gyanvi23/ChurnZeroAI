import streamlit as st

import streamlit as st

def load_css():

    import os
    import json

    base = os.path.dirname(
    os.path.abspath(__file__)
    )

    theme_path = os.path.join(
    base,
    "theme.json"
    )

    if os.path.exists(
    theme_path
    ):

        with open(
        theme_path,
        "r"
        ) as f:

            saved = json.load(f)

            dark = saved.get(
            "dark_mode",
            True
            )

    else:

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

        sidebar_btn = "rgba(255,255,255,0.08)"

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

        sidebar_btn = "rgba(0,0,0,0.05)"

    select_bg = "#1F2937" if dark else "#FFFFFF"
    select_text = "white" if dark else "black"

    st.markdown(
        f"""
<style>

/* APP */

.stApp {{
    background: {bg};
    color: {text};
}}

[data-testid="stAppViewContainer"] {{
    background: {bg};
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

/* SIDEBAR */

section[data-testid="stSidebar"] {{
    background: {sidebar} !important;
}}

section[data-testid="stSidebar"] > div {{
    background: {sidebar} !important;
}}

section[data-testid="stSidebar"] * {{
    color: {text} !important;
}}

/* SIDEBAR BUTTONS */

section[data-testid="stSidebar"] button {{
    color: {text} !important;
    background: {sidebar_btn} !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}}

/* EXPANDERS */

section[data-testid="stSidebar"] details {{
    background: transparent !important;
}}

section[data-testid="stSidebar"] details summary p {{
    color: {text} !important;
    font-weight: 600 !important;
}}

/* TITLES */

h1,h2,h3,h4,h5,h6,p,label,span {{
    color: {text} !important;
}}

/* BUTTON */

.stButton button {{
    background: linear-gradient(
    90deg,
    #06B6D4,
    #2563EB
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 14px !important;
}}

/* DOWNLOAD BUTTON */

.stDownloadButton button {{
    background: linear-gradient(
    90deg,
    #06B6D4,
    #2563EB
    ) !important;

    color: white !important;
    border: none !important;
}}

/* SELECTBOX */

div[data-baseweb="select"] {{
    background: {select_bg} !important;
    border-radius: 12px;
}}

div[data-baseweb="select"] span {{
    color: {select_text} !important;
}}

div[role="listbox"] {{
    background: white !important;
}}

div[role="option"] {{
    color: black !important;
    background: white !important;
}}

div[role="option"]:hover {{
    background: #E5E7EB !important;
}}

/* TABLE */

table {{
    background: white;
    color: black;
}}

/* NAVBAR */

.navbar {{

    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 15px;

    background: rgba(255,255,255,0.05);

    backdrop-filter: blur(15px);

    border-radius: 20px;

    margin-bottom: 25px;
}}

.navbtn {{

    padding: 12px 22px;

    border-radius: 15px;

    background: linear-gradient(
    90deg,
    #06B6D4,
    #2563EB
    );

    color: white;

    font-weight: bold;

    text-decoration: none;
}}

/* TOPBAR */

.topbar {{

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px;

    background: rgba(255,255,255,0.05);

    backdrop-filter: blur(20px);

    border-radius: 20px;

    margin-bottom: 25px;
}}

/* HERO CARD */

.hero-card {{

    padding: 35px;

    border-radius: 25px;

    background: linear-gradient(
    135deg,
    rgba(37,99,235,.2),
    rgba(124,58,237,.2)
    );

    backdrop-filter: blur(15px);

    margin-bottom: 25px;
}}

</style>
""",
        unsafe_allow_html=True
    )
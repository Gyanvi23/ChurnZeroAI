
import streamlit as st

from ai_bot import show_ai_bot
def show_layout():

    st.markdown("""
<style>

/* HIDE DEFAULT STREAMLIT NAV */

[data-testid="stSidebarNav"]{
display:none;
}

section[data-testid="stSidebar"] ul{
display:none;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{

width:220px !important;

background:
linear-gradient(
180deg,
#111827,
#0F172A
);

}

/* NAVBAR */

.topbar{

display:flex;

justify-content:space-between;

align-items:center;

padding:18px 28px;

margin-bottom:28px;

gap:25px;

border-radius:22px;

background:
rgba(
10,
15,
35,
0.72
);

backdrop-filter:blur(14px);

box-shadow:
0 10px 30px rgba(
0,
0,
0,
0.45
);

}

/* LOGO */

.logo{

font-size:24px;
margin-right:10px;
font-weight:700;

white-space:nowrap;

background:
linear-gradient(
90deg,
#00E5FF,
#FF3EF5
);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}

/* BUTTON CONTAINER */

.links{

display:flex;

gap:10px;

align-items:center;

flex-wrap:nowrap;

}

/* NAV BUTTONS */

.navbtn{

padding:10px 14px;

border-radius:14px;

background:
rgba(
255,
255,
255,
0.04
);

border:
1px solid rgba(
255,
255,
255,
0.05
);

backdrop-filter:blur(8px);

font-size:14px;

font-weight:600;

color:white !important;

text-decoration:none;

min-width:95px;

text-align:center;

transition:.3s;

}

.navbtn:hover{

background:
linear-gradient(
90deg,
#2563EB,
#06B6D4
);

transform:
translateY(-2px);

box-shadow:
0 0 18px rgba(
6,
182,
212,
0.4
);

}

@keyframes pulse{

50%{

transform:scale(
1.05
);

}

}


</style>

<div class="topbar">

<div class="logo">

🚀 ChurnZero AI

</div>

<div class="links">

<a class="navbtn" target="_self"
href="/Home">
🏠 Home
</a>

<a class="navbtn" target="_self"
href="/Prediction">
🧠 Prediction
</a>

<a class="navbtn" target="_self"
href="/Dashboard">
📊 Dashboard
</a>

<a class="navbtn" target="_self"
href="/Alerts">
🔔 Alerts
</a>

<a class="navbtn" target="_self"
href="/Customer_Profile">
👤 Profile
</a>

<a class="navbtn" target="_self"
href="/Login">
🔐 Login
</a>

</div>

</div>
""",

unsafe_allow_html=True
)

    # SIDEBAR

    with st.sidebar:

        st.title(
        "☰ Menu"
        )

        with st.expander(
        "📊 Analytics"
        ):

            st.page_link(
            "pages/5_📊_Dashboard.py",
            label="Dashboard"
            )

            st.page_link(
            "pages/3_⚠_Risk.py",
            label="Risk"
            )

            st.page_link(
            "pages/4_🎯_Retention.py",
            label="Retention"
            )

            st.page_link(
            "pages/13_💰_Business_Impact.py",
            label="Business Impact"
            )

        with st.expander(
        "👥 Customer"
        ):

            st.page_link(
            "pages/7_👤_Customer_Profile.py",
            label="Profile"
            )

            st.page_link(
            "pages/8_🔍_Customer_Search.py",
            label="Search"
            )

            st.page_link(
            "pages/9_⚖_Compare_Customers.py",
            label="Compare"
            )

            st.page_link(
            "pages/11_🛤_Customer_Journey.py",
            label="Journey"
            )

        with st.expander(
        "🏢 Management"
        ):

            st.page_link(
            "pages/10_🚀_Executive_Command_Center.py",
            label="Executive"
            )

            st.page_link(
            "pages/12_🧑‍💼_Manager_Action_Center.py",
            label="Manager"
            )
    show_ai_bot()
    st.markdown("""

    <style>

    iframe{

    position:fixed !important;

    bottom:20px !important;

    right:20px !important;

    top:auto !important;

    left:auto !important;

    width:360px !important;

    height:560px !important;

    z-index:999999 !important;

    border:none !important;

    background:transparent !important;

    }

    </style>

    """,

    unsafe_allow_html=True
    )
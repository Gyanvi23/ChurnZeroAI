import streamlit as st
from styles import load_css
if "dark_mode" not in st.session_state:

    st.session_state.dark_mode = True

theme = st.toggle(

"Dark Mode",

value=
st.session_state.dark_mode

)

st.session_state.dark_mode = theme

load_css()
demo = st.toggle(
"Demo Mode"
)
st.success(
"Demo Customer Loaded"
)
with st.spinner(
"Launching AI Engine..."
):

    import time

    time.sleep(2)


st.markdown(
"""
<div class="hero">

<h1>
🚀 ChurnZero AI
</h1>

<h3>
Predict • Explain • Retain
</h3>

AI Powered Banking Customer Intelligence Platform

</div>
""",

unsafe_allow_html=True
)

a,b,c,d = st.columns(4)

a.metric(
"Customers",
"12,540"
)

b.metric(
"Risk",
"18%"
)

c.metric(
"Retention",
"82%"
)

d.metric(
"Revenue Saved",
"$2.4M"
)

st.divider()

left,right = st.columns([2,1])

with left:

    st.subheader(
    "Platform Overview"
    )

    st.info(
"""
🧠 Predict customer churn

⚠ Analyze customer risk

🎯 Generate retention actions

📊 Business dashboard
"""
)

with right:

    st.success(
"""
System Status

AI Engine: Active

Prediction: Running

Risk Monitor: Active
"""
)
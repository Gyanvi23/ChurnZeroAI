import streamlit as st
from styles import load_css

load_css()

st.markdown(
"""
<div class="hero">

<h1>
🧠 Prediction Engine
</h1>

<h3>
AI Churn Detection
</h3>

</div>
""",

unsafe_allow_html=True
)

a,b,c = st.columns(3)

a.metric(
"Confidence",
"92%"
)

b.metric(
"Risk",
"High"
)

c.metric(
"Probability",
"0.82"
)

st.markdown(
"""
<div class="glass">

<h2>
Likely To Churn
</h2>

Customer requires attention.

</div>
""",

unsafe_allow_html=True
)
st.divider()

st.subheader(
"🤖 AI Assistant"
)

query = st.text_input(
"Ask AI"
)

if query:

    st.info(
"""
Suggested Action:

Prioritize retention campaign for risky customers.
"""
)
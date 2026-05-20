import streamlit as st
from styles import load_css

load_css()

st.markdown(
"""
<div class="hero">

<h1>
🔍 Customer Search
</h1>

</div>
""",

unsafe_allow_html=True
)

customer = st.text_input(
"Enter Customer ID"
)

if customer:

    st.success(
f"""
Customer : {customer}

Segment : High Risk

Probability : 82%

Recommendation :

Assign RM
"""
)
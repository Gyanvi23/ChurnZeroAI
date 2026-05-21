import streamlit as st
from styles import load_css


from layout import show_layout
st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
)
load_css()
show_layout()

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

cust = st.session_state.get(
"customer",
{}
)

customer = st.text_input(
"Enter Customer ID"
)

if customer:

    risk = cust.get(
    "risk_prob",
    0
    )

    balance = cust.get(
    "balance",
    0
    )

    age = cust.get(
    "age",
    0
    )

    salary = cust.get(
    "salary",
    0
    )

    if risk>0.8:

        action = (
        "Assign RM"
        )

        segment = (
        "High Risk"
        )

    elif risk>0.5:

        action = (
        "Offer Cashback"
        )

        segment = (
        "Medium Risk"
        )

    else:

        action = (
        "No Action Needed"
        )

        segment = (
        "Retained"
        )

    st.success(

f"""
Customer :

{customer}

Age :

{age}

Balance :

₹{balance}

Salary :

₹{salary}

Segment :

{segment}

Probability :

{round(risk*100)}%

Recommendation :

{action}
"""
    )
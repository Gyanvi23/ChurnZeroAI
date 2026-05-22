import streamlit as st
from styles import load_css


from layout import show_layout
import pandas as pd
import os
st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
)
load_css()
show_layout()
base = os.path.dirname(
os.path.abspath(__file__)
)

csv_path = os.path.join(
base,
"..",
"..",
"data",
"Bank Customer Churn Prediction.csv"
)

df = pd.read_csv(
csv_path
)

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

    row = df[
        df["customer_id"].astype(str)
        ==
        customer
    ]

    if len(row)==0:

        st.error(
        "Customer not found"
        )

    else:

        row = row.iloc[0]

        age = row["age"]

        balance = row["balance"]

        salary = row["estimated_salary"]

        churn = row["churn"]

        risk = (
        0.9
        if churn==1
        else 0.2
        )

        if risk>0.8:

            action="Assign RM"

            segment="High Risk"

        elif risk>0.5:

            action="Offer Cashback"

            segment="Medium Risk"

        else:

            action="No Action Needed"

            segment="Retained"

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

Recommendation :

{action}
"""
        )
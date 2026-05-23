import streamlit as st
from styles import load_css


from layout import show_layout
import pandas as pd
import os
st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
)
base = os.path.dirname(
os.path.abspath(__file__)
)

theme_path = os.path.join(
base,
"..",
"..",
"theme.json"
)

theme_path = os.path.abspath(
theme_path
)

import json

if os.path.exists(
theme_path
):

    with open(
    theme_path,
    "r"
    ) as f:

        saved = json.load(f)

        st.session_state.dark_mode = saved.get(
        "dark_mode",
        True
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
"ChurnZero_dataset_v1.csv"
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

customer = st.number_input(
"Enter Customer Index",
min_value=0,
max_value=len(df)-1,
step=1
)

if customer:

    row = df.iloc[
    int(customer)
    ]

    if len(row)==0:

        st.error(
        "Customer not found"
        )

    else:

        

        age = row["age"]

        income = row["annual_income"]

        balance = row["current_balance"]

        logins = row[
        "mobile_app_login_count"
        ]

        churn = row["churn"]

        risk = round(
        float(
        row["churn_probability"]
        )
        if "churn_probability" in df.columns
        else (
        0.9
        if churn == 1
        else 0.2
        ),
        2
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

            Income :

            ₹{income}

            Digital Logins :

            {logins}

            Segment :

            {segment}

            Recommendation :

            {action}
            """
            )
            st.metric(
            "Risk Score",
            f"{round(risk*100)}%"
            )
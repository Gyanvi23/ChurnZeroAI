import streamlit as st
import pandas as pd
import os
import time

from styles import load_css
from layout import show_layout

st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
)

# THEME

# THEME

import json

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

else:

    if "dark_mode" not in st.session_state:

        st.session_state.dark_mode = True


load_css()
show_layout()
import json

risk_prob = 0

if os.path.exists(
"selected_customer.json"
):

    with open(
    "selected_customer.json",
    "r"
    ) as f:

        customer = json.load(
        f
        )

        risk_prob = customer.get(
        "risk_prob",
        0
        )

# LOAD DATASET

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

# KPI CALCULATIONS

total_customers = len(df)

high_risk = len(
df[df["churn"]==1]
)

retained = len(
df[df["churn"]==0]
)

risk_percent = round(
(high_risk/total_customers)*100
)

retention = round(
(retained/total_customers)*100
)

saved = int(
df["annual_income"].sum()*0.05
)



# HERO

st.markdown(
"""

<div class="hero-card">

<h1>

🚀 ChurnZero AI

</h1>

<h2>

Predict • Explain • Retain

</h2>

<p>

AI Banking Customer Intelligence Platform

</p>

</div>

""",

unsafe_allow_html=True
)

# KPI ROW

a,b,c,d = st.columns(4)

a.metric(
"Customers",
total_customers
)

b.metric(
"Predicted Risk",
f"{round(risk_prob*100)}%"
)

c.metric(
"Retention",
f"{retention}%"
)

d.metric(
"Revenue Saved",
f"₹{saved}"
)

st.divider()

left,right = st.columns([2,1])

with left:

    st.subheader(
    "Platform Overview"
    )

    st.info(
f"""
 🧠 Predict customer churn

⚠ High Risk Customers : {high_risk}

🎯 Retained Customers : {retained}

📊 Customer Intelligence Dashboard

🤖 Logistic Regression Model

🎯 Cross Validation Accuracy : 93.5%
"""
)

with right:

    st.success(
"""
System Status

AI Engine : Active

Prediction Model : Logistic Regression

Customer Intelligence : Active
"""
)
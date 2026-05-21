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

if "dark_mode" not in st.session_state:

    st.session_state.dark_mode = True

theme = st.toggle(
"Dark Mode",
value=st.session_state.dark_mode
)

st.session_state.dark_mode = theme

load_css()
show_layout()

# LOAD DATASET

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
df["balance"].sum()*0.2
)

# DEMO

demo = st.toggle(
"Demo Mode"
)

if demo:

    st.success(
    "Demo Customer Loaded"
    )

with st.spinner(
"Launching AI Engine..."
):

    time.sleep(2)

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
"Risk",
f"{risk_percent}%"
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

📊 Dataset Driven Dashboard
"""
)

with right:

    st.success(
"""
System Status

AI Engine : Active

Prediction : Running

Risk Monitor : Active
"""
)
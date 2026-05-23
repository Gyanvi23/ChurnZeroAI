import os
import streamlit as st
import pandas as pd
import plotly.express as px
from styles import load_css
from pdf_export import create_executive_pdf

from layout import show_layout
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
total_customers = len(df)

high_risk = len(
    df[df["churn"]==1]
)

retained = len(
    df[df["churn"]==0]
)

risk_prob = high_risk / total_customers

retention = round(
    retained/total_customers * 100
)

saved = int(
df["annual_income"].sum()*0.05
)

name = f"{total_customers} Customers"
st.markdown(
"""
<div class="hero">

<h1>
🚀 Executive Command Center
</h1>

<h3>
Banking Customer Intelligence Platform
</h3>

</div>
""",

unsafe_allow_html=True
)

# TOP KPIs

a,b,c,d = st.columns(4)
import json

pred_risk = 0

if os.path.exists(
"selected_customer.json"
):

    with open(
    "selected_customer.json",
    "r"
    ) as f:

        cust = json.load(f)

        pred_risk = cust.get(
        "risk_prob",
        0
        )

st.metric(
"Predicted Risk",
f"{round(pred_risk*100)}%"
)

a.metric(
"Customer",
name
)

b.metric(
"Churn %",
f"{round(risk_prob*100)}%"
)

c.metric(
"Revenue Saved",
f"₹{saved}"
)

d.metric(
"Live Alerts",

1 if risk_prob>0.5 else 0

)
st.divider()

# ALERTS + SEARCH

left,right = st.columns(2)

with left:

    st.subheader(
    "🔔 Live Alerts"
    )

    if risk_prob > 0.8:

        st.error(
    f"""
    {name}

    High churn risk

    {round(risk_prob*100)}%
    """
        )

    elif risk_prob > 0.5:

        st.warning(
        "Medium risk customer"
        )

    else:

        st.success(
    "Customer retained"
    )

with right:

    st.subheader(
    "🔍 Customer Search"
    )

    cid = st.number_input(
    "Customer Index",
    0,
    len(df)-1
    )

    if cid:

        if risk_prob > 0.8:

            action = "Assign RM"

        elif risk_prob > 0.5:

            action = "Offer Cashback"

        else:

            action = "No action needed"

        st.info(

f"""
Customers :

{total_customers}

Risk :

{round(risk_prob*100)}%

Revenue Saved :

₹{saved}

Action :

{action}

"""
)
st.divider()

# DASHBOARD

retained_count = len(
    df[df["churn"]==0]
)

high_risk_count = len(
    df[df["churn"]==1]
)

medium_count = max(
    total_customers
    - retained_count
    - high_risk_count,
    0
)

data = pd.DataFrame({

"Segment":[
"Retained",
"Medium Risk",
"High Risk"
],

"Count":[
retained_count,
medium_count,
high_risk_count
]

})

c1,c2 = st.columns(2)

with c1:

    fig = px.bar(

    data,

    x="Segment",

    y="Count",

    title="Customer Segments"
    )
    dark = st.session_state.get(
    "dark_mode",
    True
    )

    chart_text = (
        "white"
    if dark
    else "black"
    )
    fig.update_layout(

paper_bgcolor=
"rgba(0,0,0,0)",

plot_bgcolor=
"rgba(0,0,0,0)",

font_color=
chart_text

)
    st.plotly_chart(
    fig,
    use_container_width=True
    )
    st.divider()

st.subheader(
"🚨 Top Risk Customers"
)

risk = df[
df["churn"]==1
][[
"age",
"annual_income",
"current_balance",
"mobile_app_login_count",
"satisfaction_score"
]].head(10)

risk["Action"] = "Assign RM"

st.dataframe(

risk,

use_container_width=True
)
st.divider()

st.subheader(
"🧑‍💼 Manager Performance"
)

m1,m2,m3 = st.columns(3)

m1.metric(

"Actions",

high_risk

)

m2.metric(

"Recovered",

retained

)

m3.metric(
"Success Rate",

f"{retention}%"

)
with c2:

    pie = px.pie(

    data,

    names="Segment",

    values="Count"
    )
    pie.update_layout(

    paper_bgcolor=
    "rgba(0,0,0,0)",

    plot_bgcolor=
    "rgba(0,0,0,0)",

    font_color=
    chart_text

    )

    pie.update_traces(

    textfont_color=
    chart_text

    )
    
    st.plotly_chart(
    pie,
    use_container_width=True
    )

st.divider()

st.subheader(
"Customer Timeline"
)

events = [

f"Total Customers : {total_customers}",

f"High Risk Customers : {high_risk}",

f"Retained Customers : {retained}",

f"Revenue Saved : ₹{saved}",

f"Predicted Risk : {round(risk_prob*100)}%",

f"Retention : {retention}%"

]

for e in events:

    st.markdown(
    f"✅ {e}"
    )
st.divider()

st.subheader(
"💰 Business Impact"
)

c1,c2,c3 = st.columns(3)

c1.success(

f"""
Revenue Saved

₹{saved}
"""
)

c2.warning(

f"""
Retention Improved

{retention}%
"""
)

c3.info(

f"""
Customers Retained

{retained}
"""
)
heat = df[[

"age",

"annual_income",

"current_balance",

"monthly_transaction_count",

"satisfaction_score",

"churn"

]].corr()

fig = px.imshow(
heat,
text_auto=True,
title="Executive Risk Heatmap"
)

st.plotly_chart(
fig,
use_container_width=True
)

create_executive_pdf(

customer=total_customers,

risk=round(risk_prob*100),

saved=saved,

retention=retention

)

with open(

"executive_report.pdf",

"rb"

) as file:

    st.download_button(

    "📄 Export Executive Report",

    file,

    file_name=
    "executive_report.pdf"
    )

st.caption(
"🚀 ChurnZero AI | Predict • Explain • Retain"
)
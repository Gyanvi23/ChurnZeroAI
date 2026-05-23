import os
import streamlit as st
import pandas as pd
import plotly.express as px

from styles import load_css
from layout import show_layout

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
import json

risk_prob = 0

if os.path.exists(
"selected_customer.json"
):

    with open(
    "selected_customer.json",
    "r"
    ) as f:

        customer = json.load(f)

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

df = pd.read_csv(csv_path)

# KPIs FROM DATASET

total_customers = len(df)

high_risk = len(
    df[df["churn"] == 1]
)

retained = len(
    df[df["churn"] == 0]
)

retention = round(
    (retained / total_customers) * 100
)

saved = int(
    df["annual_income"].sum() * 0.05
)

risk_percent = round(
    (high_risk / total_customers) * 100
)

# TITLE

st.title(
    "📊 Analytics Dashboard"
)

st.caption(
    "Customer Insights"
)

st.divider()

# SEGMENT DATA

data = pd.DataFrame({

    "Category":[
        "Retained",
        "High Risk"
    ],

    "Count":[
        retained,
        high_risk
    ]

})

left,right = st.columns(2)

with left:

    fig = px.bar(
        data,
        x="Category",
        y="Count",
        title="Customer Segments"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    pie = px.pie(
        data,
        names="Category",
        values="Count",
        title="Distribution"
    )

    pie.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

# METRICS

k1,k2,k3 = st.columns(3)

k1.metric(
    "Customers",
    total_customers
)

k2.metric(
    "Retention",
    f"{retention}%"
)

k3.metric(
"Predicted Risk",
f"{round(risk_prob*100)}%"
)
st.divider()
st.subheader(
"Selected Customer Status"
)

if risk_prob > 0.7:

    st.error(
    f"""
⚠ High Risk Customer

Probability :
{round(risk_prob*100)}%
"""
    )

else:

    st.success(
    f"""
✅ Retained Customer

Probability :
{round(risk_prob*100)}%
"""
    )

# BUSINESS IMPACT

st.subheader(
    "Business Impact"
)

a,b,c = st.columns(3)

a.success(
f"""
Revenue Saved

₹{saved}
"""
)

b.warning(
f"""
Retention

{retention}%
"""
)

c.info(
f"""
Predicted Churn

{high_risk}
"""
)

st.subheader(
"Top Risk Drivers"
)

risk_features = df[[

"total_digital_logins",

"unresolved_complaint_count",

"balance_decline_percentage",

"monthly_transaction_count",

"mobile_app_login_count",

"churn"

]].corr()["churn"].abs()

risk_features = risk_features.sort_values(
ascending=False
)

fig2 = px.bar(

x=risk_features.index,

y=risk_features.values,

title="Feature Impact on Churn"

)

fig2.update_layout(

paper_bgcolor="rgba(0,0,0,0)",

plot_bgcolor="rgba(0,0,0,0)",

font_color="white"

)

st.plotly_chart(
fig2,
use_container_width=True
)

# DATASET HEATMAP

heat = df[[

    "age",

    "annual_income",

    "current_balance",

    "monthly_transaction_count",

    "mobile_app_login_count",

    "satisfaction_score",

    "churn"

]].corr()

fig = px.imshow(

    heat,

    text_auto=True,

    title="Customer Risk Correlation Heatmap",

    color_continuous_scale="RdBu"

)

fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
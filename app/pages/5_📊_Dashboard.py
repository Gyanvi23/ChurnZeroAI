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
    df["balance"].sum() * 0.2
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
    "Risk",
    f"{risk_percent}%"
)

st.divider()

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
Recovered

{retained}
"""
)



# DATASET HEATMAP

heat = df[[
    "credit_score",
    "age",
    "balance",
    "estimated_salary",
    "tenure",
    "products_number",
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
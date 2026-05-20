import streamlit as st
import pandas as pd
import plotly.express as px

st.title(
    "Customer Dashboard"
)

data = pd.DataFrame({

    "Category":[
        "VIP",
        "Silent",
        "High Risk"
    ],

    "Count":[
        30,
        20,
        50
    ]
})

fig = px.bar(
    data,
    x="Category",
    y="Count"
)

st.plotly_chart(
    fig
)

pie = px.pie(
    data,
    names="Category",
    values="Count"
)

st.plotly_chart(
    pie
)
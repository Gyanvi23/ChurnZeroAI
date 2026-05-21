import streamlit as st
import pandas as pd
from styles import load_css


from layout import show_layout
import os

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
⚖ Customer Comparison
</h1>

</div>
""",

unsafe_allow_html=True
)

left,right = st.columns(2)

with left:

    c1 = st.selectbox(
    "Customer 1",
    df["customer_id"]
    )

with right:

    c2 = st.selectbox(
    "Customer 2",
    df["customer_id"]
    )
    row1 = df[
    df["customer_id"] == c1
    ].iloc[0]

    row2 = df[
    df["customer_id"] == c2
    ].iloc[0]
    data = pd.DataFrame({

"Metric":[
"Risk",
"Balance",
"Salary",
"Age",
"Status"
],

c1:[

f"{int(row1['churn']*100)}%",

f"₹{row1['balance']}",

f"₹{row1['estimated_salary']}",

row1["age"],

"High Risk"
if row1["churn"]==1
else "Retained"

],

c2:[

f"{int(row2['churn']*100)}%",

f"₹{row2['balance']}",

f"₹{row2['estimated_salary']}",

row2["age"],

"High Risk"
if row2["churn"]==1
else "Retained"

]

})
st.divider()

st.subheader(
"AI Comparison Result"
)

if row1["churn"] > row2["churn"]:

    st.error(
    f"{c1} has higher churn risk"
    )

elif row1["churn"] < row2["churn"]:

    st.success(
    f"{c1} is healthier"
    )

else:

    st.info(
    "Both customers have similar risk"
    )
import plotly.express as px

chart = pd.DataFrame({

"Customer":[
c1,
c2
],

"Risk":[

int(
row1["churn"]*100
),

int(
row2["churn"]*100
)

]

})

fig = px.bar(

chart,

x="Customer",

y="Risk",

title="Risk Comparison"

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

st.subheader(
"Comparison Results"
)

st.dataframe(

data,

use_container_width=True,

hide_index=True

)
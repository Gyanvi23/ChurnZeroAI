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
"ChurnZero_dataset_v1.csv"
)

df = pd.read_csv(
csv_path
)
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
    df.index
    )

with right:

    c2 = st.selectbox(
    "Customer 2",
    df.index
    )
    row1 = df.iloc[c1]

    row2 = df.iloc[c2]
    data = pd.DataFrame({

    "Metric":[
    "Risk",
    "Income",
    "Balance",
    "Logins",
    "Status"
    ],

    f"C{c1}":[

    f"{int(row1['churn']*100)}%",

    f"₹{row1['annual_income']}",

    f"₹{row1['current_balance']}",

    row1["mobile_app_login_count"],

    "High Risk"
    if row1["churn"]==1
    else "Retained"

    ],

    f"C{c2}":[

    f"{int(row2['churn']*100)}%",

    f"₹{row2['annual_income']}",

    f"₹{row2['current_balance']}",

    row2["mobile_app_login_count"],

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
sat = pd.DataFrame({

"Customer":[
f"C{c1}",
f"C{c2}"
],

"Satisfaction":[

row1[
"satisfaction_score"
],

row2[
"satisfaction_score"
]

]

})

st.bar_chart(
sat.set_index(
"Customer"
)
)

st.dataframe(

data,

use_container_width=True,

hide_index=True

)
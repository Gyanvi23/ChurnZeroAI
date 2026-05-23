import streamlit as st
from styles import load_css


from layout import show_layout
import os
import pandas as pd
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

total = len(df)

high_risk = len(
df[df["churn"]==1]
)

retained = len(
df[df["churn"]==0]
)

risk_prob = high_risk/total

revenue = int(
df["annual_income"].sum()*0.05
)

retention = round(
(retained/total)*100
)
st.title(
"🧑‍💼 Manager Action Center"
)
a,b,c = st.columns(3)

a.metric(

"Risk",

f"{round(risk_prob*100)}%"

)

b.metric(

"Revenue Saved",

f"₹{revenue}"

)

c.metric(

"Retention",

f"{retention}%"

)

st.divider()

customer = st.selectbox(

"Customer",

df.index

)
selected = df.iloc[
customer
]
risk = (
0.9
if selected["churn"]==1
else 0.2
)
if risk > 0.8:

    actions = [

    "Assign RM",

    "Priority Contact"

    ]

elif risk > 0.5:

    actions = [

    "Cashback",

    "Email Campaign"

    ]

else:

    actions = [

    "No Action Needed"

    ]

action = st.selectbox(

"Retention Action",

actions

)

if st.button(
"🚀 Execute Action"
):

    st.success(

f"""

{action}

triggered for

{customer}

"""

    )

    st.toast(
    "AI action executed"
    )
st.divider()

st.subheader(
"AI Recommendation"
)



st.metric(
"Selected Risk",
f"{round(risk*100)}%"
)
if risk > 0.8:

    st.error(
    "Assign Relationship Manager immediately"
    )

elif risk > 0.5:

    st.warning(
    "Launch retention campaign"
    )

else:

    st.success(
    "Customer retained"
    )
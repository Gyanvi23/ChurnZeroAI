import streamlit as st
from styles import load_css


from layout import show_layout
import os
import pandas as pd
st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
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
"Bank Customer Churn Prediction.csv"
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

balance = int(
df["balance"].sum()
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

"Balance",

f"₹{balance}"

)

c.metric(

"Retention",

f"{retention}%"

)

st.divider()

customer = st.selectbox(

"Customer",

df["customer_id"]

)

if risk_prob > 0.8:

    actions = [

    "Assign RM",

    "Priority Contact"

    ]

elif risk_prob > 0.5:

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

selected = df[
df["customer_id"]==customer
].iloc[0]

if selected["churn"]==1:

    st.error(
    "Assign Relationship Manager immediately"
    )

else:

    st.success(
    "Customer retained"
    )
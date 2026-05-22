import streamlit as st
from styles import load_css

import joblib
import pandas as pd
import os
from layout import show_layout
st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
)
load_css()


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

model_path = os.path.join(

base,

"..",
"..",

"model",

"churn_model.pkl"

)

model = joblib.load(
model_path
)
show_layout()
st.subheader(
    "🔮 Predict Customer Churn"
)
customer_id = st.selectbox(

"Select Customer",

df["customer_id"]

)
row = df[
df["customer_id"]==customer_id
].iloc[0]
credit_score = st.number_input(

"Credit Score",

value=int(
row["credit_score"]
)

)

age = st.number_input(
"Age",
value=int(row["age"])
)

tenure = st.number_input(
"Tenure",
value=int(row["tenure"])
)

balance = st.number_input(
"Balance",
value=float(row["balance"])
)

products_number = st.number_input(
"Products",
value=int(
row["products_number"]
)
)

estimated_salary = st.number_input(
"Salary",
value=float(
row["estimated_salary"]
)
)
credit_card = st.selectbox(

"Credit Card",

[0,1],

index=int(
row["credit_card"]
)

)

active_member = st.selectbox(

"Active Member",

[0,1],

index=int(
row["active_member"]
)

)
# SAVE CUSTOMER IMMEDIATELY


if st.button(
    "🚀 Predict Churn"
):

    sample = pd.DataFrame({

        "credit_score":[credit_score],

        "country":[0],

        "gender":[0],

        "age":[age],

        "tenure":[tenure],

        "balance":[balance],

        "products_number":[products_number],

        "credit_card":[credit_card],

        "active_member":[active_member],

        "estimated_salary":[estimated_salary]

    })

    prediction = model.predict(
        sample
    )[0]

    prob = model.predict_proba(
        sample
    )[0][1]

    customer_data = {

    "name": str(customer_id),

    "age": int(age),

    "balance": float(balance),

    "salary": float(estimated_salary),

    "products": int(products_number),

    "tenure": int(tenure),

    "active_member": int(active_member),

    "risk_prob": float(prob),

    "prediction": int(prediction)

    }

    st.session_state["customer"] = customer_data

    import json
    import os

    json_path = os.path.join(
    base,
    "..",
    "..",
    "selected_customer.json"
    )

    with open(
    json_path,
    "w"
    ) as f:

        json.dump(
        customer_data,
        f,
        indent=4
        )
    st.session_state["customer_saved"]=True
    st.success(

    f"""
    Saved customer:

    {customer_id}

    Risk:

    {round(prob*100)}%
    """

    )
    

st.markdown(
"""
<div class="hero">

<h1>
🧠 Prediction Engine
</h1>

<h3>
AI Churn Detection
</h3>

</div>
""",

unsafe_allow_html=True
)

a,b,c = st.columns(3)

import os
import json

if "customer" in st.session_state:

    cust = st.session_state[
    "customer"
    ]

else:

    if os.path.exists(
    "selected_customer.json"
    ):

        with open(
        "selected_customer.json",
        "r"
        ) as f:

            cust = json.load(
            f
            )

    else:

        cust = {

        "name":"No Customer",

        "age":0,

        "balance":0,

        "salary":0,

        "risk_prob":0

        }
risk = cust.get(
"risk_prob",
0
)
a.metric(
"Confidence",
f"{round((1-risk)*100)}%"
)

b.metric(
"Risk",

"High"

if risk>0.7

else

"Low"
)

c.metric(
"Probability",

f"{round(risk,2)}"
)


st.markdown(

f"""

<div class="glass">

<h2>

{'⚠ High Risk' if risk>0.7 else '✅ Retained'}

</h2>

Probability :

{round(risk*100)}%

</div>
""",

unsafe_allow_html=True
)
st.divider()


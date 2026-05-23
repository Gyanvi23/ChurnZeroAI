import streamlit as st
from styles import load_css

import joblib
import pandas as pd
import os
from layout import show_layout
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
st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
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
customer_index = st.selectbox(
"Select Customer",
df.index
)

row = df.iloc[customer_index]
age = st.number_input(
"Age",
value=int(row["age"])
)

annual_income = st.number_input(
"Annual Income",
value=float(row["annual_income"])
)

tenure = st.number_input(
"Tenure Months",
value=int(row["tenure_months"])
)

products = st.number_input(
"Number Of Products",
value=int(row["number_of_products"])
)

balance = st.number_input(
"Current Balance",
value=float(row["current_balance"])
)

monthly_transaction_count = st.number_input(
"Monthly Transaction Count",
value=int(row["monthly_transaction_count"])
)

credit_card_spend = st.number_input(
"Credit Card Spend",
value=float(row["credit_card_spend"])
)

loan_outstanding = st.number_input(
"Loan Outstanding",
value=float(row["loan_outstanding_amount"])
)

mobile_logins = st.number_input(
"Mobile App Logins",
value=int(row["mobile_app_login_count"])
)

satisfaction = st.number_input(
"Satisfaction Score",
value=float(row["satisfaction_score"])
)
# SAVE CUSTOMER IMMEDIATELY


if st.button(
    "🚀 Predict Churn"
):

    sample = pd.DataFrame({

    "age":[age],

    "annual_income":[annual_income],

    "tenure_months":[tenure],

    "number_of_products":[products],

    "current_balance":[balance],

    "monthly_transaction_count":[monthly_transaction_count],

    "credit_card_spend":[credit_card_spend],

    "loan_outstanding_amount":[loan_outstanding],

    "mobile_app_login_count":[mobile_logins],

    "satisfaction_score":[satisfaction]

    })
    
    prediction = model.predict(
        sample
    )[0]

    prob = model.predict_proba(
        sample
    )[0][1]

    customer_data = {

    "name":str(customer_index),

    "age":int(age),

    "income":float(
    annual_income
    ),

    "balance":float(
    balance
    ),

    "products":int(
    products
    ),

    "risk_prob":float(prob),

    "prediction":int(prediction)

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

    {customer_index}

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

    "income":0,

    "logins":0,

    "complaints":0,

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


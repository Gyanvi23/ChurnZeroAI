import streamlit as st
import time
from styles import load_css


from layout import show_layout
import os
import pandas as pd

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

st.title(
"🔔 Live Alert Feed"
)
high_risk = df[
df["churn"]==1
]

low_balance = df[
df["balance"]<50000
]

retained = df[
df["churn"]==0
]

alerts = []

alerts.append(
f"""
🔴 High Risk Customers

{len(high_risk)}
customers
"""
)

alerts.append(
f"""
🟡 Low Balance Customers

{len(low_balance)}
customers
"""
)

alerts.append(
f"""
🟢 Retained Customers

{len(retained)}
customers
"""
)

if len(alerts)==0:

    alerts.append(

"""
🟢 No active alerts
"""
    )

box = st.empty()

for i in alerts:

    box.warning(
    i
    )

    time.sleep(
    1
    )

st.divider()

st.subheader(
"AI Recommendation"
)

if len(high_risk)>50:

    st.error(
"""
Large churn segment detected

Launch retention immediately
"""
)

elif len(high_risk)>20:

    st.warning(
"""
Medium churn risk segment

Start campaign
"""
)

else:

    st.success(
"""
Customer base stable
"""
)
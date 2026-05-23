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

st.title(
"🔔 Live Alert Feed"
)
high_risk = df[
df["churn"]==1
]

low_engagement = df[
df["mobile_app_login_count"]<10
]

retained = df[
df["churn"]==0
]

alerts = []
import json

selected_risk = 0

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

        selected_risk = cust.get(
        "risk_prob",
        0
        )

alerts.append(
f"""
🎯 Selected Customer Risk

{round(selected_risk*100)}%
"""
)

alerts.append(
f"""
🔴 High Risk Customers

{len(high_risk)}
customers
"""
)

alerts.append(
f"""
🟡 Low Engagement Customers

{len(low_engagement)}
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

if selected_risk > 0.7:

    st.error(
"""
High risk customer detected

Assign relationship manager
"""
)

elif selected_risk > 0.4:
    st.warning(
"""
Moderate customer risk

Launch retention campaign
"""
)

else:

    st.success(
"""
Customer base stable
"""
)
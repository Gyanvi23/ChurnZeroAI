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

retention = round(
(retained/total)*100
)

revenue = int(
df["annual_income"].sum()*0.05
)

name = f"{total} Customers"

st.markdown(
"""
<div class="hero">

<h1>
🎯 Retention Center
</h1>

<h3>
AI Powered Customer Recovery System
</h3>

</div>
""",

unsafe_allow_html=True
)

# KPI ROW

a,b,c,d = st.columns(4)

a.metric(

"Retention %",

f"{retention}%"

)

b.metric(
"Recovered",
retained
)

c.metric(
"Campaigns",
high_risk
)

d.metric(
"Selected Risk",
f"{round(selected_risk*100)}%"
)

# RETENTION ACTIONS

st.subheader(
"Retention Actions"
)

c1,c2,c3 = st.columns(3)

with c1:

    st.success(

f"""
💎 VIP Customer

Customer :

{name}

Revenue Saved :

₹{revenue}
Premium Retention

"""

)

with c2:

    st.warning(

f"""
😴 Silent Customer

Risk :

{round(selected_risk*100)}%
Cashback

Email Campaign

"""

)

with c3:

    st.error(

f"""
🚨 High Risk

Probability :

{round(selected_risk*100)}%s

Assign RM

Priority Recovery

"""

)

st.divider()

# TIMELINE

st.subheader(
"Retention Roadmap"
)

st.info(

f"""
Customers →

{total}

Revenue Saved →

₹{revenue}

Selected Risk →

{round(selected_risk*100)}%
Risk →

{round(risk_prob*100)}%

Retention →

{retention}%
"""

)
st.subheader(
"AI Recommendation"
)

if selected_risk > 0.7:

    st.error(
    "Assign Relationship Managers"
    )

elif selected_risk > 0.4:
    st.warning(
    "Launch Cashback Campaign"
    )

else:

    st.success(
    "Customers retained"
    )
# EXPORT

report = f"""

Customer :

{name}

Revenue Saved :

₹{revenue}

Risk :

{round(selected_risk*100)}%

Retention :

{retention}%

"""

st.download_button(

"📄 Export Retention Report",

report,

file_name=
"retention_report.txt"

)
st.divider()

st.caption(
"Built with ❤️ by Team ChurnZero AI"
)
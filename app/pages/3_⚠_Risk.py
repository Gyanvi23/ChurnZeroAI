import streamlit as st
from styles import load_css

import os
import pandas as pd
from layout import show_layout
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

        cust = json.load(f)

        selected_risk = cust.get(
        "risk_prob",
        0
        )

st.metric(
"Selected Customer Risk",
f"{round(selected_risk*100)}%"
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

risk_prob = high_risk / total

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
⚠ Risk Intelligence Center
</h1>

<h3>
AI Customer Risk Monitoring
</h3>

</div>
""",

unsafe_allow_html=True
)

# KPI ROW

a,b,c,d = st.columns(4)

a.metric(

"Risk Score",

f"{round(risk_prob*100)}%"

)

b.metric(
"High Risk",
high_risk
)

c.metric(
"Retained",
retained
)

d.metric(
"Total Customers",
total
)
st.divider()
if selected_risk > 0.7:

    st.error(
    "⚠ Selected customer is high risk"
    )

else:

    st.success(
    "✅ Selected customer retained"
    )
# CUSTOMER SEGMENTS

st.subheader(
"Customer Segments"
)

c1,c2,c3 = st.columns(3)

with c1:

    st.success(

f"""
💎 VIP

Customers :

{retained}

Revenue Saved :

₹{revenue}
Low Churn Risk
"""

)

with c2:

    st.warning(

f"""
😴 Silent

Risk :

{round(risk_prob*100)}%

Needs Re-engagement

Moderate Risk

"""

)

with c3:

    st.error(

f"""
🚨 High Risk

Customers :

{high_risk}

Immediate Action

Assign RM

"""

)

st.divider()

# RISK TIMELINE

st.subheader(
"Risk Monitoring Roadmap"
)

st.info(

f"""
Total Customers →

{total}

Revenue Saved →

₹{revenue}

High Risk Customers →

{high_risk}

Retention →

{retention}%

Average Age →

{round(df['age'].mean())}

Digital Logins →

{round(df['mobile_app_login_count'].mean())}

"""

)

# ALERTS

st.subheader(
"Risk Alerts"
)

if risk_prob > 0.5:

    st.error(

f"""
🚨 Portfolio Risk High

Customers At Risk :

{high_risk}

Risk :

{round(risk_prob*100)}%

"""

)

else:

    st.success(

f"""
✅ Portfolio Stable

Retention :

{retention}%

"""

)

# EXPORT

report = f"""

Customer :

{name}

Risk :

{round(risk_prob*100)}%

Revenue Saved :

₹{revenue}

Retention :

{retention}%

"""

st.download_button(

"📄 Export Risk Report",

report,

file_name=
"risk_report.txt"

)

st.divider()

st.caption(
"Built with ❤️ by Team ChurnZero AI"
)
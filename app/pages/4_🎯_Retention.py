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

retention = round(
(retained/total)*100
)

balance = int(
df["balance"].sum()
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
"High Risk",
high_risk
)
st.divider()

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

Balance :

₹{balance}

Premium Retention

"""

)

with c2:

    st.warning(

f"""
😴 Silent Customer

Risk :

{round(risk_prob*100)}%

Cashback

Email Campaign

"""

)

with c3:

    st.error(

f"""
🚨 High Risk

Probability :

{round(risk_prob*100)}%

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

Total Balance →

₹{balance}

High Risk →

{high_risk}

Risk →

{round(risk_prob*100)}%

Retention →

{retention}%
"""

)
st.subheader(
"AI Recommendation"
)

if high_risk > total*0.5:

    st.error(
    "Assign Relationship Managers"
    )

elif high_risk > total*0.2:

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

Risk :

{round(risk_prob*100)}%

Balance :

₹{balance}

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
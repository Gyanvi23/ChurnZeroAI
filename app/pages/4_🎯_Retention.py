import streamlit as st
from styles import load_css

load_css()

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
"82%"
)

b.metric(
"Recovered",
"210"
)

c.metric(
"Campaigns",
"12"
)

d.metric(
"High Risk",
"90"
)

st.divider()

# RETENTION ACTIONS

st.subheader(
"Retention Actions"
)

c1,c2,c3 = st.columns(3)

with c1:

    st.success(
"""
💎 VIP Customers

• Loyalty Program

• Premium Offers

• Retention Campaign
"""
)

with c2:

    st.warning(
"""
😴 Silent Customers

• Cashback

• Re-engagement

• Email Campaign
"""
)

with c3:

    st.error(
"""
🚨 High Risk

• Relationship Manager

• Immediate Contact

• Priority Recovery
"""
)

st.divider()

# TIMELINE

st.subheader(
"Retention Roadmap"
)

st.info(
"""
Q1 → Detection

Q2 → Segmentation

Q3 → Retention

Q4 → Growth
"""
)

# EXPORT

st.download_button(

"📄 Export Retention Report",

"Retention Strategy Report",

file_name=
"retention_report.txt"
)

st.divider()

st.caption(
"Built with ❤️ by Team ChurnZero AI"
)
import streamlit as st
from styles import load_css

load_css()

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
"82%"
)

b.metric(
"High Risk",
"90"
)

c.metric(
"Silent",
"180"
)

d.metric(
"VIP",
"320"
)

st.divider()

# CUSTOMER SEGMENTS

st.subheader(
"Customer Segments"
)

c1,c2,c3 = st.columns(3)

with c1:

    st.success(
"""
💎 VIP

• High Value

• Premium Customers

• Low Churn Risk
"""
)

with c2:

    st.warning(
"""
😴 Silent

• Low Activity

• Needs Re-engagement

• Moderate Risk
"""
)

with c3:

    st.error(
"""
🚨 High Risk

• Churn Indicators

• Immediate Action

• Priority Customer
"""
)

st.divider()

# RISK TIMELINE

st.subheader(
"Risk Monitoring Roadmap"
)

st.info(
"""
Q1 → Detection

Q2 → Analysis

Q3 → Prevention

Q4 → Retention
"""
)

# ALERTS

st.subheader(
"Risk Alerts"
)

st.error(
"🚨 High Risk customers increased by 12%"
)

st.warning(
"⚠ Silent customer activity decreased"
)

st.success(
"✅ VIP retention stable"
)

# EXPORT

st.download_button(

"📄 Export Risk Report",

"Risk Analysis Report",

file_name=
"risk_report.txt"
)

st.divider()

st.caption(
"Built with ❤️ by Team ChurnZero AI"
)
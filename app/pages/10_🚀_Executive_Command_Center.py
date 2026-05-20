import streamlit as st
import pandas as pd
import plotly.express as px
from styles import load_css
from pdf_export import create_executive_pdf
load_css()

st.markdown(
"""
<div class="hero">

<h1>
🚀 Executive Command Center
</h1>

<h3>
Banking Customer Intelligence Platform
</h3>

</div>
""",

unsafe_allow_html=True
)

# TOP KPIs

a,b,c,d = st.columns(4)

a.metric(
"Customers",
"12,540",
"+8%"
)

b.metric(
"Churn %",
"18%",
"-4%"
)

c.metric(
"Revenue Saved",
"$2.4M",
"+12%"
)

d.metric(
"Live Alerts",
"32",
"+5"
)
st.divider()

# ALERTS + SEARCH

left,right = st.columns(2)

with left:

    st.subheader(
    "🔔 Live Alerts"
    )

    st.error(
    "High Risk +12%"
    )

    st.warning(
    "Silent customers rising"
    )

    st.success(
    "VIP stable"
    )

with right:

    st.subheader(
    "🔍 Customer Search"
    )

    cid = st.text_input(
    "Customer ID"
    )

    if cid:

        st.info(
        f"""
Customer : {cid}

Risk : High

Probability : 82%

Action :

Assign RM
"""
        )

st.divider()

# DASHBOARD

data = pd.DataFrame({

"Segment":[

"VIP",

"Silent",

"High Risk"

],

"Count":[

320,

180,

90

]

})

c1,c2 = st.columns(2)

with c1:

    fig = px.bar(

    data,

    x="Segment",

    y="Count",

    title="Customer Segments"
    )
    fig.update_layout(

    paper_bgcolor=
    "rgba(0,0,0,0)",

    plot_bgcolor=
    "rgba(0,0,0,0)",

    font_color=
    "white"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )
    st.divider()

st.subheader(
"🚨 Top Risk Customers"
)

risk = pd.DataFrame({

"Customer":[

"CUST1001",

"CUST1002",

"CUST1003",

"CUST1004"

],

"Probability":[

"92%",

"87%",

"82%",

"79%"

],

"Action":[

"Assign RM",

"Cashback",

"Priority Contact",

"Retention"

]

})

st.dataframe(

risk,

use_container_width=True
)
st.divider()

st.subheader(
"🧑‍💼 Manager Performance"
)

m1,m2,m3 = st.columns(3)

m1.metric(
"Actions",
"120"
)

m2.metric(
"Recovered",
"78"
)

m3.metric(
"Success Rate",
"82%"
)

with c2:

    pie = px.pie(

    data,

    names="Segment",

    values="Count"
    )
    pie.update_layout(

    paper_bgcolor=
    "rgba(0,0,0,0)",

    font_color=
    "white"
    )

    st.plotly_chart(
    pie,
    use_container_width=True
    )

st.divider()

st.subheader(
"Customer Timeline"
)

events = [

"2023 → Account Created",

"2024 → Active Customer",

"2025 → Activity Reduced",

"2025 → High Risk",

"2025 → Retention Triggered"

]

for e in events:

    st.markdown(
    f"✅ {e}"
    )
st.divider()

st.subheader(
"💰 Business Impact"
)

c1,c2,c3 = st.columns(3)

c1.success(
"""
Revenue Saved

$2.4M
"""
)

c2.warning(
"""
Retention Improved

+18%
"""
)

c3.info(
"""
Customers Retained

320
"""
)

create_executive_pdf()

with open(

"executive_report.pdf",

"rb"

) as file:

    st.download_button(

    "📄 Export Executive Report",

    file,

    file_name=
    "executive_report.pdf"
    )

st.caption(
"Built by Team ChurnZero AI"
)
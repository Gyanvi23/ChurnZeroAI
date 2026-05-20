import streamlit as st
from styles import load_css
from pdf_export import create_pdf

load_css()

st.markdown(
"""
<div class="hero">

<h1>
👤 Customer Profile
</h1>

<h3>
Customer Intelligence View
</h3>

</div>
""",

unsafe_allow_html=True
)

left,right = st.columns([1,2])

with left:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=180
    )

with right:

    st.metric(
        "Customer ID",
        "CUST1001"
    )

    st.metric(
        "Segment",
        "High Risk"
    )

    st.metric(
        "Churn Probability",
        "82%"
    )

st.divider()

st.subheader(
"Customer Summary"
)

st.info(
"""
Name : Rahul Sharma

Account Age : 3 Years

Balance : ₹1,50,000

Transactions : 20

Status : High Risk
"""
)

st.divider()

st.subheader(
"Recommended Action"
)

st.error(
"""
Assign Relationship Manager

Priority Contact Required
"""
)
st.divider()

st.subheader(
"Customer Journey Timeline"
)

timeline = [

"2023 → Account Created",

"2024 → High Transactions",

"Jan 2025 → Activity Reduced",

"Mar 2025 → Silent Behaviour",

"May 2025 → High Churn Risk"

]

for event in timeline:

    st.markdown(
    f"✅ {event}"
    )

create_pdf(

"CUST1001",

"High Risk",

"82%",

150000,

20,

"Assign Relationship Manager"

)

with open(

"customer_report.pdf",

"rb"

) as file:

    st.download_button(

    "📄 Download PDF Report",

    file,

    file_name=
    "customer_report.pdf"
    )
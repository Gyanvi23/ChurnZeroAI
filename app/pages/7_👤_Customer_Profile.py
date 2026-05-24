import streamlit as st
from styles import load_css
from pdf_export import create_pdf
import os

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

import json
import os

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

    st.warning(
    "Please predict customer first"
    )

    st.stop()

risk = float(

cust.get(
"risk_prob",
0
)

)


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

    cust.get(
    "name",
    "CUST"
    )
    )

    st.metric(

    "Prediction",

    "Churn"
    if cust.get(
    "prediction",
    0
    )==1
    else
    "Retained"
    )

    st.metric(

    "Churn Probability",

    f"{round(risk*100)}%"
    )

st.divider()

st.subheader(
"Customer Summary"
)

st.info(

f"""

Customer :

{cust.get(
"name",
"CUST1001"
)}

Age :

{cust.get(
'age',
0
)}

Income :

₹{cust.get(
'income',
0
)}

Digital Logins :

{cust.get(
'total_digital_logins',
cust.get(
'mobile_app_login_count',
0
)
)}

Complaints :

{cust.get(
'total_complaints',
0
)}

Prediction :

{'Churn' if cust.get(
'prediction',
0
)==1 else 'Retained'}
Status :

{'High Risk' if risk>0.7 else 'Retained'}

"""

)
st.divider()

st.subheader(
"Recommended Action"
)

if risk>0.8:

    action="Assign Relationship Manager"

elif risk>0.5:

    action="Offer Cashback"

else:

    action="No Action Needed"

st.error(

f"""

{action}

Risk :

{round(risk*100)}%

"""
)
st.divider()

st.subheader(
"Customer Journey Timeline"
)

timeline = [

"2023 → Customer Onboarded",

f"Income → ₹{cust.get('income',0)}",

f"Digital Logins → {cust.get('total_digital_logins', cust.get('mobile_app_login_count',0))}",

f"Complaints → {cust.get('total_complaints',0)}",

f"Risk → {round(risk*100)}%"

]

for event in timeline:

    st.markdown(
    f"✅ {event}"
    )

create_pdf(

cust.get(
"name",
"CUST1001"
),

"High Risk"
if risk>0.7
else
"Retained",

f"{round(risk*100)}%",

cust.get(
"income",
0
),

cust.get(
"total_digital_logins",
cust.get(
"mobile_app_login_count",
0
)
),
action

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
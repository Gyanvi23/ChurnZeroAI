import streamlit as st
from styles import load_css
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
cust = st.session_state.get(
"customer",
{
"name":"No Customer Selected",
"age":0,
"income":0,
"logins":0,
"complaints":0,
"risk_prob":0
}
)

risk_prob = cust.get(
"risk_prob",
0
)

income = cust.get(
"income",
0
)

logins = cust.get(
"logins",
0
)

complaints = cust.get(
"complaints",
0
)

name = cust.get(
"name",
"CUST1001"
)

retention = round(
(1-risk_prob)*100
)

st.title(
"🗺 Customer Journey"
)

timeline = [

f"🆔 Customer → {name}",

f"🎂 Age → {cust.get('age',0)}",

f"💰 Annual Income → ₹{income}",

f"📱 Digital Logins → {logins}",

f"📞 Complaints → {complaints}",

f"⚠ Risk → {round(risk_prob*100)}%"

]

for t in timeline:

    st.info(
        t
    )
st.divider()

st.subheader(
"Journey Status"
)

if risk_prob > 0.8:

    st.error(
"""
🚨 High Churn Risk

Customer entering danger zone

Assign RM immediately
"""
    )

elif risk_prob > 0.5:

    st.warning(
"""
⚠ Moderate Risk

Retention campaign required
"""
    )

else:

    st.success(
"""
✅ Healthy Customer Journey

Customer retained
"""
    )
st.progress(
retention/100
)
st.metric(
"Journey Health",
f"{retention}%"
)

st.caption(
f"Retention Score : {retention}%"
)
report = f"""

Customer : {name}

Age : {cust.get('age',0)}

Tenure : {cust.get('tenure',0)}

Income : ₹{income}

Digital Logins : {logins}

Complaints : {complaints}

Risk : {round(risk_prob*100)}%

Retention : {retention}%

"""

st.download_button(

"📄 Export Journey Report",

report,

file_name=
"journey_report.txt"

)
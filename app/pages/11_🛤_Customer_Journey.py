import streamlit as st
from styles import load_css


from layout import show_layout
st.set_page_config(
layout="wide",
initial_sidebar_state="collapsed"
)
load_css()
show_layout()
cust = st.session_state.get(
"customer",
{
"name":"No Customer Selected",
"age":0,
"balance":0,
"salary":0,
"risk_prob":0
}
)

risk_prob = cust.get(
"risk_prob",
0
)

balance = cust.get(
"balance",
0
)

salary = cust.get(
"salary",
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

f"📈 Tenure → {cust.get('tenure',0)} years",

f"💰 Balance → ₹{balance}",

f"🛒 Products → {cust.get('products',0)}",

f"💵 Salary → ₹{salary}",

f"👤 Active Member → {cust.get('active_member',0)}",

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

st.caption(
f"Retention Score : {retention}%"
)
report = f"""

Customer : {name}

Age : {cust.get('age',0)}

Tenure : {cust.get('tenure',0)}

Balance : ₹{balance}

Products : {cust.get('products',0)}

Salary : ₹{salary}

Risk : {round(risk_prob*100)}%

Retention : {retention}%

"""

st.download_button(

"📄 Export Journey Report",

report,

file_name=
"journey_report.txt"

)
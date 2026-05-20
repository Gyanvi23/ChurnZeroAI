import streamlit as st
import time
from styles import load_css

load_css()

st.title(
"🔔 Live Alert Feed"
)

alerts = [

"🔴 CUST1001 → churn probability 92%",

"🟡 CUST1002 → activity dropped 40%",

"🟢 CUST1003 → retained successfully",

"🔴 CUST1004 → transaction decline",

"🟡 CUST1005 → silent behaviour"
]

box = st.empty()

for i in alerts:

    box.warning(
        i
    )

    time.sleep(
        1
    )
import streamlit as st
from styles import load_css

load_css()

st.title(
"🗺 Customer Journey"
)

timeline = [

"✅ 2023 → Account Created",

"🚀 2024 → High Activity",

"⚠ Jan 2025 → Activity Reduced",

"😴 Mar 2025 → Silent Behaviour",

"🚨 May 2025 → High Churn Risk"

]

for t in timeline:

    st.info(
        t
    )
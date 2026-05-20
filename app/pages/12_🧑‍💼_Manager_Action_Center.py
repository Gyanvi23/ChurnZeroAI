import streamlit as st
from styles import load_css

load_css()

st.title(
"🧑‍💼 Manager Action Center"
)

customer = st.selectbox(

"Customer",

[
"CUST1001",
"CUST1002"
]

)

action = st.selectbox(

"Retention Action",

[
"Assign RM",

"Cashback",

"Email Campaign"
]

)

if st.button(
"🚀 Execute Action"
):

    st.success(
    f"{action} triggered for {customer}"
    )
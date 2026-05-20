import streamlit as st
import pandas as pd
from styles import load_css

load_css()

st.markdown(
"""
<div class="hero">

<h1>
⚖ Customer Comparison
</h1>

</div>
""",

unsafe_allow_html=True
)

left,right = st.columns(2)

with left:

    c1 = st.selectbox(

    "Customer 1",

    [

    "CUST1001",

    "CUST1002",

    "CUST1003"

    ]
    )

with right:

    c2 = st.selectbox(

    "Customer 2",

    [

    "CUST1001",

    "CUST1002",

    "CUST1003"

    ]
    )

data = pd.DataFrame({

"Metric":[

"Risk",

"Balance",

"Transactions"

],

c1:[

"82%",

"150000",

"20"

],

c2:[

"30%",

"300000",

"45"

]

})

st.subheader(
"Comparison Results"
)

st.dataframe(

data,

use_container_width=True,

hide_index=True

)
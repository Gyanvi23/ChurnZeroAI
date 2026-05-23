import streamlit as st
import plotly.express as px
import pandas as pd
import os

from styles import load_css


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
base = os.path.dirname(
os.path.abspath(__file__)
)

csv_path = os.path.join(
base,
"..",
"..",
"data",
"ChurnZero_dataset_v1.csv"
)
import json

selected_risk = 0

json_path = os.path.join(
base,
"..",
"..",
"selected_customer.json"
)

if os.path.exists(
json_path
):

    with open(
    json_path,
    "r"
    ) as f:

        cust = json.load(
        f
        )

        selected_risk = cust.get(
        "risk_prob",
        0
        )

df_data = pd.read_csv(
csv_path
)
st.title(
"💰 Business Impact"
)

a,b,c,d = st.columns(4)

saved = int(
df_data["annual_income"].sum()*0.05
)

retained = len(
df_data[
df_data["churn"]==0
]
)

retention = round(
(retained/len(df_data))*100
)
high_risk = len(
df_data[
df_data["churn"]==1
]
)

risk = round(
(high_risk/len(df_data))*100
)
customers = retained
a.metric(
"Revenue Saved",

f"₹{saved}"
)

b.metric(
"Retention Improved",

f"+{retention}%"
)

c.metric(
"Customers Retained",

customers
)
d.metric(
"Selected Risk",
f"{round(selected_risk*100)}%"
)

st.divider()
st.subheader(
"📈 AI Business Insight"
)

if selected_risk > 0.7:

    st.error(

f"""

Revenue at risk:

₹{saved}

Selected customer requires retention action.

"""

    )

else:

    st.success(

"""

Customer retention stable.

Revenue protected.

"""

    )
chart_df = pd.DataFrame({

"Metric":[

"Retained Customers",

"High Risk Customers"

],

"Count":[

retained,

high_risk

]

})

fig = px.pie(

chart_df,

values="Count",

names="Metric",

hole=0.45

)

fig.update_traces(

textposition="inside",

textinfo="percent+label"

)
dark = st.session_state.get(
"dark_mode",
True
)

chart_text = (
"white"
if dark
else "black"
)

fig.update_layout(

paper_bgcolor=
"rgba(0,0,0,0)",

plot_bgcolor=
"rgba(0,0,0,0)",

font_color=
chart_text,

legend_font_color=
chart_text

)

fig.update_traces(

textfont_color=
chart_text

)

st.plotly_chart(
fig,
use_container_width=True
)
gauge_df = pd.DataFrame({

"Metric":[

"Retention",

"Risk"

],

"Value":[

retention,

risk

]

})

gauge = px.bar(

gauge_df,

x="Metric",

y="Value",

text="Value"

)

gauge.update_layout(

paper_bgcolor=
"rgba(0,0,0,0)",

plot_bgcolor=
"rgba(0,0,0,0)",

font_color=
chart_text,

title=
"Retention Score"

)

st.plotly_chart(

gauge,

use_container_width=True
)
report = f"""

Revenue Saved:

₹{saved}

Retention:

{retention}%

Risk:

{round(selected_risk*100)}%

"""
impact = df_data[[

"mobile_app_login_count",

"monthly_transaction_count",

"satisfaction_score",

"annual_income",

"churn"

]].corr()["churn"].abs()

st.bar_chart(
impact.drop(
"churn"
)
)
st.download_button(

"📄 Export Business Report",

report,

file_name=
"business_report.txt"

)
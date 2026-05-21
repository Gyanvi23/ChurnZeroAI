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
"Bank Customer Churn Prediction.csv"
)

df_data = pd.read_csv(
csv_path
)
st.title(
"💰 Business Impact"
)

a,b,c = st.columns(3)

saved = int(
df_data["balance"].sum()*0.2
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

st.divider()
st.subheader(
"📈 AI Business Insight"
)

if risk>70:

    st.error(

f"""

Revenue at risk:

₹{saved}

Immediate retention action required.

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

{risk}%

"""

st.download_button(

"📄 Export Business Report",

report,

file_name=
"business_report.txt"

)
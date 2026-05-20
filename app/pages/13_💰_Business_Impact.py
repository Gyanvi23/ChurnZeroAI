import streamlit as st
import plotly.express as px
import pandas as pd

from styles import load_css

load_css()

st.title(
"💰 Business Impact"
)

a,b,c = st.columns(3)

a.metric(
"Revenue Saved",
"$2.4M"
)

b.metric(
"Retention Improved",
"+18%"
)

c.metric(
"Customers Retained",
"320"
)

st.divider()

df = pd.DataFrame({

"Metric":[

"Revenue",

"Retention",

"Saved Customers"

],

"Value":[

2.4,

18,

320

]

})

dark = st.session_state.get(
"dark_mode",
True
)

chart_text = (
"white"
if dark
else "black"
)

fig = px.pie(

df,

values=
"Value",

names=
"Metric"

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
import streamlit as st
import pandas as pd
import plotly.express as px
from styles import load_css

load_css()


st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title(
    "📊 Analytics Dashboard"
)

st.caption(
    "Customer Insights"
)

st.divider()

data = pd.DataFrame({

    "Category":[
        "VIP",
        "Silent",
        "High Risk"
    ],

    "Count":[
        320,
        180,
        90
    ]
})

left,right = st.columns(2)

with left:

    fig = px.bar(

        data,

        x="Category",

        y="Count",

        title="Customer Segments"
    )
    fig.update_layout(

    paper_bgcolor=
    "#111827",

    plot_bgcolor=
    "#111827",

    font_color=
    "white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    pie = px.pie(

        data,

        names="Category",

        values="Count",

        title="Distribution"
    )
    pie.update_layout(

    paper_bgcolor=
    "#111827",

    font_color=
    "white"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

k1,k2,k3 = st.columns(3)

k1.metric(
    "Total Customers",
    "590"
)

k2.metric(
    "Retention",
    "82%"
)

k3.metric(
    "Churn Risk",
    "18%"
)
st.subheader(
"Business Impact"
)

a,b,c = st.columns(3)

a.success(
"Revenue Saved\n\n$2.4M"
)

b.warning(
"Risk Reduced\n\n18%"
)

c.info(
"Recovered\n\n210"
)
import pandas as pd
import plotly.express as px

heat = pd.DataFrame({

"VIP":[5,7,8],

"Silent":[2,4,5],

"High Risk":[9,8,7]

})

fig = px.imshow(

heat,

title=
"Risk Heatmap"
)

st.plotly_chart(
fig
)
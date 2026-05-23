import streamlit as st
import streamlit.components.v1 as components
import os
import json
def show_ai_bot():
    

    base = os.path.dirname(
    os.path.abspath(__file__)
    )

    json_path = os.path.join(
    base,
    "..",
    "selected_customer.json"
    )

    if "customer" in st.session_state:

        cust = st.session_state[
        "customer"
        ]

    elif os.path.exists(
    json_path
    ):

        with open(
        json_path,
        "r"
        ) as f:

            cust = json.load(
            f
            )

    else:

        cust = {

        "name":"No Customer",

        "income":0,

        "logins":0,

        "complaints":0,

        "risk_prob":0

        }

    risk = cust.get(
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
    "CUST"
    )

    html_code = """
    

<style>
iframe {
    pointer-events: none !important;
}

.bot-btn{

position:fixed;
bottom:25px;
right:25px;
pointer-events:auto !important;
width:70px;
height:70px;

border:none;
border-radius:50%;

font-size:30px;

cursor:pointer;

background:linear-gradient(
135deg,
#00E5FF,
#FF3EF5
);

box-shadow:
0 0 30px rgba(255,0,255,.5);

z-index:1000;

}

.chat-window{

position:fixed;

bottom:50px;
right:40px;

max-width:300px;
width:90vw;
height:540px;
position:fixed !important;

pointer-events:auto !important;

display:none;
flex-direction:column;


background:
linear-gradient(
180deg,
#07112E,
#020816
);

border-radius:28px;

overflow:hidden;

z-index:1000;
pointer-events:auto;
border:
1px solid rgba(
255,
255,
255,
0.08
);

box-shadow:
0 0 35px rgba(
255,
0,
255,
0.18
);

}


.chat-header{

height:65px;

display:flex;

justify-content:center;

align-items:center;

font-size:22px;

font-weight:700;

color:white;

background:

linear-gradient(
90deg,
#00D9FF,
#7C83FF,
#FF3EF5
);

border-radius:

28px 28px 0 0;

flex-shrink:0;

z-index:50;

}
.chat-body{

flex:1;

overflow-y:auto;
overflow-x:hidden;

padding:14px;

display:flex;
flex-direction:column;

gap:12px;

scroll-behavior:smooth;

min-height:0;

}
.chat-body::-webkit-scrollbar-thumb{

background:#4E7CFF;

border-radius:20px;

}
.chat-body::-webkit-scrollbar{

width:6px;

}
.suggest{

height:44px;

border-radius:14px;

font-size:13px;

font-weight:700;

display:flex;

justify-content:center;
align-items:center;

text-align:center;

padding:6px;

background:
linear-gradient(
135deg,
#0CCFFF,
#3478FF
);

cursor:pointer;

transition:.25s;

overflow:hidden;

}
.suggest:hover{

transform:
translateY(-3px);

box-shadow:

0 0 18px rgba(
0,
200,
255,
0.4
);

}

.suggest-grid{

display:grid;

grid-template-columns:repeat(2,1fr);

gap:8px;

width:100%;

}
.message{

padding:12px;

border-radius:16px;

background:

linear-gradient(
135deg,

rgba(
40,
70,
120,
0.92
),

rgba(
30,
50,
90,
0.92
)

);

color:white;

font-size:13px;

line-height:1.5;

border:

1px solid rgba(
255,
255,
255,
0.05
);

box-shadow:

0 4px 10px rgba(
0,
0,
0,
0.18
);

width:100%;

max-width:100%;

box-sizing:border-box;

word-wrap:break-word;

overflow-wrap:break-word;

white-space:normal;

flex-shrink:0;

animation:fade .25s ease;

}

@keyframes fade{

from{

opacity:0;

transform:
translateY(8px);

}

to{

opacity:1;

transform:none;

}

}
.chat-footer{

padding:12px;

background:
linear-gradient(
180deg,
rgba(5,10,35,0),
#08132F
);

border-top:
1px solid rgba(
255,
255,
255,
0.08
);

display:flex;
flex-direction:column;

gap:10px;

flex-shrink:0;

}
.chat-input{

flex:1;

padding:13px;

border:none;

outline:none;

border-radius:12px;

background:#1E293B;

color:white;

}

.send-btn{

width:70px;

height:42px;

font-size:13px;

font-weight:700;

border:none;

border-radius:12px;

background:

linear-gradient(
90deg,
#00E5FF,
#FF3EF5
);

box-shadow:
0 0 14px rgba(
255,
0,
255,
0.25
);

}
@media(max-width:480px){

.chat-window{

width:92vw;
right:4vw;
height:78vh;

}
}
.navbar{
    z-index:2001 !important;
    position:relative;
}
}

</style>


<button
class="bot-btn"
onclick="toggleChat()">

🤖

</button>


<div
class="chat-window"
id="chat">

<div class="chat-header">

🤖 Churn AI Assistant

</div>

<div
class="chat-body"
id="body">

<div class="message">

👋 Hi, I am Churn AI Assistant. Ask about risk, retention, customer or revenue.

</div>

</div>

<div class="chat-footer">
<hr style="
border:none;
height:1px;
background:rgba(255,255,255,.08);
margin:0 0 8px 0;
">

<div class="suggest-grid">

<div
class="suggest"
onclick="addMsg('Show high risk customers')">

⚠ Risk

</div>

<div
class="suggest"
onclick="addMsg('Retention strategy')">

🎯 Retention

</div>

<div
class="suggest"
onclick="addMsg('Customer profile')">

👤 Customer

</div>

<div
class="suggest"
onclick="addMsg('Revenue insights')">

💰 Revenue

</div>

</div>

<div
style="
display:flex;
gap:8px;
align-items:center;
">

<input
id="msg"
class="chat-input"
placeholder="Ask something...">

<button
class="send-btn"
onclick="sendMsg()">

Send

</button>

</div>

</div>

</div>


<script>

function toggleChat(){

let c=
document.getElementById(
"chat"
);

if(
c.style.display==="flex"
){

c.style.display="none";

}

else{

c.style.display="flex";

setTimeout(()=>{

document.getElementById(
"body"
).scrollTop=

document.getElementById(
"body"
).scrollHeight;

},100);

}

}
function addMsg(text){

let body=
document.getElementById(
"body"
);

let ans=text;

if(text.includes("risk")){

ans=
"⚠ Current churn risk: RISK_PLACEHOLDER. Suggested action: Monitor customer.";

}

else if(text.includes("Retention")){

ans=
"🎯 Retention score: RETENTION_PLACEHOLDER%. Offer rewards and loyalty plans.";

}

else if(text.includes("Customer")){

ans=
"👤 Customer: CUSTOMER_PLACEHOLDER | Income: ₹INCOME_PLACEHOLDER";

}

else if(text.includes("Revenue")){

ans=
"💰 Revenue insight based on customer income: ₹REVENUE_PLACEHOLDER";

}

body.insertAdjacentHTML(

"beforeend",

"<div class='message'>"+ans+"</div>"

);

setTimeout(()=>{

body.scrollTop=
body.scrollHeight;

},50);

}
function sendMsg(){

let val=
document.getElementById(
"msg"
).value.toLowerCase();

if(val=="")
return;

let ans="";

if(
val.includes("risk")
){

ans=
"Current churn risk: " +
"RISK_PLACEHOLDER";

}

else if(
val.includes("customer")
){

ans=
"Customer: CUSTOMER_PLACEHOLDER";

}

else if(
val.includes("income")
){

ans=
"Income: ₹INCOME_PLACEHOLDER";

}

else if(
val.includes("logins")
){

ans=
"Digital Logins: LOGINS_PLACEHOLDER";

}
else if(
val.includes("retention")
){

ans=
"Retention score: RETENTION_PLACEHOLDER%";

}

else{

ans=
"Try: risk, customer, income, logins";

}

addMsg(ans);

document.getElementById(
"msg"
).value="";

}
</script>

"""
    retention = round(
    (1-risk)*100
    )

    html_code = html_code.replace(
    "RISK_PLACEHOLDER",
    str(
    round(
    risk*100
    )
    )+"%"
    )

    html_code = html_code.replace(
    "CUSTOMER_PLACEHOLDER",
    str(name)
    )

    html_code = html_code.replace(
    "INCOME_PLACEHOLDER",
    str(income)
    )

    html_code = html_code.replace(
    "LOGINS_PLACEHOLDER",
    str(logins)
    )

    html_code = html_code.replace(
    "RETENTION_PLACEHOLDER",
    str(retention)
    )
    saved = int(
    income*0.05
    )

    html_code = html_code.replace(
    "REVENUE_PLACEHOLDER",
    str(saved)
    )
    components.html(
    html_code,
    height=0,
    width=0
    )
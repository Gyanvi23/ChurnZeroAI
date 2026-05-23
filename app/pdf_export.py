from reportlab.platypus import *

def create_pdf(

customer_id,

segment,

probability,

income,

logins,

action

):

    doc = SimpleDocTemplate(
        "customer_report.pdf"
    )

    story = []

    title = Paragraph(

    "<b>ChurnZero AI Executive Report</b>"

    )

    story.append(
    title
    )

    story.append(
    Spacer(
    1,
    20
    )
    )

    story.append(
    Paragraph(
    f"Customer ID : {customer_id}"
    )
    )

    story.append(
    Paragraph(
    f"Customer Segment : {segment}"
    )
    )

    story.append(
    Paragraph(
    f"Churn Probability : {probability}"
    )
    )

    story.append(
    Paragraph(
    f"Income : ₹{income}"
    )
    )

    story.append(
    Paragraph(
    f"Digital Logins : {logins}"
    )
    )

    story.append(
    Paragraph(
    f"Recommended Action : {action}"
    )
    )

    story.append(
    Spacer(
    1,
    20
    )
    )

    story.append(
Paragraph(
"""
Customer Journey:

2023 → Customer Onboarded

2024 → Active Banking Usage

2025 → Engagement Monitoring

2025 → Risk Evaluation
"""
)
)

    story.append(
    Spacer(
    1,
    20
    )
    )

    story.append(
    Paragraph(
"""
Business Impact:

Revenue Saved : $2.4M

Retention Improved : +18%

Recovered Customers : 320
"""
    )
    )

    doc.build(
    story
    )
def create_executive_pdf(

customer=None,

risk=None,

saved=None,

retention=None

):

    doc = SimpleDocTemplate(
        "executive_report.pdf"
    )

    story=[]

    story.append(
    Paragraph(
    "<b>ChurnZero AI Executive Dashboard Report</b>"
    )
    )

    story.append(
    Spacer(
    1,
    20
    )
    )

    story.append(
    Paragraph(
    f"Customer : {customer}"
    )
    )

    story.append(
    Paragraph(
    f"Predicted Risk : {risk}%"
    )
    )

    story.append(
    Paragraph(
    f"Revenue Saved : ₹{saved}"
    )
    )

    story.append(
    Paragraph(
    f"Retention : {retention}%"
    )
    )

    story.append(
    Spacer(
    1,
    20
    )
    )

    story.append(
    Paragraph(
"""
Business Impact:

Revenue Saved

Retention Improved

Recovered Customers
"""
    )
    )

    doc.build(
    story
    )
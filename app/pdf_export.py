from reportlab.platypus import *

def create_pdf(

customer_id,

segment,

probability,

balance,

transactions,

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
    f"Balance : ₹{balance}"
    )
    )

    story.append(
    Paragraph(
    f"Transactions : {transactions}"
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

2023 → Account Created

2024 → Active Customer

2025 → Reduced Activity

2025 → High Risk
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
def create_executive_pdf():

    doc = SimpleDocTemplate(
        "executive_report.pdf"
    )

    story = []

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
"""
KPIs:

Total Customers : 12,540

Churn Percentage : 18%

Revenue Saved : $2.4M

Live Alerts : 32
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
Top Risk Customers:

CUST1001 → 92%

CUST1002 → 87%

CUST1003 → 82%

CUST1004 → 79%
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
Manager Performance:

Actions Triggered : 120

Recovered : 78

Success Rate : 82%
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
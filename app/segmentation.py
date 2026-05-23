def customer_segment(
risk
):

    if risk > 0.8:

        return "High Risk"

    elif risk > 0.5:

        return "Medium Risk"

    else:

        return "Retained"
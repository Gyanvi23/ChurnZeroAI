def retention_plan(
    segment
):

    if segment == "High Risk":

        return (
            "Assign Relationship Manager"
        )

    elif segment == "Silent":

        return (
            "Give Cashback Offer"
        )

    else:

        return (
            "Start Retention Campaign"
        )
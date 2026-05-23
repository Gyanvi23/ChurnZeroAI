def retention_plan(
segment
):

    if segment == "High Risk":

        return (
        "Assign Relationship Manager"
        )

    elif segment == "Medium Risk":

        return (
        "Offer Cashback Campaign"
        )

    else:

        return (
        "No Action Needed"
        )
def customer_segment(
    balance,
    transactions
):

    if balance > 100000:

        return "VIP"

    elif transactions < 5:

        return "Silent"

    else:

        return "High Risk"
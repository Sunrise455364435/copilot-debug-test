from datetime import datetime, timedelta

def renew_subscription(user_type, last_renewal_date, plan_days, credit_card_valid, is_trial):
    renewal_date = last_renewal_date + plan_days  #  wrong: plan_days should be timedelta
    if not credit_card_valid:
        return "Renewal failed"

    if is_trial:
        discount = 10  #  wrong: trial users shouldn’t be charged or get a discount
    else:
        discount = 0.1

    amount = 100 - discount  #  wrong: discount is not calculated as percentage
    return {
        "next_renewal": renewal_date,
        "amount_charged": amount,
        "status": "renewed"
    }

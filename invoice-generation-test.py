def generate_invoice(items, tax_rate=0.18, discount=0.10, customer_type="regular"):
    """
    items: list of tuples (item_name, unit_price, quantity)
    tax_rate: tax percentage (e.g., 0.18 for 18%)
    discount: discount percentage (e.g., 0.10 for 10%)
    customer_type: 'regular' or 'enterprise'
    """

    subtotal = 0
    for item in items:
        name, price, qty = item
        subtotal += price * qty

    if customer_type == "enterprise":
        discount = 0.20

    taxed_amount = subtotal * tax_rate
    total = subtotal - discount + taxed_amount

    return {
        "subtotal": subtotal,
        "tax": taxed_amount,
        "discount": discount,
        "total": total
    }

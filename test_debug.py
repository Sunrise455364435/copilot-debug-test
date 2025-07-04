def calculate_total(price, tax):
    return price + price * tax
print(calculate_total("100", 0.1))  # This crashes

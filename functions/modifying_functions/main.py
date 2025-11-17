def apply_discount(price, discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price

def apply_tax(price, tax=0.07):
    taxed_price = price * (1 + tax)
    return taxed_price

def calculate_total(price, discount=.05, tax=0.07):
    discounted = apply_discount(price, discount)
    final = apply_tax(discounted, tax)
    return final

final = calculate_total(120)

print(f"Total cost with default discount and tax: ${final}")

print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.10, tax=0.08)}")


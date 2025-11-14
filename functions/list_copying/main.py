def apply_discount(prices):
    prices_copy = prices.copy()
    #unpack the prices copy information for the length of the list
    for index in range(len(prices_copy)):
        if prices_copy[index] > 2.00:
            prices_copy[index] *= 0.90
    #don't indent to ensure it runs after the loop is done
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: {updated_prices}")
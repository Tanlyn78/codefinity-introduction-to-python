# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenues = []
    for i in range(len(prices)):
        revenues.append(prices[i] * quantities_sold[i])
    return revenues

def formatted_output(revenues):
    for product_name, revenue in revenues:
        print(f"{product_name.lower()} has total revenue of ${revenue}")

# Re-create the zip (it was consumed by calculate_revenue)
revenue_list = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue_list))
revenue_per_product = sorted(revenue_per_product, key=lambda x: x[0])
formatted_output(revenue_per_product)
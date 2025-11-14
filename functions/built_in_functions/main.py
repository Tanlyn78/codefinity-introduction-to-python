# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, (price_str, quantity_str) in products.items():
    price = float(price_str)
    quantity = int(quantity_str)
    total_sales = price * quantity
    print(f"Total sales for {product}: ${total_sales}")
    total_sales_list.append(total_sales)

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list) 
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum Sales: ${min_sales}")
print(f"Maximum Sales: ${max_sales}")


    
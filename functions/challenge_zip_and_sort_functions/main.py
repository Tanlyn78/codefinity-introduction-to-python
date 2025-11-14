# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]
#combine lists in a tuple
combined_list = list(zip(products, prices, quantities_sold))
#sort products alphabetically
sorted_products = sorted(combined_list)

#unpack the combined_list to print specific content from the lists
for name, price, quantity in sorted_products:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {quantity}")
# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for item in inventory:
    #unpacking the item list in inventory
    current_stock, min_stock, restock_quantity, on_sale = inventory[item]
    print(f"Processing {item}")
    while current_stock < min_stock:
        #adding the restock amount to current stock 
        current_stock = current_stock + restock_quantity
        #updating the current stock value based on the line above
        inventory[item][0] = current_stock
        
    if current_stock> discount_threshold:
            inventory[item][3] = True
print("Processing Completed.")
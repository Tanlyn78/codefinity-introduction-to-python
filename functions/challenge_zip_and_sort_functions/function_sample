# Function to check stock levels of grocery items

def check_stock(inventory):
    for item, stock in inventory.items():
        if stock < 10:
            print(f"Warning: {item} is running low on stock with only {stock} units left!")
            print("Please restock the item before proceeding with the check.")
            return  # Stops the function if stock is below 10
        print(f"{item} has sufficient stock: {stock} units.")
    
    print("All items have sufficient stock.")

# Example inventory of a grocery store
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Milk": 8,  # This will trigger the early exit
    "Bread": 25
}

# Check stock levels
check_stock(inventory)

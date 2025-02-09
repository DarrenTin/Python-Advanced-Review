# Function to calculate total price
def calculate_total(items):
    total = sum(items.values())
    return total

# Main program
if __name__ == "__main__":
    print("Welcome to the Grocery Price Calculator!")

    # Dictionary to hold item prices
    items = {}

    # Input prices for various grocery items
    while True:
        item_name = input("Enter the item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        
        price = float(input(f"Enter the price for {item_name}: "))
        items[item_name] = price

    # Calculate the total
    total_bill = calculate_total(items)

    # Display the items and their prices
    print("\nYour grocery list and prices:")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
    
    # Display the total bill
    print(f"\nTotal Bill: ${total_bill:.2f}")

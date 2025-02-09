# Function to calculate the tip and total bill
def calculate_tip_and_total(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip
    return tip, total

# Main program
if __name__ == "__main__":
    print("Welcome to the Tip Calculator!")

    # Input: Total bill and tip percentage
    bill_amount = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

    # Calculate the tip and total
    tip, total = calculate_tip_and_total(bill_amount, tip_percentage)

    # Display the results
    print(f"Tip: ${tip:.2f}")
    print(f"Total bill including tip: ${total:.2f}")

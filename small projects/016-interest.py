# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Main program
if __name__ == "__main__":
    print("Welcome to the Simple Interest Calculator!")

    # Input: Principal amount, rate of interest, and time
    principal = float(input("Enter the principal amount: $"))
    rate = float(input("Enter the rate of interest (in percentage): "))
    time = float(input("Enter the time period (in years): "))

    # Calculate the interest
    interest = calculate_simple_interest(principal, rate, time)

    # Display the result
    print(f"The simple interest is: ${interest:.2f}")
    total_amount = principal + interest
    print(f"The total amount after {time} years is: ${total_amount:.2f}")

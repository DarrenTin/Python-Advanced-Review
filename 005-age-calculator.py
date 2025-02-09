from datetime import datetime

# Function to calculate age
def calculate_age(birth_date):
    current_date = datetime.now()
    age = current_date - birth_date
    years = age.days // 365.25  # Account for leap years
    days = age.days % 365.25
    return f"{int(years)} years {int(days)} days"  # Convert to integers

# Example usage
# birth_date = "2002-12-09"  # Replace with the person's birth year
birth_date = input("Please enter your birth date (yyyy-mm-dd): ")
birth_date = datetime.strptime(birth_date, "%Y-%m-%d") # Changed variable name for clarity
age = calculate_age(birth_date)
print(f"{age}")
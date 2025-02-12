from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_date_input(prompt):
    """Function to get valid date input from user."""
    while True:
        date_str = input(prompt).strip()
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid format! Please enter date in YYYY-MM-DD format.")

def calculate_date_difference(date1, date2):
    """Calculate the difference between two dates in years, months, and days."""
    delta = relativedelta(date2, date1)
    
    years = delta.years
    months = delta.months
    days = delta.days

    return years, months, days

# Main program
if __name__ == "__main__":
    print("Welcome to the Date Difference Calculator!")

    # Get user input for dates
    date1 = get_date_input("Enter the first date (YYYY-MM-DD): ")
    date2 = get_date_input("Enter the second date (YYYY-MM-DD): ")

    # Ensure the correct order of dates
    if date2 < date1:
        date1, date2 = date2, date1  # Swap to always calculate positive difference

    # Calculate the date difference
    years, months, days = calculate_date_difference(date1, date2)

    # Display result
    print(f"\nDate Difference:")
    print(f"{years} Years, {months} Months, {days} Days")

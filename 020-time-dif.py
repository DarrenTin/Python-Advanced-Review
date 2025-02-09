from datetime import datetime

def get_time_input(prompt):
    """Function to get valid time input from user."""
    while True:
        time_str = input(prompt).strip()
        try:
            return datetime.strptime(time_str, "%H:%M:%S").time()
        except ValueError:
            print("Invalid format! Please enter time in HH:MM:SS format.")

def calculate_time_difference(time1, time2):
    """Calculate the difference between two time objects."""
    fmt = "%H:%M:%S"
    t1 = datetime.strptime(str(time1), fmt)
    t2 = datetime.strptime(str(time2), fmt)

    # If second time is earlier, assume it's on the next day
    if t2 < t1:
        t2 = t2.replace(day=t2.day + 1)

    diff = t2 - t1
    return diff

# Main program
if __name__ == "__main__":
    print("Welcome to the Time Difference Calculator!")
    
    # Get user input for timestamps
    time1 = get_time_input("Enter the first time (HH:MM:SS): ")
    time2 = get_time_input("Enter the second time (HH:MM:SS): ")

    # Calculate the time difference
    time_diff = calculate_time_difference(time1, time2)
    
    # Display result
    print(f"\nTime Difference: {time_diff}")
    print(f"Hours: {time_diff.seconds // 3600}, Minutes: {(time_diff.seconds % 3600) // 60}, Seconds: {time_diff.seconds % 60}")

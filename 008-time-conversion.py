# Function to convert hours to minutes and seconds
def hours_to_minutes_seconds(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds

# Function to convert minutes to hours and seconds
def minutes_to_hours_seconds(minutes):
    hours = minutes / 60
    seconds = minutes * 60
    return hours, seconds

# Function to convert seconds to hours and minutes
def seconds_to_hours_minutes(seconds):
    hours = seconds / 3600
    minutes = (seconds % 3600) / 60
    return hours, minutes

# Example usage
unit = input("Enter the unit to convert (hours, minutes, or seconds): ").lower()

if unit == "hours":
    hours = float(input("Enter the time in hours: "))
    minutes, seconds = hours_to_minutes_seconds(hours)
    print(f"{hours} hours is equal to {minutes} minutes or {seconds} seconds.")

elif unit == "minutes":
    minutes = float(input("Enter the time in minutes: "))
    hours, seconds = minutes_to_hours_seconds(minutes)
    print(f"{minutes} minutes is equal to {hours:.2f} hours or {seconds} seconds.")

elif unit == "seconds":
    seconds = float(input("Enter the time in seconds: "))
    hours, minutes = seconds_to_hours_minutes(seconds)
    print(f"{seconds} seconds is equal to {hours:.2f} hours or {minutes} minutes.")

else:
    print("Invalid unit. Please enter 'hours', 'minutes', or 'seconds'.")

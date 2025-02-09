import re

# Function to evaluate password strength
def check_password_strength(password):
    # Check the length of the password
    length = len(password)

    # Check if the password contains uppercase, lowercase, numbers, and special characters
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_numbers = bool(re.search(r'[0-9]', password))
    has_special_char = bool(re.search(r'[\W_]', password))

    # Evaluate the password strength based on conditions
    if length >= 8 and has_uppercase and has_lowercase and has_numbers and has_special_char:
        return "Strong"
    elif length >= 6 and (has_uppercase or has_lowercase) and has_numbers:
        return "Medium"
    else:
        return "Weak"

# Main program
if __name__ == "__main__":
    # Take input password from the user
    password = input("Enter a password: ")

    # Check and display the password strength
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

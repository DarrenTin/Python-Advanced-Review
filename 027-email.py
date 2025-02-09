import re

def is_valid_email(email):
    """Validates if the email address is in correct format."""
    
    # Regular expression for validating email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Matching the input email with the regex pattern
    if re.match(email_regex, email):
        return "✅ Valid Email!"
    else:
        return "❌ Invalid Email!"

# Main program
if __name__ == "__main__":
    print("📧 Email Validator 📧")
    
    while True:
        email_input = input("Enter email address to validate: ").strip()
        
        if email_input:  # Ensure email input is not empty
            result = is_valid_email(email_input)
            print(result)
            break
        else:
            print("Email cannot be empty. Please enter a valid email address.")

import random
import string

def generate_password(length=12):
    """Generates a strong password with a default length of 12 characters."""
    
    if length < 4:
        return "❌ Password length must be at least 4 characters."

    # Character pools
    uppercase = string.ascii_uppercase  # A-Z
    lowercase = string.ascii_lowercase  # a-z
    digits = string.digits  # 0-9
    special_chars = string.punctuation  # Special characters

    # Ensuring at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest with random choices from all categories
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to mix characters
    random.shuffle(password)

    return "".join(password)

# Main program
if __name__ == "__main__":
    print("🔐 Strong Password Generator 🔐")
    
    while True:
        try:
            length_input = input("Enter password length (default is 12, press Enter to skip): ").strip()
            length = int(length_input) if length_input else 12

            if length < 4:
                print("Password must be at least 4 characters long for security reasons.")
                continue

            password = generate_password(length)
            print(f"🔑 Generated Password: {password}")
            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

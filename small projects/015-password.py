import re

def check_password_strength(password):
    length = len(password)
    has_number = bool(re.search(r'[0-9]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_special = bool(re.search(r'[\W_]', password))

    if length >= 10 and has_number and has_lower and has_upper and has_special:
        return 'strong'
    elif length >= 8 and has_number and (has_lower or has_upper):
        return 'medium'
    else:
        return 'weak'

password = input("password:")
strength = check_password_strength(password)
print(strength)
# Function to convert a decimal number to binary
def decimal_to_binary(num):
    return bin(num)[2:]

# Function to convert a decimal number to octal
def decimal_to_octal(num):
    return oct(num)[2:]

# Function to convert a decimal number to hexadecimal
def decimal_to_hexadecimal(num):
    return hex(num)[2:]

# Function to convert a binary number to decimal
def binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        raise ValueError("Invalid binary number. Please enter a valid binary number.")

# Function to convert an octal number to decimal
def octal_to_decimal(octal_str):
    try:
        return int(octal_str, 8)
    except ValueError:
        raise ValueError("Invalid octal number. Please enter a valid octal number.")

# Function to convert a hexadecimal number to decimal
def hexadecimal_to_decimal(hex_str):
    try:
        return int(hex_str, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal number. Please enter a valid hexadecimal number.")

# Function to check if input is a valid number for the given base
def is_valid_number_for_base(number_str, base):
    if base == 'binary':
        return all(c in '01' for c in number_str)
    elif base == 'octal':
        return all(c in '01234567' for c in number_str)
    elif base == 'hexadecimal':
        return all(c in '0123456789ABCDEFabcdef' for c in number_str)
    return False

# Main program
if __name__ == "__main__":
    print("Welcome to the Enhanced Number Base Converter!")

    # Ask user for the type of conversion they want to perform
    choice = input("Choose the conversion: \n1. Decimal to Binary/Octal/Hexadecimal \n2. Binary/Octal/Hexadecimal to Decimal\nEnter 1 or 2: ")

    if choice == '1':
        # Input: Decimal number
        try:
            num = int(input("Enter a decimal number: "))
            
            # Convert and display results
            print(f"Decimal {num} to Binary: {decimal_to_binary(num)}")
            print(f"Decimal {num} to Octal: {decimal_to_octal(num)}")
            print(f"Decimal {num} to Hexadecimal: {decimal_to_hexadecimal(num)}")
        except ValueError:
            print("Invalid decimal number. Please enter a valid integer.")
    
    elif choice == '2':
        # Input: Type of number system and the number
        base = input("Enter the base of the number (binary, octal, hexadecimal): ").lower()
        
        if base not in ['binary', 'octal', 'hexadecimal']:
            print("Invalid base. Please enter binary, octal, or hexadecimal.")
            exit()

        num_str = input(f"Enter the {base} number: ").strip()

        # Validate the number format for the chosen base
        if not is_valid_number_for_base(num_str, base):
            print(f"Invalid {base} number. Please enter a valid {base} number.")
            exit()

        # Convert based on input base and display result
        try:
            if base == 'binary':
                decimal_value = binary_to_decimal(num_str)
            elif base == 'octal':
                decimal_value = octal_to_decimal(num_str)
            elif base == 'hexadecimal':
                decimal_value = hexadecimal_to_decimal(num_str)
            
            print(f"{base.capitalize()} {num_str} to Decimal: {decimal_value}")
        
        except ValueError as e:
            print(e)
    
    else:
        print("Invalid choice. Please choose 1 or 2.")

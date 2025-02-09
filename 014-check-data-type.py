# Function to check and return the data type of the input
def check_data_type(user_input):
    try:
        # Try to convert the input to a float
        float_input = float(user_input)
        if '.' in user_input:
            return 'float'
        else:
            return 'integer'
    except ValueError:
        # If conversion to float fails, check for other data types
        if user_input.lower() == 'true' or user_input.lower() == 'false':
            return 'boolean'
        elif user_input.lower() == 'none':
            return 'NoneType'
        else:
            return 'string'

# Main program
if __name__ == "__main__":
    # Take input from user
    user_input = input("Enter something: ")

    # Check and display the data type
    data_type = check_data_type(user_input)
    print(f"The data type of your input is: {data_type}")

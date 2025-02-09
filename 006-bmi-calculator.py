# Function to calculate BMI and categorize it
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / height (m)^2
    bmi = weight / (height ** 2)
    
    # Categorize BMI
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    
    return bmi, category

# Example usage
weight = float(input("Enter your weight in kg: "))  # Get weight input
height = float(input("Enter your height in meters: "))  # Get height input

bmi, category = calculate_bmi(weight, height)

print(f"Your BMI is {bmi:.2f}. Category: {category}")

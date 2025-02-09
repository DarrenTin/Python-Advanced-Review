# Function to calculate grade based on score
def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid score. Please enter a score between 0 and 100."

# Main program
if __name__ == "__main__":
    # Input: User's numeric score
    score = float(input("Enter your score (0-100): "))

    # Calculate the grade
    grade = calculate_grade(score)

    # Display the result
    print(f"Your grade is: {grade}")

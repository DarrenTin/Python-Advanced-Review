from datetime import datetime

def is_eligible_to_vote(birth_year, citizenship, criminal_record):
    """Checks voting eligibility based on age, citizenship, and criminal record."""
    
    current_year = datetime.now().year
    age = current_year - birth_year

    if age < 18:
        return f"❌ Not eligible: You are {age} years old. Must be at least 18 to vote."
    
    if citizenship.lower() != "yes":
        return "❌ Not eligible: Only citizens are allowed to vote."
    
    if criminal_record.lower() == "yes":
        return "❌ Not eligible: People with felony convictions may not be allowed to vote."

    return "✅ Eligible: You meet all voting requirements!"

# Main program
if __name__ == "__main__":
    print("🗳 Voting Eligibility Checker 🗳")
    
    while True:
        try:
            birth_year = int(input("Enter your birth year: "))
            if birth_year > datetime.now().year or birth_year < 1900:
                print("Invalid birth year! Please enter a realistic value.")
                continue

            citizenship = input("Are you a citizen? (yes/no): ").strip().lower()
            if citizenship not in ["yes", "no"]:
                print("Invalid input! Please enter 'yes' or 'no'.")
                continue

            criminal_record = input("Do you have a felony conviction? (yes/no): ").strip().lower()
            if criminal_record not in ["yes", "no"]:
                print("Invalid input! Please enter 'yes' or 'no'.")
                continue

            # Check voting eligibility
            result = is_eligible_to_vote(birth_year, citizenship, criminal_record)
            print(result)
            break

        except ValueError:
            print("Invalid input! Please enter numeric values for birth year.")

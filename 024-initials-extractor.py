def get_initials(full_name):
    """Converts a full name into initials (e.g., 'John Doe' → 'J.D.')"""
    
    # Remove extra spaces and split name into words
    name_parts = full_name.strip().split()
    
    # Extract first letter of each name part and convert to uppercase
    initials = [name[0].upper() for name in name_parts if name[0].isalpha()]
    
    return ".".join(initials) + "." if initials else "Invalid Name"

# Main program
if __name__ == "__main__":
    print("🔠 Name Initials Extractor 🔠")

    while True:
        full_name = input("Enter full name: ").strip()
        
        if full_name:  # Ensure input is not empty
            initials = get_initials(full_name)
            print(f"🔹 Initials: {initials}")
            break
        else:
            print("Name cannot be empty! Please enter a valid name.")

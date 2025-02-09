def sort_data(data, criteria="value", order="ascending"):
    """
    Sorts a list based on user-selected criteria and order.
    
    :param data: List of items to sort.
    :param criteria: Sorting criteria ('value', 'length', 'alphabetical').
    :param order: Sorting order ('ascending' or 'descending').
    :return: Sorted list.
    """
    try:
        if not isinstance(data, list):
            raise ValueError("Input data must be a list.")

        if criteria == "value":  # Sort by numerical or alphabetical value
            sorted_data = sorted(data, reverse=(order == "descending"))
        elif criteria == "length":  # Sort by length of items (for strings)
            sorted_data = sorted(data, key=len, reverse=(order == "descending"))
        elif criteria == "alphabetical":  # Sort alphabetically (for words)
            sorted_data = sorted(data, key=str.lower, reverse=(order == "descending"))
        else:
            raise ValueError("Invalid criteria! Choose 'value', 'length', or 'alphabetical'.")

        return sorted_data

    except Exception as e:
        return f"❌ Error: {e}"

# Main program
if __name__ == "__main__":
    print("📊 Data Sorting Function 📊")

    # User inputs a list
    raw_data = input("Enter a list of numbers or words (comma-separated): ").strip()
    data_list = [x.strip() for x in raw_data.split(",")]

    # Check if all items are numbers and convert them
    if all(x.replace(".", "", 1).isdigit() for x in data_list):
        data_list = [float(x) if "." in x else int(x) for x in data_list]

    # User chooses sorting criteria
    print("\n🔹 Choose Sorting Criteria: ")
    print("1️⃣ Value (Numeric or Alphabetical)")
    print("2️⃣ Length (Word Length)")
    print("3️⃣ Alphabetical Order")
    
    criteria_choice = input("Enter choice (1/2/3, default: 1): ").strip()
    criteria_map = {"1": "value", "2": "length", "3": "alphabetical"}
    criteria = criteria_map.get(criteria_choice, "value")

    # User chooses sorting order
    order = input("Enter sorting order ('ascending' or 'descending', default: ascending): ").strip().lower()
    if order not in ["ascending", "descending"]:
        order = "ascending"

    # Perform sorting
    sorted_result = sort_data(data_list, criteria, order)
    
    print("\n✅ Sorted Data:")
    print(sorted_result)

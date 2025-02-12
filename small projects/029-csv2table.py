import pandas as pd
from tabulate import tabulate

def display_csv_as_table(csv_file, num_rows=10):
    """
    Reads a CSV file and displays it as a formatted table on the screen.
    
    :param csv_file: Path to the CSV file.
    :param num_rows: Number of rows to display (default: 10).
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Display the table with a readable format
        print("\n📊 CSV Data Table:\n")
        print(tabulate(df.head(num_rows), headers='keys', tablefmt='grid'))

    except FileNotFoundError:
        print("❌ Error: CSV file not found!")
    except pd.errors.EmptyDataError:
        print("❌ Error: The CSV file is empty!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    csv_path = input("Enter the CSV file path: ").strip()
    rows = input("Enter number of rows to display (default 10, press Enter to skip): ").strip()
    num_rows = int(rows) if rows.isdigit() else 10

    display_csv_as_table(csv_path, num_rows)

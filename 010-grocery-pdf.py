from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

# Function to calculate total price
def calculate_total(items):
    total = sum(items.values())
    return total

# Function to generate PDF invoice
def generate_invoice(items, total_bill):
    doc = SimpleDocTemplate("invoice.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    style = styles["Normal"]

    elements = []

    # Title
    title = Paragraph("Grocery Invoice", styles["h1"])
    elements.append(title)
    elements.append(Spacer(1, 12))  # Add some space

    # Itemized list
    data = [["Item", "Price"]]  # Table header
    for item, price in items.items():
        data.append([item, f"${price:.2f}"])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Row background
        ('GRID', (0,0), (-1,-1), 1, colors.black) # Add grid lines
    ]))
    elements.append(table)
    elements.append(Spacer(1, 24))  # Add some space


    # Total bill
    total_text = Paragraph(f"<b>Total Bill: ${total_bill:.2f}</b>", styles["h2"]) # Make total bold and larger
    elements.append(total_text)

    doc.build(elements)
    print("Invoice generated successfully!")



# Main program
if __name__ == "__main__":
    print("Welcome to the Grocery Price Calculator!")

    # Dictionary to hold item prices
    items = {}

    # Input prices for various grocery items
    while True:
        item_name = input("Enter the item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break

        try:  # Handle potential errors if user enters non-numeric input
            price = float(input(f"Enter the price for {item_name}: "))
            items[item_name] = price
        except ValueError:
            print("Invalid input. Please enter a number for the price.")


    # Calculate the total
    total_bill = calculate_total(items)

    # Display the items and their prices
    print("\nYour grocery list and prices:")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")

    # Display the total bill
    print(f"\nTotal Bill: ${total_bill:.2f}")

    # Generate the invoice
    generate_invoice(items, total_bill)
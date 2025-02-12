from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors

def totalize(items):
    total = sum(i[1] for i in items)
    return total

def generate_pdf(items, total_bill, pdf_name='invoice1.pdf'):
    doc = SimpleDocTemplate(pdf_name)
    styles = getSampleStyleSheet()
    elements = []

    img = Image(r"small projects\logo.jpg", width=200, height=200)
    elements.append(img)
    title = Paragraph("Buy Record", styles["h1"])
    elements.append(title)
    elements.append(Spacer(1, 12)) # 1 width, 12 height

    data = [['Item', 'Price']] # table header
    col_widths = [300, 100]
    
    for i in items:
        data.append([i[0], f"${i[1]:.2f}"]) # table data

    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        # ('STYLE_TYPE', (row_start [x], col_start [y]), (row_end, col_end), style_value),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all text
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding for header
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Row background color
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Grid lines for table
    ]))
    elements.append(table)
    elements.append(Spacer(1, 24))

    total_text = Paragraph(f"<b>Total Bills: ${total_bill:.2f}</b>", styles['h2'])
    elements.append(total_text)

    doc.build(elements)
    print("Invoice generated")

items = []

while True:
    item = input("Item name ('done'): ")
    if item == 'done':
        break
    price = float(input(f"Price of {item}: "))
    items.append([item, price])

print("Grocery list\n------------------")
print("Item\tPrice")
for i in items:
    print(f"{i[0]}\t${i[1]}")
total_bill = totalize(items)
print(f"total bill: ${total_bill:.2f}")
generate_pdf(items, total_bill)
def enter_bill():
    bill = float(input("Enter bill: "))
    percent = float(input("Percentage: "))
    return bill, percent

def calculate_tip(bill, pencent):
    total = bill + bill * pencent / 100
    return f"{total:.1f}"

bill, percent = enter_bill()
print("Total:", calculate_tip(bill, percent))
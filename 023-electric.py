def calculate_electricity_bill(units):
    """Calculates electricity bill based on tiered rates."""
    
    # Tiered Pricing (Example: Adjust based on your local rates)
    tier1_rate = 0.12  # First 100 kWh
    tier2_rate = 0.15  # 101-300 kWh
    tier3_rate = 0.20  # 301-500 kWh
    tier4_rate = 0.25  # Above 500 kWh

    service_charge = 10  # Fixed monthly service charge

    if units <= 100:
        cost = units * tier1_rate
    elif units <= 300:
        cost = (100 * tier1_rate) + ((units - 100) * tier2_rate)
    elif units <= 500:
        cost = (100 * tier1_rate) + (200 * tier2_rate) + ((units - 300) * tier3_rate)
    else:
        cost = (100 * tier1_rate) + (200 * tier2_rate) + (200 * tier3_rate) + ((units - 500) * tier4_rate)

    total_bill = cost + service_charge

    print("\n💡 Electricity Bill Breakdown:")
    print(f"Units Consumed: {units} kWh")
    print(f"Energy Cost: ${cost:.2f}")
    print(f"Service Charge: ${service_charge:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")

# Main program
if __name__ == "__main__":
    print("⚡ Electricity Bill Estimator ⚡")

    while True:
        try:
            units = float(input("Enter electricity consumption (kWh): "))
            if units < 0:
                print("Units consumed cannot be negative. Please enter a valid number.")
                continue
            calculate_electricity_bill(units)
            break
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")

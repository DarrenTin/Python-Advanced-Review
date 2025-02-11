exchange_rates = {
    'USD_to_EUR': 0.91,
    'EUR_to_USD': 1.10,
    'USD_to_GBP': 0.82,
    'GBP_to_USD': 1.22,
    'EUR_to_GBP': 0.90,
    'GBP_to_EUR': 1.11
}

def convert_currency(amount, from_currency="USD", to_currency="EUR"):
    conversion_key = f"{from_currency}_to_{to_currency}"
    if conversion_key in exchange_rates:
        new_amount = amount * exchange_rates[conversion_key]
        new_amount = f"{new_amount:.2f}"
        return new_amount
    else:
        return "Conversion key not found!"

print(convert_currency(100, "GBP", "EUR"))
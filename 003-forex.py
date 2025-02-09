# Define exchange rates (example rates)
exchange_rates = {
    'USD_to_EUR': 0.91,
    'EUR_to_USD': 1.10,
    'USD_to_GBP': 0.82,
    'GBP_to_USD': 1.22,
    'EUR_to_GBP': 0.90,
    'GBP_to_EUR': 1.11
}

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    conversion_key = f"{from_currency}_to_{to_currency}"
    if conversion_key in exchange_rates:
        conversion_rate = exchange_rates[conversion_key]
        return amount * conversion_rate
    else:
        return f"Unsupported currency conversion: {from_currency} to {to_currency}"

# Example usage
amount = 100  # Amount to convert
from_currency = 'USD'
to_currency = 'EUR'

converted = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}")

# Another example
amount = 50  # Amount to convert
from_currency = 'EUR'
to_currency = 'GBP'

converted = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}")

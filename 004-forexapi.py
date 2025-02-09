import requests

# Function to get exchange rate from API
def get_exchange_rate(from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    # Check if the request was successful
    if data['result'] == 'success':
        # print(data)
        exchange_rate = data['conversion_rates'].get(to_currency)
        if exchange_rate:
            return exchange_rate
        else:
            return f"Conversion rate for {to_currency} not available."
    else:
        return "Error fetching exchange rates."

# Function to convert currency
def convert_currency(amount, from_currency, to_currency, api_key):
    exchange_rate = get_exchange_rate(from_currency, to_currency, api_key)
    
    if isinstance(exchange_rate, float):
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return exchange_rate

# Example usage
api_key = ''  # Replace with your API key
amount = 100
from_currency = 'USD'
to_currency = 'MYR'

converted = convert_currency(amount, from_currency, to_currency, api_key)
if isinstance(converted, float):
    print(f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}")
else:
    print(converted)

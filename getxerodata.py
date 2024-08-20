import requests

class XEClient:
    def __init__(self, api_id, api_key):
        self.api_id = api_id
        self.api_key = api_key
        self.base_url = 'https://xecdapi.xe.com/v1/'

    def get_currencies(self):
        url = self.base_url + 'currencies'
        response = requests.get(url, auth=(self.api_id, self.api_key))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve currencies: {response.status_code} - {response.text}")
            return None

    def convert_currency(self, from_currency, to_currency, amount):
        url = self.base_url + 'convert_from/'
        params = {
            'from': from_currency,
            'to': to_currency,
            'amount': amount
        }
        response = requests.get(url, auth=(self.api_id, self.api_key), params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to convert currency: {response.status_code} - {response.text}")
            return None

# Example usage:

# API credentials
api_id = 'yourapiid'
api_key = 'yourapikey'

# Instantiate the client
client = XEClient(api_id, api_key)

# Get all available currencies
currencies = client.get_currencies()
if currencies:
    print("Available Currencies:")
    for currency in currencies['currencies']:
        print(f"{currency['currency_name']} ({currency['currency_code']})")

# Convert from one currency to another
from_currency = 'USD'
to_currency = 'EUR'
amount = 100
conversion = client.convert_currency(from_currency, to_currency, amount)
if conversion:
    print(f"\n{amount} {from_currency} is equal to {conversion['to'][0]['mid']} {to_currency}")

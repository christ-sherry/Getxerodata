import requests
import json

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
        url = f"{self.base_url}convert_from.json/?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(url, auth=(self.api_id, self.api_key))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to convert currency: {response.status_code} - {response.text}")
            return None

# API credentials
api_id = 'autochekafrica632696224'
api_key = 'c3sei1i6pm28b6m1d57r0mqttp'

# Instantiate the client
client = XEClient(api_id, api_key)

# Get all available currencies
currencies2_data = client.get_currencies()
if currencies2_data:
    # Specify the filename to save the data
    filename = 'currencies2_data.json'
    
    # Save the data to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(currencies2_data, json_file, indent=4)
    
    print(f"Currency data has been saved to {filename}")

    # Print the available currencies
    print("Available Currencies:")
    for currency in currencies2_data['currencies']:
        print(f"{{currency['currency_name']}} ({{currency['currency_code']}})")

    # Convert from one currency to another
    from_currency = 'USD'
    to_currency = 'EUR'
    amount = 100
    conversion = client.convert_currency(from_currency, to_currency, amount)
    if conversion:
        print(f"\n{amount} {from_currency} is equal to {conversion['to'][0]['mid']} {to_currency}")
else:
    print("No data to save.")

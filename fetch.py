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

# Replace these with your actual API credentials
api_id = 'yourapiid'
api_key = 'yourapikey'

# Instantiate the client
client = XEClient(api_id, api_key)

# Get all available currencies
currencies_data = client.get_currencies()
if currencies_data:
    # Specify the filename you want
    filename = 'currencies_data.json'
    
    # Save the data to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(currencies_data, json_file, indent=4)
    
    print(f"Currency data has been saved to {filename}")
else:
    print("No data to save.")

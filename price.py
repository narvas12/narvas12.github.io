import requests

# Replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' with your actual API key and secret.
api_key = 'cWcf0itFyjpmCvnfb04cponvJ2XKlQDLthYGzE7YDDNHNkCCNRlkuroT6iQAztSY'
api_secret = 'q2wcxyzcEjWApYMVyAEDxzjycwApYJ5bsNi6i0QUSbG8XXEs3qkISpjfoRRFNvk0'

# Define the endpoint for fetching the price of a cryptocurrency.
symbol = 'BTCUSDT'  # Replace with the symbol of the cryptocurrency you want to fetch.

endpoint = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'

# Create a request header with your API key.
headers = {
    'X-MBX-APIKEY': api_key
}

# Send the GET request.
response = requests.get(endpoint, headers=headers)

if response.status_code == 200:
    data = response.json()
    price = data['price']
    print(f'Price of {symbol}: {price}')
else:
    print(f'Error: {response.status_code} - {response.text}')

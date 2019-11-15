import requests

endpoint = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(endpoint).json()
price = response[0].get('price_usd')
print(f'Bitcoin price is {price}$')

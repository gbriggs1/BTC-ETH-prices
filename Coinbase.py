import requests

url = "https://api.exchange.coinbase.com/products/BTC-USD/ticker"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)
d = {}
d['bid'] = response.json()['bid']
d['ask'] = response.json()['ask']

return d

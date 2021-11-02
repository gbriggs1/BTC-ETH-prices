import requests

def BTC():
    url = "https://api.exchange.coinbase.com/products/BTC-USD/ticker"
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    d = {}
    d['bid'] = "Buy: $"+str(response.json()['bid'])
    d['ask'] = "Sell: $"+str(response.json()['ask'])
    return d

def ETH():
    url = "https://api.exchange.coinbase.com/products/ETH-USD/ticker"
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    d = {}
    d['bid'] = "Buy: $"+str(response.json()['bid'])
    d['ask'] = "Sell: $"+str(response.json()['ask'])
    return d

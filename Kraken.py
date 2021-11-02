import requests

def BTC():
    resp = requests.get('https://api.kraken.com/0/public/Spread?pair=BTCUSD')

    bid = round(float(resp.json()['result']['XXBTZUSD'][0][1]), 3)
    ask = round(float(resp.json()['result']['XXBTZUSD'][0][2]), 3)
    d = {}
    d['bid'] = "Buy: $"+str(bid)
    d['ask'] = "Sell: $"+str(ask)
    return d
def ETH():
    resp = requests.get('https://api.kraken.com/0/public/Spread?pair=ETHUSD')

    bid = round(float(resp.json()['result']['XETHZUSD'][0][1]), 3)
    ask = round(float(resp.json()['result']['XETHZUSD'][0][2]), 3)
    d = {}
    d['bid'] = "Buy: $"+str(bid)
    d['ask'] = "Sell: $"+str(ask)
    return d

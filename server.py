import requests

resp = requests.get('https://api.kraken.com/0/public/Spread?pair=BTCUSD')

bid = resp.json()['result']['XXBTZUSD'][0][1]
ask = resp.json()['result']['XXBTZUSD'][0][2]
d = {}
d['bid'] = bid
d['ask'] = ask
return d

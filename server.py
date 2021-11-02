import Coinbase
import Kraken
from flask import Flask, render_template

# data = [{ --coinbase ---
#         'BTC':'{bid: , ask: }',
#         'ETH': {bid: , ask: }
#
#     },
#     { --kraken ---
#         'BTC': '{bid: , ask:}',
#         'ETH': {bid: , ask: }
#     }
# ]
app = Flask(__name__)

def bestVendor(coinbase, kraken):
    optimal = {}
    if coinbase['BTC']['bid'] > kraken['BTC']['bid']:
        bit = 'Bitcoin (BTC): You should buy from Kraken'
    else:
        bit = 'Bitcoin (BTC): You should buy from Coinbase'
    if coinbase['BTC']['ask'] > kraken['BTC']['ask']:
        bit = bit + ' and sell on Coinbase'
    else:
        bit = bit + ' and sell on Kraken'
    optimal['BTC'] = bit
    if coinbase['ETH']['bid'] > kraken['ETH']['bid']:
        eth = 'Ethereum (ETH): You should buy from Kraken'
    else:
        eth = 'Ethereum (ETH): You should buy from Coinbase'
    if coinbase['ETH']['ask'] > kraken['ETH']['ask']:
        eth = eth + ' and sell on Coinbase'
    else:
        eth = eth + ' and sell on Kraken'
    optimal['ETH'] = eth
    return optimal

@app.route('/')
def index():
    data = []
    coinbase = {}
    coinbase['BTC'] = Coinbase.BTC()
    coinbase['ETH'] = Coinbase.ETH()
    kraken = {}
    kraken['BTC'] = Kraken.BTC()
    kraken['ETH'] = Kraken.ETH()
    optimal = bestVendor(coinbase, kraken) #dictionary with val as a string set to display optimal choice

    data.append(coinbase)
    data.append(kraken)
    data.append(optimal)
    return render_template('index.html', data=data)




if __name__ == '__main__':
  app.run()

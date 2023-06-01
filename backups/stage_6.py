# Project: Currency Converter
# Stage 6/6: Last but not least
import requests
import json


currency_from = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{currency_from}.json")
data = json.loads(r.text)
cache = {'usd': data['usd']['rate'] if currency_from != 'usd' else 1,
         'eur': data['eur']['rate'] if currency_from != 'eur' else 1}
while True:
    currency_to = input().lower()
    if currency_to == '':
        break
    else:
        amount = int(input())
        print('Checking the cache...')
        if currency_to in cache.keys():
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            cache[currency_to] = data[currency_to]['rate']
        print(f'You received {round(amount * cache[currency_to], 2)} {currency_to.upper()}.')

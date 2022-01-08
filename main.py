import json
import requests


currency_from = input().lower()
cache = {}
r = requests.get(f"http://www.floatrates.com/daily/{currency_from}.json")
conv = json.loads(r.text)
if currency_from == "usd":
    cache["eur"] = conv["eur"]
elif currency_from == "eur":
    cache["usd"] = conv["usd"]
else:
    cache["usd"] = conv["usd"]
    cache["eur"] = conv["eur"]

while True:
    currency_to = input().lower()
    if len(currency_to) < 1:
        break
    else:
        amount = float(input())
        print("Checking the cache...")
        if currency_to in cache.keys():
            print("Oh! It is in the cache!")
            print(f"You received {round(amount * (cache[currency_to]['rate']), 2)} {currency_to.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            r = requests.get(f"http://www.floatrates.com/daily/{currency_from}.json")
            conv = json.loads(r.text)
            cache[currency_to] = conv[currency_to]
            print(f"You received {round(amount * (cache[currency_to]['rate']), 2)} {currency_to.upper()}.")

# Project: Currency Converter
# Stage 5/6: JSON and the Rates
import requests
import json


currency = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
rates = json.loads(r.text)
print(rates['usd'])
print(rates['eur'])

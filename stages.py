# Stage 5/6: JSON and the Rates
import requests
import json


currency = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
dic = json.loads(r.text)
print(dic["usd"])
print(dic["eur"])

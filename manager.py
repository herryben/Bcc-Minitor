import requests
import json
url = 'https://yunbi.com//api/v2/tickers/bcccny.json'
response = requests.request("GET", url, timeout=5)
result = json.loads(response.text)
print result['ticker']['buy']
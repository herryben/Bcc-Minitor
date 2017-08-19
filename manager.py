import requests
import json
import pickle
from common.emailhelper import MailHelper
from config import app_config
data = {}
try:
  with open('data', 'r') as f:
    data = pickle.load(f)
except Exception as e:
  pass
print data, 'data'
url = 'https://yunbi.com//api/v2/tickers/bcccny.json'
response = requests.request("GET", url, timeout=5)
result = json.loads(response.text)
buy = float(result['ticker']['buy'])
print buy, 'buy'
if abs( buy - data.get('last_buy', 0)) > app_config['buy_price_delta']:
  for k, v in app_config['email'].items():
    MailHelper.send_email(subject='the current buy price is %s' % buy,
      content='the current buy price is %s' % buy, from_addr='18647246574@163.com',
      to_addr=v, nick_name='Herry')
data['last_buy'] = buy
with open('data', 'w') as f:
  pickle.dump(data, f)
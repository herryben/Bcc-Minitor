#! /usr/bin/env python
#-*- coding: UTF-8 -*-

import requests
import json
import re
import pickle
from common.emailhelper import MailHelper
from config import app_config

def get_yun_bi_market_info():
    r = requests.get('https://yunbi.com/markets/bcccny')
    s = r.text
    rgx = re.compile(r'''"bcccny":{"name":"BCC/CNY","base_unit":"bcc","quote_unit":"cny","low":(.*?)}};gon.asks''')
    m = rgx.search(s)
    return eval('{"low":'+m.group(1)+'}')

data = {}
try:
  with open(app_config['data_path'], 'r') as f:
    data = pickle.load(f)
except Exception as e:
  pass
# print data, 'data'

result = get_yun_bi_market_info()

buy = float(result['last'])
print buy, 'buy', result
if abs( buy - data.get('last_buy', 0)) > app_config['buy_price_delta']:
  for k, v in app_config['email'].items():
    MailHelper.send_email(subject='the current buy price is %s' % buy,
      content='the bbc data is %s' % result, from_addr='18647246574@163.com',
      to_addr=v, nick_name='Herry')
data['last_buy'] = buy
with open(app_config['data_path'], 'w') as f:
  pickle.dump(data, f)

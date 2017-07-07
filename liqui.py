import hmac
import hashlib
from time import time
from urllib.parse import urlencode

import requests


class LiquiApiError(Exception):
    pass


class Liqui:

    def __init__(self, key, secret):
        self._key = key
        self._secret = secret

    def info(self):
        return self._v3('info')

    def ticker(self, pair):
        return self._v3('ticker', pair)

    def depth(self, pair):
        return self._v3('depth', pair)

    def trades(self, pair):
        return self._v3('trades', pair)

    def balances(self):
        funds = self.get_info()['funds']
        return {currency: balance for currency, balance in funds.items() if balance != 0}

    def get_info(self):
        return self._tapi(method='getInfo')

    def buy(self, pair, rate, amount):
        return self.trade(pair, 'buy', rate, amount)

    def sell(self, pair, rate, amount):
        return self.trade(pair, 'sell', rate, amount)

    def trade(self, pair, type, rate, amount):
        return self._tapi(method='Trade', pair=pair, type=type, rate=rate, amount=amount)

    def active_orders(self, pair=''):
        return self._tapi(method='ActiveOrders', pair=pair)

    def order_info(self, order_id):
        return self._tapi(method='OrderInfo', order_id=order_id)

    def cancel_order(self, order_id):
        return self._tapi(method='CancelOrder', order_id=order_id)

    def trade_history(self, **params):
        return self._tapi(method='TradeHistory', **params)

    def _v3(self, *args):
        url = 'https://api.liqui.io/api/3/' + '/'.join(args)
        r = requests.get(url)
        return r.json()

    def _tapi(self, **params):
        params.update(nonce=int(time()))
        headers = {'Key': self._key, 'Sign': self._sign(params)}
        resp = requests.post('https://api.liqui.io/tapi', data=params, headers=headers)
        data = resp.json()
        if 'error' in data:
            raise LiquiApiError(data['error'])
        return data.get('return', data)

    def _sign(self, data):
        if isinstance(data, dict):
            data = urlencode(data)
        return hmac.new(self._secret.encode(), data.encode(), hashlib.sha512).hexdigest()

# liqui

a minimal [liqui.io api](https://liqui.io/api) wrapper

## installation

```
pip install liqui
```

## usage

```python
from liqui import Liqui
from somewhere_else import key, secret

liqui = Liqui(key, secret)

# public api
liqui.info()
liqui.ticker('eth_btc')
liqui.depth('eth_btc')
liqui.trades('eth_btc')

# private api
liqui.get_info()
liqui.active_orders()
liqui.order_info(314159265)
liqui.cancel_order(271828182)
liqui.trade('eth_btc', 'sell', 0.13, 10)
liqui.trade_history()

# convenience methods
liqui.balances()
liqui.sell('eth_btc', 0.14, 10)
liqui.buy('eth_btc', 0.12, 10)
```


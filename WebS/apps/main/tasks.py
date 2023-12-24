import time

import ccxt
from django.apps import apps


def update_prices():
    Price = apps.get_model('main', 'Price')
    binance = ccxt.binance()

    while True:
        ticker = binance.fetch_ticker('BTC/USDT')
        btc_price = ticker['last']
        print(btc_price)

        try:
            price = Price.objects.get(currency='BTC')
            price.price = btc_price
            price.save()
        except Price.DoesNotExist:
            price = Price(currency='BTC', symbol='BTC/USDT', price=btc_price, price_in_usd=0)
            price.save()

        time.sleep(60)
from pricealert.celery import app
from api.models import PriceAlert
import requests
import json

COINGECKO_MARKETS_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"


@app.task
def price_check():
    """
    Price Check Celery task function.
    """

    print("Starting price_check ...")

    for price_alert in PriceAlert.objects.all():
        if price_alert.status == "CR":
            print(price_alert.symbol)
            try:
                res = requests.get(COINGECKO_MARKETS_URL)
                res_obj = json.loads(res.text)
                symbol_details = list(
                    filter(
                        lambda x: x["symbol"] == str(price_alert.symbol).lower(),
                        res_obj,
                    )
                )[0]
                current_price = symbol_details["current_price"]
                print(current_price)

                if (
                    price_alert.lower_higher == "l"
                    and current_price <= price_alert.price_limit
                ):
                    print(
                        f"{price_alert.symbol} has a new lower price - {current_price}"
                    )
                    price_alert.status = "TR"
                    price_alert.save()
                elif (
                    price_alert.lower_higher == "h"
                    and current_price >= price_alert.price_limit
                ):
                    print(
                        f"{price_alert.symbol} has a new higher price - {current_price}"
                    )
                    price_alert.status = "TR"
                    price_alert.save()
            except Exception as e:
                print(e)

    print("Ending price_check ...")

    return

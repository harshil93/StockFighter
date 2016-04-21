import StockFighter
import time
import os

account = ""
venue = ""
stock = ""
quantity = 10
direction = "buy"
orderType = "limit"

# set the environment variable properly
apikey = os.environ['stockfighterapikey']

client = StockFighter.StockFighter(account, apikey)

remaining = 100000

while remaining > 0:
    order = StockFighter.Order(account, venue, stock, 10000, quantity, direction, orderType)
    print client.placeOrder(order)
    remaining = remaining - quantity
    time.sleep(1)
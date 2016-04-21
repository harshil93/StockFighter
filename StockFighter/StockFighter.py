import urllib2
import json

class Order(object):
    def __init__(self,account, venue, stock, price, qty, direction, orderType):
        self.account = account
        self.venue = venue
        self.stock = stock
        self.price = price
        self.qty = qty
        self.direction = direction
        self.orderType = orderType


class StockFighter(object):
    
    def __init__(self, account, apikey):
        self.account = account
        self.apikey = apikey
        self.requestHeaders = {"X-Starfighter-Authorization": apikey, 
                               "content-type": "application/json",
                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/14.14316"
                               }

    def getOrderbook(self, venue, stock):
        apiUrl = "https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}".format(venue, stock)
        return self.doGetRequest(apiUrl)

    def getQuote(self, venue, stock):
        apiUrl = "https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/quote".format(venue, stock)
        return self.doGetRequest(apiUrl)

    def getStatusOfOrder(self, orderId, venue, stock):
        apiUrl = "https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/orders/{2}".format(venue, stock, orderId)
        return self.doGetRequest(apiUrl)

    def getStatusOfAllOrdersOfAStock(self, venue, account, stock):
        apiUrl = "https://api.stockfighter.io/ob/api/venues/{0}/accounts/{1}/stocks/{2}/orders".format(venue, account, stock)
        return self.doGetRequest(apiUrl)

    def placeOrder(self, order):
        apiUrl = "https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}/orders".format(order.venue, order.stock)
        return self.doPostRequest(apiUrl, order.__dict__)

    def doGetRequest(self, apiUrl):
        request = urllib2.Request(apiUrl, None, self.requestHeaders)
        return json.loads(urllib2.urlopen(request).read())
    
    def doPostRequest(self, apiUrl, data):
        request = urllib2.Request(apiUrl, json.dumps(data), self.requestHeaders)
        return json.loads(urllib2.urlopen(request).read())
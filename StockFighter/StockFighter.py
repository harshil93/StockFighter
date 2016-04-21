import urllib2
import json

class Order(object):
    def __init__(self,  venue, stock, price, qty, direction, orderType):
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
        self.requestHeaders = {"X-Starfighter-Authorization": apikey}

    def getOrderbook(self, venue, stock):
        apiUrl = "https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}".format(venue, stock)
        request = urllib2.Request(apiUrl, None, self.requestHeaders)
        response = urllib2.urlopen(request)
        return response.read()

    def placeOrder(self, order):
        apiUrl = "https://api.stockfighter.io/ob/api/venues/{0}/stocks/{1}".format(order.venue, order.stock)
        request = urllib2.Request(apiUrl, json.dumps(order.__dict__), self.requestHeaders)
        response = urllib2.urlopen(request)
        return response.read()


client = StockFighter(account, "<apikey>")

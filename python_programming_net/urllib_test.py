# Exercise 35
# urllib

import urllib.request
import urllib.parse


# .urlopen() must start with HTTP or HTTPS
# x = urllib.request.urlopen('https://www.google.com')
# print(x.read())

url = 'http://pythonprogramming.net'
# dictionary with values of an HTTP GET request. This is seen in the URL
# ex. pythonpg.net/?s=basic&submit=Search
values = {'s': 'basic',
          'submit': 'search'}
# Encodes our 'values' so that the web server can understand our GET/POST.
# HTTP requests must be encoded/decoded to send or read a GET or POST request.
# Analogous to JSON. ex: in the browser, '%20' the encode of a space.
# USE THIS METHOD - If you use hardcoding, Python will often throw errors.
data = urllib.parse.urlencode(values)

# Encodes using the 'utf-8' encoding standard which is like ASCII or unicode
# in that it uses symbols. This takes our GET/POST request(think like JSON,
# but for HTTP requests) and it encodes it so that it can be read (like ASCII)
# GET/POST must be parsed(unlike JSON) before we can work with them(like a CSV)
data = data.encode('utf-8')

# CREATES a GET request from Python 3, after all data has been encoded.
req = urllib.request.Request(url, data)
# SENDS our HTTP(GET) request and saves the response
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)

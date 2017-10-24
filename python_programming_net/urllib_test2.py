# This will fail because Google and many other don't like bots
# They want you to use their API (or be smart enough to work around it!)
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')

    print(x.read())

except Exception as e:
    # 403 Forbidden. Big surprise.
    print(str(e))

try:
    url = 'https://www.google.com/search?q=test'
    
    # HEADERS are all the data you send in when you visit a website:
    # Your IP, browser, operating system, version, user agent, etc
    # Python says the browser is 'python/urllib/python3.6' NOT SO SNEEKY
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url)
except Exception as e:

# Exercise 37
# Parsing Websites with regex and urllib

import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s': 'basics',
          'submit': 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# Used print to test code. Commenting out unless needed to test.
# print(respData)

# Searching for ANYTHING between <p> tags
# (.*?) is the pattern to search
# . "means any character except new line"
# * applies to the '.' and means "0 or more repetitions"
# ? applies to  '.*' and means "Match 0 or 1 repetitions of that"
#
# Also, remember to convert respData to a string or re.findall won't work!
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)

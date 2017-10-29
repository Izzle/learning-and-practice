# Web scraping and parsing with Beautfiul Soup 4 

import bs4 as bs
import urllib.request

# Sauce and Soup are standard variable names in the BS4 community (like foo bar)
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# Test print.
print(soup)  # Works! Prints HTML that looks like the source code
print(soup.title)         # <title> Greatest Page in USA</title>
print(soup.title.name)    # title
print(soup.title.string)  # returns a "navigable string" so child tags return 'NONE'
print(soup.title.text)    # returns unicode, meaning it returns EVERYTHING
print(soup.get_text())    # Gets text from all sorts of tags (span, code, div, etc)

print(soup.p)             # First 'p' element
print(soup.nav)           # First 'nav' element, LIKELY THE MAIN NAV OF THE PAGE!
# print(soup.find_all('p'))  # Finds ALL paragraph tags

for paragraph in soup.find_all('p'):
    print(paragraph)

'''Test Driven Development with Python

   TODO: Add a requirements file
         Required:
             -Python 3.6
             -Django
             -Selenium
             -Geckodriver
             -virtualenv
             -Firefox
         Recommended:
             -Git

'''

# Testing to see if we have Django installed,
# and that its ready for us to work with. 

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://localhost:8000')

assert 'Django' in browser.title
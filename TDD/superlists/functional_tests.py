'''Test Driven Development with Python

   TODO: Finish setup of Dev Environment on each platform
         that I work on.
         Windows:
             -Selenium
             -Geckodriver
             -virtualenv
         macOS:
             -Firefox
             -Geckodriver
         Linux(VMware):
             -Complete!
         Linux(proxmox):
             -verify virtualenvwrapper PATH
              (may need to reorder .bashrc entries)      

'''

# Testing to see if we have Django installed,
# and that its ready for us to work with. 

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUP(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Sally has heard about a cool new online to-do app.
        # She wants to check out its homepage
        self.browser.get('https://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # [...to be continued]


if __name__ == '__main__':
    unittest.main(warnings='ignore')


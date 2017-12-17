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
             -Complete!
'''

# Testing to see if we have Django installed,
# and that its ready for us to work with. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Sally has heard about a cool new online to-do app.
        # She wants to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        # (Sally's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Sally is
        # very methodical)
        self.fail('Finish the test!')

        # The page updates again, now shows both items on the list
        # [...]


if __name__ == '__main__':
    unittest.main(warnings='ignore')


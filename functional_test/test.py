import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase




class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text: str):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app she goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # she types "buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page updates, and now the page lists
        # "1: Buy peacock freathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # There is still a text box inviting her to add another item.
        # she enters "Use peacock feathers to make a fly" (Edith is 
        # very methodical)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.fail("Finish the test!!")

        # The page updates again, and now show both items on her list

        # Edith wonders wheter the site will remember her list. Then she
        # sees that the site generated a unique URL fo her -- there is some
        # explanatory text to that

        # she visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

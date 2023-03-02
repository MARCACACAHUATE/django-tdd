import unittest
from selenium import webdriver




class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app she goes
        # to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        self.fail("Finish the test")
        
        # She is invited to enter a to-do item straight away

        # she types "buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # when she hits enter, the page updates, and now the page lists
        # "1: Buy peacock freathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # she enters "Use peacock feathers to make a fly" (Edith is 
        # very methodical)

        # The page updates again, and now show both items on her list

        # Edith wonders wheter the site will remember her list. Then she
        # sees that the site generated a unique URL fo her -- there is some
        # explanatory text to that

        # she visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main()

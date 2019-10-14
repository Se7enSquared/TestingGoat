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
        # Edith has heard about a cool new online to-do
        # to check out is homepage
        self.browser.get('http://localhost:8000')

        # shet notices the page title and header mention
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1')
        self. assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types "buy peacock features" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page updates, and now the page lists
        # 1: Buy peacock feathers as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock features' for row in rows)
        )
        # there is still a textbox inviting her to add a new to-do
        # she enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')
        

        #The page updates again and now shows both items on her list


        # Will the site remember her list? She sees that the site has 
        # generated a unique url for her with some explanatory text


        # She visits that URL and her to-do list is still there


        # Satisfied, she closes the window

if __name__ == "__main__":
    unittest.main(warnings='ignore')
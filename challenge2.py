#!/usr/bin/env python3

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_challenge2(self):
        
        # Get the page.
        self.browser.get('https://www.copart.com/')
        # Search for exotic in the top search box.
        searchBox= self.browser.find_element_by_xpath('//*[@id="input-search"]')
        searchBox.send_keys('exotic' + Keys.RETURN)
        searchButton = self.browser.find_element_by_xpath('//*[@id="search-form"]/div/div[2]/button')
        searchButton.click()
        # Wait 10 sec for the page to load then search the page source for given string.
        wait = WebDriverWait(self.browser, 10)
        search_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[3]/div[3]/div/div[2]/table/tbody/tr[1]/td[1]')))
        self.assertIn("Porsche", self.browser.page_source, msg="Not found on page.")

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()


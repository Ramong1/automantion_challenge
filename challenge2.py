#!/usr/bin/env python3

import unittest
import time
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_challenge1(self):
        # Assumes you have made it past the captcha page.
        self.browser.get('https://www.copart.com/')
        self.browser.save_screenshot("screenshot-1.png")

        element = self.browser.find_element_by_xpath("//a[contains(text(),'Find Vehicles')]")
        element.click()

        vFinder = self.browser.find_element_by_xpath("//a[contains(@href, './vehicleFinder')]")
        vFinder.click()
        
        eFinder = self.browser.find_element_by_xpath("//span[contains(.,'Exotics')]")
        eFinder.click()
        time.sleep(6) # Wait a few seconds for cars to load on page.
        
        self.assertIn("Porsche", self.browser.page_source, msg="Not found on page.")

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()


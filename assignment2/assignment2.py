# install selenium wire for python using 'pip install selenium-wire' in the terminal
# download and place chromedriver in the same directory as this file to successfully run this test

import os
import time
import unittest
from seleniumwire import webdriver
from selenium.webdriver.common.by import By


class SeleniumTest(unittest.TestCase):
    
    def setUp(self):
        # finds the path for the current working directory and adds '/chromedriver' to the end of the path
        cwd = os.getcwd() + '/chromedriver'
        # creates a new instance of the chrome webdriver
        self.driver = webdriver.Chrome(executable_path=cwd)

    def test_basic_functionality(self):
        # goes to the url
        driver = self.driver
        driver.get("http://www.google.com")
        # finds the search box and enters 'selenium' into it
        search = driver.find_element(By.CLASS_NAME,'gLFyf')
        search.send_keys('selenium')
        search.submit()
        # assertion test in the event that the search does not render any results
        self.assertNotIn("No results found.", driver.page_source)

        # waits for the page to load by one second
        time.sleep(1)

        # finds the first few results and outputs them to the console
        print('\n')
        print("First few search result URLs:")
        results = driver.find_elements(By.XPATH, ".//*[@id='rso']//div//h3/a")
        for result in results:
            print(result.get_attribute("href"))
        print("______________________________________________________________")


    def test_api_call(self):
        driver = self.driver
        # all API calls made by the webdriver are recorded and can be retrieved using the following functions
        driver.get("http://www.google.com")
        assert driver.requests[0].response.status_code == 200 or driver.requests[0].response.status_code == 302, "status code is not 200 or 302"
        
        print('\n')
        print("API testing using Selenium")
        print("Format: method, host, status code, date and time")

        # gets the list of all API calls made by the webdriver and prints out the first 10 which include all get and post requests
        for each in driver.requests[:10]:
             if each.response:
                print(each.method, each.host, each.response.status_code, each.response.date, end='\n')
        print("______________________________________________________________")

def main():
    unittest.main()

if __name__ == "__main__":
    main()

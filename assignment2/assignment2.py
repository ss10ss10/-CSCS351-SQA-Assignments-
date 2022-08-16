# install selenium wire for python using 'pip install selenium-wire' in the terminal
# download and place chromedriver in the same directory as this file to successfully run this test

import os
import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By


def createDriver():
    # finds the path for the current working directory and adds '/chromedriver' to the end of the path
    cwd = os.getcwd() + '/chromedriver'

    # creates a new instance of the chrome webdriver
    driver = webdriver.Chrome(executable_path=cwd)

    return driver

def basicFunctionality(driver):
    # goes to the url
    driver.get('http://www.google.com')

    # finds the search box and enters 'selenium' into it
    search = driver.find_element(By.CLASS_NAME,'gLFyf')
    search.send_keys('selenium')
    search.submit()

    # waits for the page to load by one second
    time.sleep(1)

    # finds the first few results and outputs them to the console

    print("First few search result URLs:")
    results = driver.find_elements(By.XPATH, ".//*[@id='rso']//div//h3/a")
    for result in results:
        print(result.get_attribute("href"))
    print("______________________________________________________________")
    
    return driver

def apiTesting(driver):
    # all API calls made by the webdriver are recorded and can be retrieved using the following functions

    print("API testing using Selenium")
    print("Format: method, host, status code, date and time")

    # gets the list of all API calls made by the webdriver and prints out the first 10 which include all get and post requests
    for each in driver.requests[:10]:
         if each.response:
            print(each.method, each.host, each.response.status_code, each.response.date, end='\n')
    print("______________________________________________________________")
    return driver

def main():
    
    driver = createDriver()
    driver = basicFunctionality(driver)
    driver = apiTesting(driver)
    time.sleep(1)
    driver.quit()

if __name__ == "__main__":
    main()
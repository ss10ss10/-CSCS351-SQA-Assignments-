# install selenium for python using 'pip install selenium' in the terminal
# download and place chromedriver in the same directory as this file to successfully run this test

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# finds the path for the current working directory and adds '/chromedriver' to the end of the path
cwd = os.getcwd() + '/chromedriver'

# creates a new instance of the chrome webdriver
driver = webdriver.Chrome(executable_path=cwd)

# goes to the url
driver.get('http://www.google.com')

# finds the search box and enters 'selenium' into it
search = driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('selenium')
search.submit()

# waits for the page to load by one second
time.sleep(1)

# finds the first few results and outputs them to the console
results = driver.find_elements(By.XPATH, ".//*[@id='rso']//div//h3/a")
for result in results:
    print(result.get_attribute("href"))

time.sleep(1)
driver.quit()

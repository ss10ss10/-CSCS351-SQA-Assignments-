# Muhammad Sulaiman Sultan 231453415

## Objective

The objective of this task is to demonstrate API testing using ```Selenium``` for ```Python```.

### Dependencies
- ```selenium-wire``` install seleniumwire using "pip install selenium-wire"
- ```chromedriver``` chromedriver executable needs to be in the current working directory where the python script is

### Test Cases for Basic Functionality
- ```get``` opens an instance of the provided URL (in this case 'google.com')
- ```find_element``` finds the search box by class_name
- ```send_keys``` puts the string to be searched (in this case 'selenium') in the search box
- ```submit``` sends the query back to the server which displays the result in the chromedriver instance we opened previously
- ```find_elements``` finds the first few search results and gets their urls and displays them to the console
- ```close``` closes the chromedriver instance that carried all of these tasks out
- ```assertNotIn``` tests whether the the search yielded any results or not

# API Testing
### Using ```webdriver.requests``` to list the response for each call
- ```method``` shows whether it was a get or post response
- ```host``` shows the host these responses were from
- ```status_code``` shows the response status code
- ```date``` shows the date and time for the specific response
- ```assert``` checks if the returned response status code is 200 or 302

### Console output
![image](https://user-images.githubusercontent.com/64100540/184954039-d1277da7-d528-4360-8370-4b56f113f3ee.png)

### Chromedriver outputs
![Screenshot from 2022-08-16 23-38-48](https://user-images.githubusercontent.com/64100540/184954245-b1da6b03-b90f-495d-a144-17a0025b3f85.png)
![Screenshot from 2022-08-16 23-38-51](https://user-images.githubusercontent.com/64100540/184954266-e858db0d-b134-4668-8c22-3cad46bc6cbc.png)







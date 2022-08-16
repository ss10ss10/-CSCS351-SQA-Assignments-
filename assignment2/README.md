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

### API Testing
# Using ```webdriver.requests``` to list the response for each call
- ```method``` shows whether it was a get or post response
- ```host``` shows the host these responses were from
- ```status_code``` shows the response status code
- ```date``` shows the date and time for the specific response

### Console output
![image](https://user-images.githubusercontent.com/64100540/184938143-a3d8d969-f442-4c22-95a0-62733ad0874a.png)


### Chromedriver outputs
![Screenshot from 2022-08-16 22-09-04](https://user-images.githubusercontent.com/64100540/184938246-47ee3f33-8a92-49ae-84d6-3b78ca3f870b.png)
![Screenshot from 2022-08-16 22-09-08](https://user-images.githubusercontent.com/64100540/184938492-ff1caf3f-3d1d-421b-ae44-8e7f7375cab3.png)





# Python Selenium Automation Testing for Automation Practice Website #

### Introduction ###

This repository contains automated test scripts written in Python using Selenium WebDriver for testing the [Automation Testing](https://practice.automationtesting.in/). The main focus of the tests is on the **Shop** category.

## Getting Started ##
### Prerequisites ###

To run these tests locally, you need to have the following installed:
* Python
* Selenium WebDriver
* Web browser (Chrome)
* pytest-html

Imported Packages:
* pytest
* configparser
* re
* time
* logging

### Running the Tests ###
To run the tests, execute the following command:
```python
pytest testcases/test_homepage.py -s -v --html=./Reports/report1.html
```

### Test Cases ### 
Test cases covered are from the **Shop** category test cases only [/test-cases](https://practice.automationtesting.in/test-cases/)
1. Shop-Filter By Price Functionality -- **test_001**
2. Shop-Product Categories Functionality -- **test_002**
3. Shop-Default Sorting Functionality -- **test_003**
4. Shop-Default Sorting Functionality -- **test_004**
5. Shop-Default Sorting Functionality -- **test_005**
6. Shop-Default Sorting Functionality -- **test_006**
7. Shop-Default Sorting Functionality -- **test_007**
8. Shop-Sale Functionality -- **test_008**
9. Shop-Add to Basket-View Basket Functionality -- **test_009**
10. Shop-Add to Basket-View Basket through Item link -- **test_010**
11. Shop-Add to Basket-View Basket-Tax Functionality -- **test_011**

### Reports ### 
After the test cases are completed, the reports are generated in the Reports folder with .html tag



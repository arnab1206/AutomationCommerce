from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


# pytest testcases/test_homepage.py -s -v --html=./Reports/reportslatest.html
#pytest -s -v -n=3 --html=C:\Users\USER\PycharmProjects\ArnabNew\Reports\report.html testcases/test_homepage.py --browser chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# creating class to add user
class AddUser:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #setting first name
    def setfname(self,fname):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_first_name']")))
        elem.send_keys(fname)

    # setting last name
    def setlname(self, lname):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_last_name']")))
        elem.send_keys(lname)

    # setting email
    def setemail(self, email):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_email']")))
        elem.send_keys(email)

    # setting phone number
    def setphone(self, phone):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_phone']")))
        elem.send_keys(phone)

    # setting country dropdown click
    def countrydrpdwn(self):
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='s2id_billing_country']")))
        elem.click()

    # setting list to be clickable from country dropdown
    def countrydrpdwnselect(self, index):
        xpath = "//*[@id='select2-results-1']/li[{}]".format(index)
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elem.click()

    def get_selected_country_value(self):
        country_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='select2-chosen-1']")))
        return country_element.text

    # setting address line 1
    def setadrs1(self, adrs1):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_address_1']")))
        elem.send_keys(adrs1)

    # setting address line 2
    def setadrs2(self, adrs2):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_address_2']")))
        elem.send_keys(adrs2)

    # setting town/city
    def settowncity(self, towncity):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_city']")))
        elem.send_keys(towncity)

    # setting state/county
    def setstatecounty(self, statecounty):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_state']")))
        elem.send_keys(statecounty)

    # setting postcode
    def setpostcodeid(self, postcodeid):
        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='billing_postcode']")))
        elem.send_keys(postcodeid)

    # setting click on cod
    def clickcod(self):
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='payment_method_cod']")))
        elem.click()

    # setting click on place of order
    def clickplaceorder(self):
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='place_order']")))
        elem.click()

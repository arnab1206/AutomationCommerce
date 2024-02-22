import time
import re
from selenium.webdriver.common.by import By

from utilities.customerlogger import LogGen
from utilities.readproperties import ReadConfig

from pages.HomePage import HomePage
from pages.HomePage import SliderAutomation
from pages.HomePage import DropdownAutomation
from pages.AddUser import AddUser

class Test_01_ShopTC:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_001(self, setup):
        self.logger.info("*************** Test_01 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()
        self.slider_automator = SliderAutomation(self.driver)
        self.slider_automator.move_slider("//*[@id='woocommerce_price_filter-2']/form/div/div[1]/span[2]", -23, 0)
        self.hp.filter()

        self.logger.info("*************** Showing the filtered product names *****************")

        # Creating an empty string to verify the test case
        filtered_product_names = []
        expected_string = "Android Quick Start Guide, Functional Programming in JS, HTML5 Forms, HTML5 WebApp Develpment, JS Data Structures and Algorithm, Mastering JavaScript, Thinking in HTML"

        # Print the titles of filtered products
        filtered_products = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul//a[1]/h3")

        for product in filtered_products:
            filtered_product_names.append(product.text)
        print(", ".join(filtered_product_names))

        for product in filtered_products:
            assert product.text in expected_string, f"Expected '{product.text}' to be in '{expected_string}'"

        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_002(self, setup):
        self.logger.info("*************** Test_02 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()

        self.hp.android()
        self.logger.info("*************** Showing the filtered product names as per Product Category*****************")

        filtered_product_names = []
        expected_string = "Android Quick Start Guide"

        # Print the titles of filtered products
        filtered_products = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul//a[1]/h3")

        for product in filtered_products:
            filtered_product_names.append(product.text)
            print(", ".join(filtered_product_names))

        for product in filtered_products:
            assert product.text in expected_string, f"Expected '{product.text}' to be in '{expected_string}'"

        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_003(self, setup):
        self.logger.info("*************** Test_03 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()

        self.da = DropdownAutomation(self.driver)
        self.da.move_dropdown("Sort by popularity")
        self.logger.info("*************** Sorting by popularity *****************")

        # filtered_product_names = []
        expected_string = "Android Quick Start Guide"

        # Print the titles of filtered products
        filtered_products = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul//a[1]/h3")

        first_product_text = filtered_products[0].text
        print(first_product_text)
        assert first_product_text == expected_string

        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_004(self, setup):
        self.logger.info("*************** Test_04 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()

        self.da = DropdownAutomation(self.driver)
        self.da.move_dropdown("Sort by average rating")
        self.logger.info("*************** Sorting by average rating *****************")

        filtered_product_names = []
        expected_string = "Selenium Ruby"

        # Print the titles of filtered products
        filtered_products = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul//a[1]/h3")

        first_product_text = filtered_products[0].text
        print(first_product_text)
        assert first_product_text == expected_string

        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_005(self, setup):
        self.logger.info("*************** Test_05 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()

        self.da = DropdownAutomation(self.driver)
        self.da.move_dropdown("Sort by newness")
        self.logger.info("*************** Sorting by Newness *****************")

        filtered_product_names = []
        expected_string = "HTML5 WebApp Develpment"

        # Print the titles of filtered products
        filtered_products = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul//a[1]/h3")

        first_product_text = filtered_products[0].text
        print(first_product_text)
        assert first_product_text == expected_string

        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_006(self, setup):
        self.logger.info("*************** Test_06 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()

        self.da = DropdownAutomation(self.driver)
        self.da.move_dropdown("Sort by price: low to high")
        self.logger.info("*************** Sorting by low to high *****************")

        filtered_product_names = []
        expected_string = "JS Data Structures and Algorithm"

        # Print the titles of filtered products
        filtered_products = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul//a[1]/h3")

        first_product_text = filtered_products[0].text
        print(first_product_text)
        assert first_product_text == expected_string

        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_007(self, setup):
        self.logger.info("*************** Test_07 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()

        self.da = DropdownAutomation(self.driver)
        self.da.move_dropdown("Sort by price: high to low")
        self.logger.info("*************** Sorting by high to low *****************")

        filtered_product_names = []
        expected_string = "Selenium Ruby"

        # Print the titles of filtered products
        filtered_products = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul//a[1]/h3")

        first_product_text = filtered_products[0].text
        print(first_product_text)
        assert first_product_text == expected_string

        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_009(self, setup):
        self.logger.info("*************** Test_09 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()

        self.logger.info("*************** Checking the Sale Products prices *****************")
        sale_products = self.driver.find_elements(By.XPATH, "//*[@class ='onsale']")
        for index, product in enumerate(sale_products, start=1):
            # Click on the sale product
            product.click()
            time.sleep(2)
            # Getting the price of the product from the next page
            element_name = self.driver.find_element(By.XPATH, "//*[@class='product_title entry-title']")
            old_price_element = self.driver.find_element(By.XPATH,
                                                         "//p/del/span[@class='woocommerce-Price-amount amount']")
            new_price_element = self.driver.find_element(By.XPATH,
                                                         "//p/ins/span[@class='woocommerce-Price-amount amount']")
            price_old = old_price_element.text
            price_new = new_price_element.text
            element = element_name.text
            print(f"Price of Sale Product {index}+{element}: old price {price_old} new price {price_new}")
            self.driver.back()
        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_010(self, setup):
        self.logger.info("*************** Test_10 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()
        time.sleep(2)

        self.hp.clickbook("//*[@id='content']/ul/li[2]/a[2]")
        time.sleep(2)

        self.hp.viewbasket("//*[@id='content']/ul/li[2]/a[3]")
        self.hp.proceedtocheckout()

        self.logger.info("*************** Add customer details *****************")
        self.adduser = AddUser(self.driver)
        self.adduser.setfname("test")
        self.adduser.setlname("xyz")
        self.adduser.setemail("testxyz@gmail.com")
        self.adduser.setphone("0123456")
        self.adduser.countrydrpdwn()
        self.adduser.countrydrpdwnselect(179)
        time.sleep(2)
        self.adduser.setadrs1("abc")
        self.adduser.setadrs2("def")
        self.adduser.settowncity("towntest")
        self.adduser.setstatecounty("statetest")
        self.adduser.setpostcodeid("01234")
        self.adduser.clickcod()
        self.adduser.clickplaceorder()
        time.sleep(2)

        confirm_title = self.driver.find_element(By.CLASS_NAME, "woocommerce-thankyou-order-received")
        confirm_title_text = confirm_title.text
        if confirm_title_text == "Thank you. Your order has been received.":
            self.driver.close()
            print({confirm_title_text})
            assert True
        else:
            self.driver.close()
            assert False
        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_011(self, setup):
        self.logger.info("*************** Test_11 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()
        time.sleep(2)

        self.hp.clickbook("//*[@id='content']/ul/li[2]/a[2]")
        time.sleep(2)
        self.hp.menubasket("//*[@id='wpmenucartli']")
        self.hp.proceedtocheckout()

        self.logger.info("*************** Add customer details *****************")
        self.adduser = AddUser(self.driver)
        self.adduser.setfname("test")
        self.adduser.setlname("xyz")
        self.adduser.setemail("testxyz@gmail.com")
        self.adduser.setphone("0123456")
        self.adduser.countrydrpdwn()
        self.adduser.countrydrpdwnselect(179)
        time.sleep(2)
        self.adduser.setadrs1("abc")
        self.adduser.setadrs2("def")
        self.adduser.settowncity("towntest")
        self.adduser.setstatecounty("statetest")
        self.adduser.setpostcodeid("01234")
        self.adduser.clickcod()
        self.adduser.clickplaceorder()
        time.sleep(2)

        confirm_title = self.driver.find_element(By.CLASS_NAME, "woocommerce-thankyou-order-received")
        confirm_title_text = confirm_title.text
        if confirm_title_text == "Thank you. Your order has been received.":
            self.driver.close()
            print({confirm_title_text})
            assert True
        else:
            self.driver.close()
            assert False
        self.logger.info("*************** Test Case Passed *****************")
        self.driver.quit()

    def test_012(self, setup):
        self.logger.info("*************** Test_12 *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.logger.info("*************** Rejecting the consent popup *****************")
        self.hp.consentReject()
        self.logger.info("*************** Clicking into shop icon *****************")
        self.hp.clickShop()
        time.sleep(2)
        self.hp.clickbook("//*[@id='content']/ul/li[2]/a[2]")
        time.sleep(2)
        self.hp.menubasket("//*[@id='wpmenucartli']")
        self.hp.proceedtocheckout()
        self.adduser = AddUser(self.driver)
        self.adduser.countrydrpdwn()
        time.sleep(2)
        self.adduser.countrydrpdwnselect(103)
        time.sleep(2)

        # Get the tax and subtotal values
        tax_value = self.driver.find_element(By.XPATH, "//*[@id='order_review']/table/tfoot/tr[2]/td/span").text
        subtotal_value = self.driver.find_element(By.XPATH, "//*[@id='order_review']/table/tfoot/tr[1]/td/span").text

        # Convert values to float
        tax_value = float(re.findall(r'\d+\.\d+', tax_value)[0])
        subtotal_value = float(re.findall(r'\d+\.\d+', subtotal_value)[0])

        # Check if the tax rate for the selected country is correct
        if self.adduser.get_selected_country_value() == "India":
            expected_tax_rate = subtotal_value * 0.02  # Tax rate for Indian is 2%
            print({expected_tax_rate})
            assert True
            self.logger.info("*************** Country is India *****************")
        else:
            expected_tax_rate = subtotal_value * 0.05  # Tax rate for abroad is 5%
            print({expected_tax_rate})
            self.logger.info("*************** Country is not India *****************")
            assert False

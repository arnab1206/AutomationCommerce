from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():

    SHOP_LINK = (By.LINK_TEXT, "https://practice.automationtesting.in/shop/")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Initialize WebDriverWait with a timeout of 10 seconds

    def clickShop(self):
        shop_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-40']/a")))
        shop_link.click()
    def consentReject(self):
        consent_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[2]/p")))
        consent_button.click()
    def filter(self):
        filter_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='woocommerce_price_filter-2']/form/div/div[2]/button")))
        filter_button.click()

    def android(self):
        android_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='woocommerce_product_categories-2']/ul/li[1]/a")))
        android_link.click()

    def clickbook(self, book_xpath):
        book_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, book_xpath)))
        book_link.click()

    def viewbasket(self, book_xpath):
        basket_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, book_xpath)))
        basket_link.click()

    def proceedtocheckout(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='checkout-button button alt wc-forward']")))
        checkout_button.click()

    def menubasket(self, book_xpath):
        menu_basket_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, book_xpath)))
        menu_basket_link.click()

class SliderAutomation():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Initialize WebDriverWait with a timeout of 10 seconds

    def move_slider(self, slider_xpath, offset_x, offset_y):
        elem1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, slider_xpath)))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(elem1, offset_x, offset_y)
        action.perform()

class DropdownAutomation():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Initialize WebDriverWait with a timeout of 10 seconds

    def move_dropdown(self, element):
        elem2 = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "orderby")))
        Select(elem2).select_by_visible_text(element)




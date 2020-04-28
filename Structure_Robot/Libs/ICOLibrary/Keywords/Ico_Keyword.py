from selenium import webdriver
from selenium.webdriver.common.by import By
from SeleniumLibrary.base import keyword, LibraryComponent
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class TableKeyword(LibraryComponent):

    @keyword
    def open_browser_test(self, url, browser):
        try:
            if browser == 'Chrome':
                print("Open with browser: ", browser)
                print("Link URL: ", url)
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Firefox()

            # Navigate to the application home page
            driver.get(url)

            driver.maximize_window()
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def click_element_page(self, locator):
        """Click element on page"""
        try:
            self.find_element(locator).click()
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def click_element_with_class_name(self, locator):
        """Click element on page"""
        try:
            self.driver.find_element_by_class_name(locator).click()
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def get_title_page(self):
        """Verify title on page current"""
        try:
            if self.driver.title != "":
                return self.driver.title
            else:
                raise ElementNotVisibleException
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def input_text_element(self, locator, text_input):
        """Input text on page"""
        try:
            element = self.driver.find_element_by_name(locator)
            element.send_keys(text_input)
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def input_text_element_with_id(self, locator, text_input):
        """Input text on page"""
        try:
            element = self.driver.find_element_by_id(locator)
            element.send_keys(text_input)
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def get_text_on_page(self, locator):
        """Get text on locator"""
        try:
            element = self.driver.find_element_by_id(locator).text
            print(element)
            return element
        except ElementNotVisibleException as err:
            print(str(err))

    @keyword
    def wait_element_until_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, float(timeout))
        men_menu = wait.until(ec.visibility_of_element_located((By.NAME, locator)))
        ActionChains(self.driver).move_to_element(men_menu).perform()

    @keyword
    def wait_page_load(self, locator, timeout):
        try:
            element_present = ec.presence_of_element_located((By.ID, locator))
            WebDriverWait(self.driver, float(timeout)).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

    # @keyword
    # def get_locator(self, locator):
    #     try:
    #         if self.driver.find_element_by_id(locator).is_displayed():
    #             return
    #     except ElementNotVisibleException as err:
    #         print(str(err))
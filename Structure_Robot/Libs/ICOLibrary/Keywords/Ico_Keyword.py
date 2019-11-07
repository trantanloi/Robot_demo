from SeleniumLibrary.base import keyword, LibraryComponent
from selenium.common.exceptions import ElementNotVisibleException


class TableKeyword(LibraryComponent):

    @keyword
    def click_element_page(self, locator):
        """Click element on page"""
        try:
            self.find_element(locator).click()
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
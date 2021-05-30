from selenium.webdriver.remote.webdriver import WebDriver

import pages.book_details_page
from utils import wait_for_element, clear_input


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_product_names(self):
        wait_for_element(self.driver, '.product-name', 10)
        products = self.driver.find_elements_by_css_selector('.product-name')

        return [x.text for x in products]

    def submit_expecting_success(self):
        self._submit_btn()
        return pages.book_details_page.BookDetails(self.driver)

    def _submit_btn(self):
        submit_btn = self.driver.find_element_by_css_selector('button[type=submit]')
        submit_btn.click()

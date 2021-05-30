from selenium.webdriver.remote.webdriver import WebDriver

from pages.cart_page import CartPage
from utils import wait_for_element


class BookDetails:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_names(self):
        wait_for_element(self.driver, 'h1', 5)
        names = self.driver.find_elements_by_css_selector('h1')

        return [x.text for x in names]

    def add_book_to_cart(self):
        wait_for_element(self.driver, '#add-to-cart-button-13', 10)
        add_to_card = self.driver.find_element_by_css_selector('#add-to-cart-button-13')

        add_to_card.click()

    def open_cart_page(self):
        wait_for_element(self.driver, '#topcartlink', timeout=5)
        cart_link_element = self.driver.find_element_by_css_selector('#topcartlink')

        cart_link_element.click()

        return CartPage(self.driver)

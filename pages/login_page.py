from selenium.webdriver.remote.webdriver import WebDriver

from pages.book_page import BookPage
from utils import wait_for_element, clear_input


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_email(self, email):
        input_email = self.driver.find_element_by_name("Email")
        input_email.send_keys(email)

    def input_password(self, password):
        input_password = self.driver.find_element_by_name("Password")
        clear_input(input_password)
        input_password.send_keys(password)

    def submit_expecting_success(self, url):
        self._submit_btn()

        book_link = '//a[@href="' + url + '"]'

        wait_for_element(self.driver, book_link, timeout=1)
        book_link_element = self.driver.find_element_by_xpath(book_link)

        book_link_element.click()

        return BookPage(self.driver)

    def submit_expecting_failure(self):
        self._submit_btn()

    def get_errors(self):
        error_class = '.validation-summary-errors'
        wait_for_element(self.driver, error_class, timeout=2)
        errors_elements = self.driver.find_elements_by_css_selector(error_class)

        return [x.text for x in errors_elements]

    def _submit_btn(self):
        submit_btn = self.driver.find_element_by_css_selector('input.login-button')
        submit_btn.submit()

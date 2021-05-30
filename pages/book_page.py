from selenium.webdriver.remote.webdriver import WebDriver

from pages.book_details_page import BookDetails
from utils import wait_for_element


class BookPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_book(self, url):
        book_link = '//a[@href="' + url + '"]'

        wait_for_element(self.driver, book_link, timeout=1)
        link = self.driver.find_element_by_link_text("Computing and Internet")
        link.click()

        #wait_for_element(self.driver, book_link, timeout=1)
        #book_link_element = self.driver.find_element_by_xpath(book_link)
        #book_link_element.click()

        return BookDetails(self.driver)


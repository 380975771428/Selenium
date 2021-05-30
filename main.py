from selenium import webdriver

from pages.login_page import LoginPage

URL = 'http://demowebshop.tricentis.com/login'

VALID_BOOK_NAME = "Computing and Internet"
INVALID_BOOK_NAME = "Unknown"


def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)


def run():
    driver = get_web_driver()
    driver.get(URL)

    # login tests
    login_page = LoginPage(driver)

    login_page.input_email("nazarzubriy@test.com")
    login_page.input_password("qwertyError")
    login_page.submit_expecting_failure()

    errors = login_page.get_errors()
    assert len(errors) > 0

    login_page.input_password("qwerty")

    # book tests
    books_page = login_page.submit_expecting_success('/books')

    # job details tests
    book_details_page = books_page.open_book('/computing-and-internet')

    book_names = book_details_page.get_names()

    assert VALID_BOOK_NAME in book_names
    assert INVALID_BOOK_NAME not in book_names

    book_details_page.add_book_to_cart()

    # cart page tests
    cart_page = book_details_page.open_cart_page()
    product_names = cart_page.get_product_names()

    assert VALID_BOOK_NAME in product_names
    assert INVALID_BOOK_NAME not in product_names

    print('All tests were passed successfully')
    input()


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print('An exception was thrown during running tests: ' + str(e))

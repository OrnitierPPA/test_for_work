import random

from .locators import SearchPageLocators

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def random_pass_mail(num):
    string = ''
    for i in range(num):
        string = string + random.choice(list('ABCDEFGHIGKLMNOPQRSTUVYXWZabcdefghigklmnopqrstuvyxwz1234567890'))
    return string


def copy_link(link_file):
    with open(link_file, "r") as file:
        link = file.read()
        print(link)
    return link


class BasePage:
    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def element_is_not_available(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def refresh_page(self):
        self.browser.refresh()

    def search_in_browser(self, request):
        self.browser.find_element(*SearchPageLocators.SEARCH_LINE).send_keys(request, Keys.ENTER)

    def open_in_new_window(self, link):
        first_window = self.browser.window_handles[0]
        self.browser.execute_script(f"window.open('{link}')")
        new_window = self.browser.window_handles[1]
        self.browser.close()
        self.browser.switch_to.window(new_window)

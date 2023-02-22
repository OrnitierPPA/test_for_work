from .base_page import BasePage, random_pass_mail
from .locators import SearchPageLocators, LogInPageLocators


class LoginPage(BasePage):
    def open_login_page(self):
        print(self.browser.find_element(*SearchPageLocators.RESULT_STATS).text)
        assert self.browser.find_element(*SearchPageLocators.LINK).get_attribute('href') == \
               'https://portal.sovcombank.ru/', "Предполагаемый результат не был найден"
        link = self.browser.find_element(*SearchPageLocators.LINK).get_attribute('href')
        self.open_in_new_window(link)

    def login_in_account(self):
        assert self.is_element_present(*LogInPageLocators.LOGIN_LINE), "Строка логина не найдена"
        assert self.is_element_present(*LogInPageLocators.PASSWORD_LINE), "Строка пароля не найдена"
        assert self.is_element_present(*LogInPageLocators.BUTTON), "Кнопка входа не найдена"
        self.browser.find_element(*LogInPageLocators.LOGIN_LINE).send_keys(random_pass_mail(8))
        self.browser.find_element(*LogInPageLocators.PASSWORD_LINE).send_keys(random_pass_mail(15))
        self.browser.find_element(*LogInPageLocators.BUTTON).click()

        if self.is_element_present(*LogInPageLocators.ERROR):
            print(self.browser.find_element(*LogInPageLocators.ERROR).text)
            assert self.element_is_not_available(*LogInPageLocators.BUTTON), "Кнопка кликабельна"

    def login_lines_blank(self):
        assert len(self.browser.find_element(*LogInPageLocators.LOGIN_LINE).get_attribute("value")) == 0, \
            "Поле логина не пустое"
        assert len(self.browser.find_element(*LogInPageLocators.PASSWORD_LINE).get_attribute("value")) == 0, \
            "Поле пароля не пустое"


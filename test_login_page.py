import pytest

from pages.base_page import copy_link
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_open_login_page(browser):
    """
    Тест на проверку возможности найти сайт в поиске и перейти на его страницу
    """
    link = copy_link('url.txt')
    page = LoginPage(browser, link)
    page.open()
    page.search_in_browser('Портал совкомбанк')
    page.open_login_page()


@pytest.mark.smokeg
def test_error_with_incorrect_data(browser):
    """
    Тест на проверку ошибки, при вводе неверных данных
    """
    link = "https://portal.sovcombank.ru/login"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_account()


def test_lines_are_empty_after_the_update(browser):
    """
    Тест на проверку очистки полей после обновления страницы
    """
    link = "https://portal.sovcombank.ru/login"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_account()
    page.refresh_page()
    page.login_lines_blank()






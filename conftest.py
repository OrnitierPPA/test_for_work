import pytest
import time

from datetime import datetime
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstar browser..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    now = datetime.now()
    browser.save_screenshot("%d_%d_%d_screen.png" % (now.hour, now.minute, now.second))
    print("\nquit browser..")
    browser.quit()


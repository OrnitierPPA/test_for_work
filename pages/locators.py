from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_LINE = (By.CSS_SELECTOR, "input.gLFyf")
    LINK = (By.CSS_SELECTOR, "div.yuRUbf > a")
    RESULT_STATS = (By.XPATH, "//div[@class='LHJvCe']/div[@id='result-stats']")


class LogInPageLocators:
    LOGIN_LINE = (By.XPATH, "//div[@class='auth-form__field']/input[@id='auth-form-email']")
    PASSWORD_LINE = (By.XPATH, "//div[@class='auth-form__field']/input[@id='auth-form-password']")
    ERROR = (By.CSS_SELECTOR, "div.error-text > span:nth-child(2)")
    BUTTON = (By.CLASS_NAME, "auth__btn")

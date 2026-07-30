import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LogoutLocators

class TestLogout:
    def test_logout_from_personal_account(self, authorized_main_page, driver):  # проверяем выход по кнопке «Выйти»
        authorized_main_page.find_element(*LogoutLocators.PERSONAL_ACCOUNT_LINK).click()   # нажимаем личный кабинет
        authorized_main_page.find_element(*LogoutLocators.LOGOUT_BUTTON).click()            # нажимаем выход

        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))
        assert authorized_main_page.current_url == "https://stellarburgers.education-services.ru/login"
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LogoutLocators
from data import LOGIN_PAGE_URL


class TestLogout:
    def test_logout_from_personal_account(self, authorized_main_page, driver):  # проверяем выход по кнопке «Выйти»
        authorized_main_page.find_element(*LogoutLocators.PERSONAL_ACCOUNT_LINK).click()   # нажимаем личный кабинет
        authorized_main_page.find_element(*LogoutLocators.LOGOUT_BUTTON).click()            # нажимаем выход

        wait = WebDriverWait(driver, 20)
        wait.until(EC.url_to_be(LOGIN_PAGE_URL))
        assert authorized_main_page.current_url == LOGIN_PAGE_URL
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators  
from data import LOGIN_PAGE_URL

class TestLogout:
    def test_logout_from_personal_account(self, authorized_main_page):
        driver = authorized_main_page 
        wait = WebDriverWait(driver, 20)

        # Нажимаем «Личный кабинет»
        account_link = wait.until(EC.element_to_be_clickable(AuthLocators.PERSONAL_ACCOUNT_LINK))
        account_link.click()

        # Нажимаем «Выход»
        logout_btn = wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON))
        logout_btn.click()

        # Проверяем, что попали на страницу входа
        wait.until(EC.url_to_be(LOGIN_PAGE_URL))
        assert driver.current_url == LOGIN_PAGE_URL
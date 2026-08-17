import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginAccountLocators


class TestLoginAccount:
    def test_login_account(self, main_page, existing_user):
        
        main_page.find_element(*LoginAccountLocators.PERSONAL_ACCOUNT_LINK).click() # нажимаем на кнопку "Личный Кабинет" на главной
        
        main_page.find_element(*LoginAccountLocators.EMAIL_INPUT_LOGIN).send_keys(existing_user["email"]) # вводим email
        
        main_page.find_element(*LoginAccountLocators.INP_PAS).send_keys(existing_user["password"]) # вводим пароль
        
        main_page.find_element(*LoginAccountLocators.SUBMIT_LOGIN).click() # нажимаем кнопку "Войти"
        
        # ожидаем появления кнопки "Оформить заказ" (явное ожидание)
        wait = WebDriverWait(main_page, 10)
        order_button = wait.until(EC.visibility_of_element_located(LoginAccountLocators.TITLE_ORDER))
        assert order_button.is_displayed()
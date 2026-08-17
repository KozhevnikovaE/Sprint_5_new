import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators

class TestLogin:
    @staticmethod
    def is_order_button_visible(driver, timeout=10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located(LoginLocators.ORDER_BUTTON))

    def test_login_main_button(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        assert self.is_order_button_visible(main_page), "Кнопка «Оформить заказ» не отображается после входа"

    def test_login_account_icon(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.ACCOUNT_LINK).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        assert self.is_order_button_visible(main_page), "Кнопка «Оформить заказ» не отображается после входа"

    def test_login_from_registration_page(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()
        main_page.find_element(*LoginLocators.REGISTER_LINK).click()
        main_page.find_element(*LoginLocators.LOGIN_LINK_REGISTER).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        assert self.is_order_button_visible(main_page), "Кнопка «Оформить заказ» не отображается после входа"

    def test_login_from_password_recovery(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()
        main_page.find_element(*LoginLocators.RECOVER_PASSWORD_LINK).click()
        main_page.find_element(*LoginLocators.LOGIN_LINK_RECOVER).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        assert self.is_order_button_visible(main_page), "Кнопка «Оформить заказ» не отображается после входа"

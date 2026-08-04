import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators

class TestLogin:
    @staticmethod
    def _wait_for_order_button(driver, timeout=10):
        """Ждёт появления кнопки в DOM и возвращает элемент."""
        wait = WebDriverWait(driver, timeout)
        # presence быстрее и стабильнее для автотестов
        return wait.until(EC.presence_of_element_located(LoginLocators.ORDER_BUTTON))

    def test_login_main_button(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        order_button = self._wait_for_order_button(main_page)
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отображается после входа"

    def test_login_account_icon(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.ACCOUNT_LINK).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        order_button = self._wait_for_order_button(main_page)
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отображается после входа"

    def test_login_from_registration_page(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()
        main_page.find_element(*LoginLocators.REGISTER_LINK).click()
        main_page.find_element(*LoginLocators.LOGIN_LINK_REGISTER).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        order_button = self._wait_for_order_button(main_page)
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отображается после входа"

    def test_login_from_password_recovery(self, main_page, existing_user):
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()
        main_page.find_element(*LoginLocators.RECOVER_PASSWORD_LINK).click()
        main_page.find_element(*LoginLocators.LOGIN_LINK_RECOVER).click()
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()

        order_button = self._wait_for_order_button(main_page, timeout=15)  # чуть дольше, если форма сложная
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отображается после входа"

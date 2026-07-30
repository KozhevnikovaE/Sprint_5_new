import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators

class TestLogin:
    def test_login_main_button(self, main_page, existing_user):  # проверяем вход по кнопке «Войти в аккаунт» на главной
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()   # нажимаем кнопку войти в аккаунт
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])   # поле емайл
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])  # поле пароль
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()   # нажимаем кнопку войти
        wait = WebDriverWait(main_page, 10)
        order_button = wait.until(EC.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_account_icon(self, main_page, existing_user):  # проверяем вход через кнопку «Личный кабинет»
        main_page.find_element(*LoginLocators.ACCOUNT_LINK).click()   # нажимаем кнопку личный кабинет на главной
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])   # поле емайл
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])  # поле пароль
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()   # нажимаем кнопку войти
        wait = WebDriverWait(main_page, 10)
        order_button = wait.until(EC.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_registration_page(self, main_page, existing_user):  # проверяем вход через кнопку на форме регистрации
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()   # нажимаем кнопку войти в аккаунт
        main_page.find_element(*LoginLocators.REGISTER_LINK).click()   # нажимаем ссылку на регистрацию
        main_page.find_element(*LoginLocators.LOGIN_LINK_REGISTER).click()   # нажимаем кнопку войти на форме регистрации
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])   # поле емайл
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])  # поле пароль
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()   # нажимаем кнопку войти
        wait = WebDriverWait(main_page, 10)
        order_button = wait.until(EC.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_password_recovery(self, main_page, existing_user):  # проверка входа через форму восстановления
        main_page.find_element(*LoginLocators.BUTTON_ENTER).click()   # нажимаем кнопку войти в аккаунт
        main_page.find_element(*LoginLocators.RECOVER_PASSWORD_LINK).click()   # нажимаем ссылку восстановить пароль
        main_page.find_element(*LoginLocators.LOGIN_LINK_RECOVER).click()   # нажимаем кнопку войти на форме восстановления
        main_page.find_element(*LoginLocators.EMAIL_INPUT).send_keys(existing_user["email"])   # поле емайл
        main_page.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(existing_user["password"])  # поле пароль
        main_page.find_element(*LoginLocators.SUBMIT_LOGIN).click()   # нажимаем кнопку войти
        wait = WebDriverWait(main_page, 5)
        order_button = wait.until(EC.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
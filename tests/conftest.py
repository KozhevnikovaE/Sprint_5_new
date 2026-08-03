import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_valid_new_user
from data import EXISTING_USER 
from data import BASE_URL
from locators import AuthLocators

@pytest.fixture               #создаёт экземпляр Chrome-драйвера
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture             #генерирует случайные валидные данные нового пользовател
def valid_user():
    return generate_valid_new_user()


@pytest.fixture            #принимает драйвер, открывает главную страницу приложения
def main_page(driver):
    driver.get(BASE_URL)
    return driver

@pytest.fixture
def existing_user():        #Возвращает данные существующего пользователя (фиксированные)
    return EXISTING_USER.copy()
    
#выполняет авторизацию
@pytest.fixture 
def authorized_main_page(main_page, existing_user):
    driver = main_page
    wait = WebDriverWait(driver, 10) 

    login_btn = wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_LINK_MAIN))
    login_btn.click()

    email_field = wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
    email_field.clear()
    email_field.send_keys(existing_user["email"])

    password_field = wait.until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
    password_field.clear()
    password_field.send_keys(existing_user["password"])

    submit_btn = wait.until(EC.element_to_be_clickable(AuthLocators.SUBMIT_LOGIN_BUTTON))
    submit_btn.click()

    wait.until(EC.visibility_of_element_located(AuthLocators.ORDER_BUTTON))
    return driver
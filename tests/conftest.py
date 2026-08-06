import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, EXISTING_USER, LOGIN_PAGE_URL
from helpers import valid_user as data_valid_user
from locators import LoginLocators as LL


@pytest.fixture               #создаёт экземпляр Chrome-драйвера
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#принимает драйвер, открывает главную страницу приложения
@pytest.fixture
def main_page(driver):
    url = BASE_URL
    driver.get(url)
    return driver

@pytest.fixture
def existing_user():
    return EXISTING_USER

#выполняет авторизацию
@pytest.fixture 
def authorized_main_page(main_page, existing_user):
    main_page.find_element(*LL.BUTTON_ENTER).click()
    main_page.find_element(*LL.EMAIL_INPUT).send_keys(existing_user["email"])
    main_page.find_element(*LL.PASSWORD_INPUT).send_keys(existing_user["password"])
    main_page.find_element(*LL.SUBMIT_LOGIN).click()
    WebDriverWait(main_page, 10).until(EC.visibility_of_element_located(LL.ORDER_BUTTON))
    return main_page

@pytest.fixture
def valid_user():
    return data_valid_user()
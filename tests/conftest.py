import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture               #создаёт экземпляр Chrome-драйвера
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture                #генерирует случайные валидные данные нового пользователя
def valid_user():
    email = f"kozhevnikova_evgeniya50{random.randint(100,999)}@yandex.ru"
    name = "Евгения"
    password = "987654"
    return {"name": name, "email": email, "password": password}

#принимает драйвер, открывает главную страницу приложения
@pytest.fixture
def main_page(driver):
    url = "https://stellarburgers.education-services.ru/"
    driver.get(url)
    return driver


EXISTING_USER = {"email": "jane123@yandex.ru", "password": "123456"}
#выполняет авторизацию
@pytest.fixture 
def authorized_main_page(main_page):
    main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    main_page.find_element(By.XPATH, "(//input[@name='name'])").send_keys(EXISTING_USER["email"])
    main_page.find_element(By.NAME, "Пароль").send_keys(EXISTING_USER["password"])
    main_page.find_element(By.XPATH, "//button[text()='Войти']").click()
    WebDriverWait(main_page, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
    return main_page
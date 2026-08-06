import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators as RL

class TestRegistration:
    def test_successful_registration(self, main_page, valid_user, driver):

        main_page.find_element(*RL.BUTTON_ENTER).click() # нажимаем кнопку войти в аккаунт

        main_page.find_element(*RL.REGISTER_LINK).click() # нажимаем ссылку на регистрацию

    #заполняем поля
        main_page.find_element(*RL.INP_NAME).send_keys(valid_user["name"])    #поле имя 
        main_page.find_element(*RL.INP_EMAIL).send_keys(valid_user["email"])   #поле емайл
        main_page.find_element(*RL.INP_PAS).send_keys(valid_user["password"]) #поле пароль  

        main_page.find_element(*RL.BUTTON_CHEKIN).click()  # нажимаем кнопку зарегистрироваться

        wait = WebDriverWait(driver, 10)
        login_title = wait.until(EC.visibility_of_element_located(RL.TITLE_LOGIN))
        assert login_title.is_displayed()  # ожидаем вывод на экран кнопки "Войти"


    # добавляем негативный тест с невалидным паролем

    def test_registration_invalid_password(self, main_page, valid_user, driver):

        invalid_password = "123" 

        main_page.find_element(*RL.BUTTON_ENTER).click() # нажимаем кнопку войти в аккаунт
        main_page.find_element(*RL.REGISTER_LINK).click() # нажимаем ссылку на регистрацию

        #заполняем поля
        main_page.find_element(*RL.INP_NAME).send_keys(valid_user["name"])    #поле имя 
        main_page.find_element(*RL.INP_EMAIL).send_keys(valid_user["email"])   #поле емайл
        main_page.find_element(*RL.INP_PAS).send_keys(invalid_password) #поле пароль 

        main_page.find_element(*RL.BUTTON_CHEKIN).click() # нажимаем кнопку зарегистрироваться
        
        wait = WebDriverWait(driver, 10)
        error_message = wait.until(EC.visibility_of_element_located(RL.MESSAGE_ERROR))  # проверяем вывод сообщения об ошибке

        assert error_message.is_displayed()
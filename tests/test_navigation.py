import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import NavigateLocators 

class TestConstructor:
    def test_click_constructor(self, authorized_main_page: WebDriver):  # проверяем переход по кнопке конструктор
        authorized_main_page.find_element(*NavigateLocators.CONSTRUCTOR_LINK).click()        # нажимаем кнопку конструктор

        wait = WebDriverWait(authorized_main_page, 10)
        header = wait.until(EC.visibility_of_element_located(NavigateLocators.BURGER_HEADER))
        assert header.is_displayed()

    def test_click_logo(self, authorized_main_page: WebDriver):  # проверяем переход по логотипу Stellar Burgers
        authorized_main_page.find_element(*NavigateLocators.LOGO_LINK).click()               # нажимаем логотип Stellar Burgers

        wait = WebDriverWait(authorized_main_page, 10)
        header = wait.until(EC.visibility_of_element_located(NavigateLocators.BURGER_HEADER))
        assert header.is_displayed()
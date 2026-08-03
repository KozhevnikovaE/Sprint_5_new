import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, ConstructorLocators

class TestConstructor:

    def test_sauces_section(self, authorized_main_page): # проверяем переход к разделу соусы
        wait = WebDriverWait(authorized_main_page, 10)

        sauces_tab=wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB))
        sauces_tab.click()
                
        active_tab = wait.until(EC.visibility_of_element_located(ConstructorLocators.ACTIVE_SAUCES_TAB))
        assert active_tab.is_displayed()

    def test_buns_section(self, authorized_main_page):  # проверяем переход к разделу булки
        wait = WebDriverWait(authorized_main_page, 10)

        # Сначала убеждаемся, что можно кликнуть по вкладке «Соусы» (если это нужно для перехода)
        sauces_tab = wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB))
        sauces_tab.click()
        # Если логика конструктора требует сначала открыть «Соусы», то оставляем этот шаг,
        # но обязательно ждём, что секция «Соусы» действительно отрендерилась.
        wait.until(EC.visibility_of_element_located(ConstructorLocators.ACTIVE_SAUCES_TAB))

        # Теперь кликаем на «Булки»
        buns_tab = wait.until(EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB))
        buns_tab.click()

        # Проверяем активность вкладки «Булки»
        active_tab = wait.until(EC.visibility_of_element_located(ConstructorLocators.ACTIVE_BUNS_TAB))
        assert active_tab.is_displayed()

    def test_fillings_section(self, authorized_main_page):  # проверяем переход к разделу начинки
        wait = WebDriverWait(authorized_main_page, 10)

        fillings_tab = wait.until(EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB))
        fillings_tab.click()

        active_tab = wait.until(EC.visibility_of_element_located(ConstructorLocators.ACTIVE_FILLINGS_TAB))
        assert active_tab.is_displayed()
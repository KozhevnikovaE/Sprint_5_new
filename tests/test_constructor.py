import pytest
from locators import ConstructorLocators
from helpers import is_element_visible

class TestConstructor:

    def test_sauces_section(self, authorized_main_page):

        sauces_tab = authorized_main_page.find_element(*ConstructorLocators.SAUCES_TAB)
        sauces_tab.click()

        assert is_element_visible(authorized_main_page, ConstructorLocators.ACTIVE_SAUCES_TAB)

    def test_buns_section(self, authorized_main_page):  

        sauces_tab = authorized_main_page.find_element(*ConstructorLocators.SAUCES_TAB)
        sauces_tab.click()

        buns_tab = authorized_main_page.find_element(*ConstructorLocators.BUNS_TAB)
        buns_tab.click()

        assert is_element_visible(authorized_main_page, ConstructorLocators.ACTIVE_SAUCES_TAB)

    def test_fillings_section(self, authorized_main_page):  

        fillings_tab = authorized_main_page.find_element(*ConstructorLocators.FILLINGS_TAB)
        fillings_tab.click()

        assert is_element_visible(authorized_main_page, ConstructorLocators.ACTIVE_SAUCES_TAB)
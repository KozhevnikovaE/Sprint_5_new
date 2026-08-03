from selenium.webdriver.common.by import By

class AuthLocators:
    # Навигация
    LOGIN_LINK_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    REGISTER_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

    # Поля ввода (по реальным атрибутам name)
    EMAIL_INPUT = (By.NAME, "name")        # name="name"
    PASSWORD_INPUT = (By.NAME, "Пароль")  # name="Пароль"

    # Регистрация (если нужна отдельно)
    REG_NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/parent::div//input")
    REG_EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/parent::div//input")

    # Действия
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    SUBMIT_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Индикаторы
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(., 'пароль')]")


class ConstructorLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    LOGO_LINK = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    HEADER_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    BUNS_TAB = (By.XPATH, "//span[contains(text(), 'Булки')]")
    SAUCES_TAB = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    FILLINGS_TAB = (By.XPATH, "//span[contains(text(), 'Начинки')]")

    ACTIVE_BUNS_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Булки')]/parent::div[contains(@class, 'tab_tab_type_current')]"
    )
    ACTIVE_SAUCES_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Соусы')]/parent::div[contains(@class, 'tab_tab_type_current')]"
    )
    ACTIVE_FILLINGS_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Начинки')]/parent::div[contains(@class, 'tab_tab_type_current')]"
    )

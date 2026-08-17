from selenium.webdriver.common.by import By

class RegistrationLocators:
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка войти в аккаунт на главной странице
    REGISTER_LINK = (By.CLASS_NAME, "Auth_link__1fOlj") #ссылка на регистрацию

    INP_NAME = (By.XPATH, "//label[text()='Имя']/parent::div//input")   #поле имя 
    INP_EMAIL = (By.XPATH, "//label[text()='Email']/parent::div//input")   #поле емайл
    INP_PAS =(By.NAME, "Пароль")                         #поле пароль 

    BUTTON_CHEKIN = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка зарегистрироваться в форме регистрации
    TITLE_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]") #ожидаемый вывод на экран кнопки "Войти"
    MESSAGE_ERROR = (By.XPATH, "//p[contains(text(),'пароль')]")  #ожидаемый вывод на экран сообщения об ошибке

class LoginAccountLocators:
    # Локаторы для входа через кнопку "Личный кабинет"
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # ссылка для входа в личный кабинет на главной странице
    EMAIL_INPUT_LOGIN = (By.XPATH, "(//input[@name='name'])")           # поле email на форме входа
    INP_PAS = (By.NAME, "Пароль")                                       # поле пароль на форме входа
    SUBMIT_LOGIN = (By.XPATH, "//button[text()='Войти']")               # кнопка «Войти»
    TITLE_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # проверка успешного входа

class LoginLocators:
    # Локаторы для входа по кнопке "Войти в аккаунт"
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти в аккаунт']")   # ссылка для входа в личный кабинет на главной странице
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])")              # поле емайл
    PASSWORD_INPUT = (By.NAME, "Пароль")                             # поле пароль
    SUBMIT_LOGIN = (By.XPATH, "//button[text()='Войти']")            # кнопка войти
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # кнопка проверки входа

    #Локаторы для входа через "Личный кабинет"
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")        # кнопка личный кабинет

    #Локаторы для входа через форму регистрации
    REGISTER_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")              # ссылка на регистрацию
    LOGIN_LINK_REGISTER = (By.XPATH, "//a[text()='Войти']")          # кнопка войти на форме регистрации

    #Локаторы для входа через форму восстановления пароля
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # ссылка восстановить пароль
    LOGIN_LINK_RECOVER = (By.XPATH, "//a[text()='Войти']")            # кнопка войти на форме восстановления

class NavigateLocators:
    #Локаторы для перехода в конструктор
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")           # кнопка конструктор
    LOGO_LINK = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")         # логотип Stellar Burgers
    BURGER_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")  # заголовок для проверк

class LogoutLocators:
    #Локаторы для выхода из аккаунта
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")   # кнопка личный кабинет
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")               # кнопка выход из личного кабинета

class ConstructorLocators:
    #Локаторы для перехода к разделам булки, соусы, начинки
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")                # вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")              # вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")         # вкладка «Начинки»

    ACTIVE_BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]") #локатор активного таба булки
    ACTIVE_SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")  #локатор активного таба соусы
    ACTIVE_FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")  #локатор активного таба начинки
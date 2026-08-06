import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def valid_user():
    name = "Евгения"
    email = f"kozhevnikova_evgeniya50{random.randint(100,999)}@yandex.ru"
    password = "987654"
    return {"name": name, "email": email, "password": password}


def is_element_visible(driver, locator, timeout=15):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()
    except Exception:
        return False
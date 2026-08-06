import random

def valid_user():
    name = "Евгения"
    email = f"kozhevnikova_evgeniya50{random.randint(100,999)}@yandex.ru"
    password = "987654"
    return {"name": name, "email": email, "password": password}
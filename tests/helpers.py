import random

def generate_valid_new_user():
    #Генерирует данные для регистрации нового пользователя (каждый раз разный email)
    name = "Евгения"
    email = f"kozhevnikova_evgeniya50{random.randint(100, 999)}@yandex.ru"
    password = "987654"
    return {"name": name, "email": email, "password": password}
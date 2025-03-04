password = input("Введите пароль: ")

def has_digit(password):
    for char in password:
        if char.isdigit():  # Если символ — цифра
            return True
    return False  # Если цифры не найдены

# Функция для проверки, является ли пароль слишком длинным
def is_very_long(password):
    return len(password) >= 12  # Возвращает True, если длина пароля больше 15

# Основная функция для вычисления рейтинга пароля
def calculate_password_score(password):
    score = 0  # Начальный рейтинг

    if is_very_long(password):
        score += 2

    return score

# Запрашиваем ввод пароля
password = input("Введите пароль: ")

# Вычисляем рейтинг пароля
score = calculate_password_score(password)

# Выводим результат
print(f"Рейтинг пароля: {score}")



    # Начальный рейтинг
# Примеры использования функций
print(has_digit("rnfeinginr"))  # False
print(has_digit("rnvnreiv83282"))  # True
print(is_very_long("onrv"))  # False
print(is_very_long("ogvorneorenvoernb"))  # True
# def has_digit():
#     found_digit = False
#     for char in password:
#         if char.isdigit():
#             found_digit = True
#             break
#     if found_digit:
#         print("Есть цифры")
#     else:
#         print("Нет цифр")
#
#
# def is_very_long():
#     if len(password) >= 12:
#         print("Длинный")
#     else:
#         print("Короткий")
#
#




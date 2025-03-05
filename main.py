password = input("Введите пароль: ")

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_letters(password):
    for char in password:
        if char.isalpha():
            return True
    return False


def is_very_long(password):
    return len(password) >= 12


def calculate_password_score(password):
    score = 0
    if len(password) <= 8:
        score = 0
    else:
        score += (len(password) - 8) / 2
    return score


def has_lower_letters(password):
    for char in password:
        if char.islower():
            return True
    return False


def calculate_password_score(password):
    score = 0
    length = len(password)

    # Учитываем длину пароля
    if length <= 8:
        score = 0
    else:
        score += (length - 8) / 2

    # Учитываем наличие цифр
    if has_digit(password):
        score += 2

    # Учитываем наличие заглавных букв
    if has_upper_letters(password):
        score += 2

    # Учитываем наличие строчных букв
    if has_lower_letters(password):
        score += 2

    # Учитываем очень длинный пароль
    if is_very_long(password):
        score += 4

    # Ограничиваем максимальный балл 8
    return min(score, 8)


#print(has_lower_letters()) # True
print("Счет пароля:", calculate_password_score(password))
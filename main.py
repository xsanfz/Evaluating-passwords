def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def is_very_long(password):
    return len(password) >= 12


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def calculate_password_score(password):
    checks = [
        has_digit,
        has_upper_letters,
        has_lower_letters,
        is_very_long,
        has_symbols,
    ]

    score = 0

    score += sum(2 for check in checks if check(password))

    return score


def main():
    password = input("Введите пароль: ")
    score = calculate_password_score(password)
    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()
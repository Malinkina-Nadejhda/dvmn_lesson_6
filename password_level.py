def is_very_long(password):
    return len(password) > 12


def has_digits(password):
    return any(symbol.isdigit() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isalnum() for symbol in password)


def lvl_password(password):
    score = 0
    check_list_password = [
        is_very_long,
        has_digits,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    for check_password in check_list_password:
        if check_password(password): score += 2
    return score


def main():
    user_password = input("Введите пароль: ")
    print(lvl_password(user_password))


if __name__ == "__main__":
    main()


# Задача 2 (средняя) — Валидация пароля через срезы
#
# Напиши функцию is_valid_password(password: str) -> bool
#
# Пароль валиден если:
# - Длина от 8 до 32 символов включительно
# - Первый символ — буква (используй .isalpha())
# - Последний символ — не пробел
# - Не содержит подстроку "password" (регистронезависимо)
# - Содержит хотя бы одну цифру (используй any() и .isdigit())
#
# Реализуй БЕЗ регулярных выражений — только срезы, in, встроенные методы str.
#
# Примеры:
# is_valid_password("Hello123!")  -> True
# is_valid_password("Hi1")        -> False (короткий)
# is_valid_password("1Hello123!")  -> False (первый символ — цифра)
# is_valid_password("Hello123 ")  -> False (последний символ — пробел)
# is_valid_password("mypassword1") -> False (содержит "password")
# is_valid_password("NoDigitsHere!") -> False (нет цифр)

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if len(password) > 32:
        return False
    if not password[0].isalpha():
        return False
    if password[-1] == " ":
        return False
    if "password" in password.lower():
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    return True
    
    
print(is_valid_password("Hello123!"))
print(is_valid_password("Hi1"))
print(is_valid_password("1Hello123!"))
print(is_valid_password("Hello123 "))
print(is_valid_password("mypassword1"))
print(is_valid_password("NoDigitsHere!"))


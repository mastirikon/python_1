# Задача 3 — С подвохом: Валидатор с повтором
#
# Напиши функцию ask_until_valid(prompt: str, validator, max_attempts: int = 3) -> str | None
# которая:
# - Запрашивает ввод у пользователя через input(prompt)
# - Проверяет через validator(value) -> bool
# - Если валидно — возвращает значение
# - Если исчерпаны попытки — возвращает None
#
# Требования:
# - Использовать while с счётчиком попыток
# - После каждой неудачной попытки выводить: f"Неверно, осталось {remaining} попыток"
# - Не использовать break — выход только через return
#
# Пример использования:
#   result = ask_until_valid(
#       "Введи число от 1 до 10: ",
#       validator=lambda x: x.isdigit() and 1 <= int(x) <= 10,
#       max_attempts=3
#   )
#   if result:
#       print(f"Принято: {result}")
#   else:
#       print("Попытки исчерпаны")
#
# Подвох: не использовать break — только return для выхода из цикла.
# Подумай как при этом сообщить о неудаче после последней попытки.

def ask_until_valid(prompt: str, validator, max_attempts: int = 3) -> str | None:
    for attempt in range(1, max_attempts + 1):
        user_input = input(prompt)
        is_valid: bool = validator(user_input)
        if is_valid:
            return user_input
        print(f"Неверно, осталось {max_attempts - attempt} попыток")
    return None


result = ask_until_valid(
    "Введи число от 1 до 10: ",
    validator=lambda x: x.isdigit() and 1 <= int(x) <= 10,
    max_attempts=3
)
if result:
    print(f"Принято: {result}")
else:
    print("Попытки исчерпаны")
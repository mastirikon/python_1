# Задача 1 — Лёгкая: Таблица умножения
#
# Напиши функцию multiplication_table(n: int) -> str,
# которая возвращает таблицу умножения от 1 до n в виде строки.
#
# Формат вывода:
#   1 x 1 = 1
#   1 x 2 = 2
#   ...
#   n x n = n*n
#
# Требования:
# - Использовать вложенные for + range
# - Строки собирать через список и join (не конкатенацией в цикле)
#
# Пример для n=3:
#   1 x 1 = 1
#   1 x 2 = 2
#   1 x 3 = 3
#   2 x 1 = 2
#   2 x 2 = 4
#   2 x 3 = 6
#   3 x 1 = 3
#   3 x 2 = 6
#   3 x 3 = 9


def multiplication_table(n: int) -> str:
    result: list[str] = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result.append(f"{i} x {j} = {i * j}")
    return "\n".join(result)

print(multiplication_table(3))
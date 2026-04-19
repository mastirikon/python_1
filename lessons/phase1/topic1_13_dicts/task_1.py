# Задача 1 — Лёгкая: инвентаризация
#
# Дан список транзакций — каждая это кортеж (товар, количество).
# Одни товары встречаются несколько раз.
#
# Напиши функцию summarize(transactions) -> dict,
# которая суммирует количество по каждому товару.
#
# Пример:
#   transactions = [
#       ("apple", 3),
#       ("banana", 5),
#       ("apple", 2),
#       ("cherry", 1),
#       ("banana", 3),
#   ]
#   summarize(transactions)
#   → {"apple": 5, "banana": 8, "cherry": 1}

def summarize(transactions: list[tuple]) -> dict:
    result: dict[str, int] = {}
    for key, value in transactions:
        result[key] = result.get(key, 0) + value
    return result

transactions = [
    ("apple", 3),
    ("banana", 5),
    ("apple", 2),
    ("cherry", 1),
    ("banana", 3),
]

print(summarize(transactions))
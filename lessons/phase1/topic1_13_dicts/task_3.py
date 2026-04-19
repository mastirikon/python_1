# Задача 3 — С подвохом: инвертирование словаря
#
# Напиши функцию invert(d: dict) -> dict,
# которая меняет ключи и значения местами.
#
# Пример простого случая:
#   invert({"a": 1, "b": 2, "c": 3})
#   → {1: "a", 2: "b", 3: "c"}
#
# Подвох: что если несколько ключей имеют одинаковое значение?
#   invert({"a": 1, "b": 1, "c": 2})
#   → ?
#
# Реши задачу в двух вариантах:
#   1. invert(d) — просто инвертирует, последний ключ побеждает при дублях
#   2. invert_safe(d) — значения со словаря становятся ключами,
#      а значениями становятся списки всех оригинальных ключей с таким значением
#      invert_safe({"a": 1, "b": 1, "c": 2})
#      → {1: ["a", "b"], 2: ["c"]}

def invert(d: dict[str, int]) -> dict[int, str]:
    by_num: dict[int, str] = {}
    
    for key, val in d.items():
        by_num[val] = key
    
    return by_num

def invert_safe(d: dict[str, int]) -> dict[int, list[str]]:
    by_num: dict[int, list[str]] = {}
    
    for key, val in d.items():
        by_num[val] = by_num.get(val, [])
        by_num[val].append(key)
    
    return by_num
    
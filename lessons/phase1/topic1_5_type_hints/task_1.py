# Задача 1 (лёгкая) — Аннотируй функции
#
# Добавь type hints для параметров и возвращаемых значений.
# Подсказка: get_first возвращает элемент или None если список пуст.

def multiply(a: int, b: int) -> int:
    return a * b

def get_first[T](items: list[T]) -> T | None:
    return items[0] if items else None

def merge_dicts(d1: dict, d2: dict) -> dict:
    return {**d1, **d2}

#
# Задача 2 — Средняя: Частотная таблица
# Напиши функцию frequency(items: list) -> list[tuple]
# которая возвращает список пар (элемент, количество),
# отсортированный по убыванию количества, затем по возрастанию элемента.
#
# Не использовать Counter из collections — только методы list и tuple.
#
# Пример:
#   frequency([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
#   → [(5, 3), (1, 2), (3, 2), (2, 1), (4, 1), (6, 1), (9, 1)]
#
# Подсказка: sorted() принимает key= с tuple — Python сравнивает tuple лексикографически.
#   sorted(..., key=lambda x: (-x[1], x[0]))


from typing import Any


def frequency(items: list) -> list[tuple]:
    items_dict: dict[Any, int] = {}
    for item in items:
        items_dict[item] = items_dict.get(item, 0) + 1
    return sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))

print(frequency([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
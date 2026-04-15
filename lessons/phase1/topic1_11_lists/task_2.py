# Задача 2 — Средняя: Топ-N уникальных
#
# Напиши функцию top_n(items: list, n: int) -> list
# которая возвращает N наибольших *уникальных* элементов,
# отсортированных по убыванию.
#
# Требования:
# - Не использовать set (только методы list)
# - Не изменять исходный список
# - Если уникальных элементов меньше N — вернуть все уникальные
#
# Пример:
#   top_n([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3)  →  [9, 6, 5]
#   top_n([1, 1, 1], 5)                            →  [1]
#   top_n([], 3)                                   →  []

def top_n(items: list, n: int) -> list:
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return sorted(new_list, reverse=True)[:n]


print(top_n([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3))
print(top_n([1, 1, 1], 5))
print(top_n([], 3))
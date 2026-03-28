# Задача 2 (средняя)
# Напиши функцию first_non_none(values: list) -> any | None,
# которая возвращает первый элемент списка, который не является None.
# Если все элементы None — вернуть None.
# Не используй filter() — только цикл с is not None.

def first_non_none(values: list) -> any | None:
    for val in values:
        if val is not None:
            return val
    return None



print(first_non_none([None, None, 3]))
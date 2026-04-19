# Задача 1 — Лёгкая: Возврат статистики
#
# Напиши функцию stats(numbers: list[float]) -> tuple
# которая возвращает (min, max, mean) одним tuple.
# Если список пустой — вернуть (None, None, None).
#
# Использовать только встроенные функции: min(), max(), sum(), len().
# round() для среднего до 2 знаков.
#
# Пример:
#   mn, mx, avg = stats([3, 1, 4, 1, 5, 9, 2, 6])
#   print(mn, mx, avg)   # 1 9 3.88
#
#   stats([])   # (None, None, None)


def stats(numbers: list[float]) -> tuple:
    if not numbers:
        return (None, None, None)
    return (min(numbers), max(numbers), round(sum(numbers) / len(numbers), 2))
    
    
mn, mx, avg = stats([3, 1, 4, 1, 5, 9, 2, 6])
print(mn, mx, avg)   # 1 9 3.88
print(stats([]))
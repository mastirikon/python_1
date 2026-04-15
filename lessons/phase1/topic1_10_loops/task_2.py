# Задача 2 — Средняя: Поиск простых чисел
#
# Напиши функцию primes_up_to(n: int) -> list[int],
# которая возвращает список всех простых чисел от 2 до n включительно.
#
# Требования:
# - Для каждого числа проверяй делимость через вложенный цикл
# - Используй for/else: else срабатывает если делитель не найден — число простое
# - Не использовать готовые библиотеки
#
# Примеры:
#   primes_up_to(10)   -> [2, 3, 5, 7]
#   primes_up_to(20)   -> [2, 3, 5, 7, 11, 13, 17, 19]
#   primes_up_to(2)    -> [2]
#   primes_up_to(1)    -> []

import math


def primes_up_to(n: int) -> list[int]:
    result: list[int] = []
    for i in range(2, n + 1):
        for divisor in range(2, int(math.sqrt(i)) + 1):
            if i % divisor == 0:
                break
        else:
            result.append(i)
        
    return result


print(primes_up_to(10))
print(primes_up_to(20))
print(primes_up_to(2))
print(primes_up_to(1))
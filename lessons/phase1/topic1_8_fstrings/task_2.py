# Задача 2 — Средняя: Отладочный логгер
#
# Напиши функцию debug_call(func, *args), которая:
# 1. Вызывает func с переданными аргументами
# 2. Выводит лог в формате:
#
#    [DEBUG] calculate(a=3, b=4) -> 15  (0.000123s)
#
# Требования:
# - Имя функции берётся из func.__name__
# - Аргументы выводятся как имя=значение через запятую
#   (используй inspect.signature или просто enumerate для позиционных)
# - Результат — через repr()
# - Время выполнения — через time.perf_counter(), формат .6f
# - Используй f"{value!r}" для значений аргументов и результата
#
# Пример вызова:
#   debug_call(calculate, 3, 4)   # -> [DEBUG] calculate(3, 4) -> 15  (0.000042s)
#   debug_call(str.upper, "hello") # -> [DEBUG] upper('hello') -> 'HELLO'  (0.000010s)
#
# Упрощение: позиционные аргументы без имён — просто через repr() через запятую

from time import perf_counter


def calculate(a, b):
    return a * b + a

def debug_call(func, *args) -> None:
    start = perf_counter()
    result = func(*args)
    time_dif = perf_counter() - start
    args_repr = ", ".join(repr(arg) for arg in args)
    print(f"[DEBUG] {func.__name__}({args_repr}) -> {result!r} ({time_dif:.6f})")
    

debug_call(calculate, 3, 4)
debug_call(str.upper, "hello")
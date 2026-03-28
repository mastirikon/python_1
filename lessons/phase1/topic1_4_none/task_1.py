# Задача 1 (лёгкая)
# Напиши функцию safe_divide(a: float, b: float) -> float | None,
# которая делит a на b и возвращает None если b == 0. Без исключений.

def safe_divide(a: float, b: float) -> float | None:
    if b == 0: return None
    return a / b
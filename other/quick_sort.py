import random
import time
from functools import wraps
from typing import Callable

data = [random.randint(0, 1000) for _ in range(0, 1000)]

def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        
        print(f"{func.__name__}: {end - start:.6f} сек, {result[:10]}")

        return result

    return wrapper

def quick_sort(record: list[int]) -> list[int]:
    # список меньше 2-х элементов нет смысла сортировать
    if len(record) < 2:
        return record
    
    # контрольное значение от которого будем отталкиваться при разбиении списка
    pivot = random.randint(0, len(record) - 1)
    start = [el for el in record if el < record[pivot]]
    middle = [el for el in record if el == record[pivot]]
    end = [el for el in record if el > record[pivot]]
    
    # Рекурсия на оставшивеся списки + конкатенация
    return quick_sort(start) + middle + quick_sort(end)


def quick_set_sort(record: list[int]) -> list[int]:
    # список меньше 2-х элементов нет смысла сортировать
    if len(record) < 2:
        return record
    
    # контрольное значение от которого будем отталкиваться при разбиении списка
    pivot = random.randint(0, len(record) - 1)
    start = [el for el in record if el < record[pivot]]
    middle = [record[pivot]]
    end = [el for el in record if el > record[pivot]]
    # Рекурсия на оставшивеся списки + конкатенация
    return quick_set_sort(start) + middle + quick_set_sort(end)


@timer
def quick_sort_wrapper(data):
    return quick_sort(data)


@timer
def quick_set_sort_wrapper(data):
    return quick_set_sort(data)


@timer
def sorted_wrapper(data):
    return sorted(data)


@timer
def sort_inplace(data):
    data.sort()
    return data


quick_sort_wrapper(data.copy())
quick_set_sort_wrapper(data.copy())
sorted_wrapper(data.copy())
sort_inplace(data.copy())
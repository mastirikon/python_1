# Задача 3 — С подвохом: NamedTuple маршрут
#
# Определи NamedTuple Waypoint с полями:
#   - lat: float
#   - lon: float
#   - label: str = ""
#
# Напиши функцию total_distance(route: list[Waypoint]) -> float
# которая считает суммарное расстояние маршрута между точками по формуле
# евклидова расстояния: sqrt((lat2-lat1)**2 + (lon2-lon1)**2)
# Если точек меньше 2 — вернуть 0.0.
#
# Пример:
#   route = [
#       Waypoint(0.0, 0.0, "start"),
#       Waypoint(3.0, 4.0, "middle"),
#       Waypoint(6.0, 8.0, "end"),
#   ]
#   total_distance(route)  →  10.0
#
# Подвох: zip(route, route[1:]) — попробуй объяснить себе почему это даёт пары соседних точек.
#
import math
from typing import NamedTuple


class Waypoint(NamedTuple):
    lat: float # широта
    lon: float # долгота
    label: str = ""


route = [
    Waypoint(0.0, 0.0, "start"),
    Waypoint(3.0, 4.0, "middle"),
    Waypoint(6.0, 8.0, "end"),
]


def total_distance(route: list[Waypoint]) -> float:
    if len(route) < 2: 
        return 0.0
    
    distance: float = 0.0
    
    for a, b in zip(route, route[1:]):
        distance += math.sqrt((b.lat-a.lat)**2 + (b.lon-a.lon)**2)
    
    return distance


print(total_distance(route)) #  →  10.0
print(total_distance([]))
print(total_distance([Waypoint(0.0, 1.2, 'start')]))


# Подвох: zip(route, route[1:]) - Объясняю: zip берет первые элементы каждого из списка, строки, словаря (дефолтно берутся ключи словаря) (или в нашем случае кортежа)
# но если первый кортеж мы передали полностью, то вторым параметром мы передали срез кортежа, который начинается с первого элемента а не с нулевого
# Каждая итерация zip возвращает кортеж который содержит элеметы переданных структур с одинаковым индексом, начиная с 0, заканчивая длинной самой короткой структуры переданных данных
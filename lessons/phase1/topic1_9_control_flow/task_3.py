# Задача 3 — С подвохом: Классификатор точек
#
# Напиши функцию classify_point(point) -> str,
# которая принимает точку в одном из форматов и классифицирует её.
#
# Форматы входных данных (используй match/case с деструктуризацией):
# - (0, 0)           -> "Origin"
# - (x, 0)           -> f"X-axis at {x}"
# - (0, y)           -> f"Y-axis at {y}"
# - (x, y) где x==y  -> f"Diagonal at {x}"
# - (x, y)           -> f"Point ({x}, {y})"
# - [x, y, z]        -> f"3D point ({x}, {y}, {z})"
# - любое другое     -> "Unknown"
#
# Примеры:
#   classify_point((0, 0))       -> "Origin"
#   classify_point((3, 0))       -> "X-axis at 3"
#   classify_point((4, 4))       -> "Diagonal at 4"
#   classify_point((1, 2))       -> "Point (1, 2)"
#   classify_point([1, 2, 3])    -> "3D point (1, 2, 3)"
#   classify_point("something")  -> "Unknown"
#
# Подвох: порядок case имеет значение — подумай какой case должен идти первым

def classify_point(point) -> str:
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"X-axis at {x}"
        case (0, y):
            return f"Y-axis at {y}"
        case (x, y) if x == y:
            return f"Diagonal at {x}"
        case (x, y):
            return f"Point ({x}, {y})"
        case [x, y, z]:
            return f"3D point ({x}, {y}, {z})"
        case _:
            return "Unknown"
        
print(classify_point((0, 0)))
print(classify_point((3, 0)))
print(classify_point((4, 4)))
print(classify_point((1, 2)))
print(classify_point([1, 2, 3]))
print(classify_point("something"))
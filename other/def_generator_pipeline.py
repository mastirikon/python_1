# Определите функцию генератора get_odds(), 
# которая возвращает нечетные числа из диапазона range(10). 
# Используйте цикл for, чтобы найти и вывести третье возвращенное значение.

# def get_odds():
#     x = 0
#     while True:
#         yield x
#         x += 1
            
# generator = get_odds()            
            
# print("1:", next(generator))
# print("2:", next(generator))
# print("3:", next(generator))

# while True:
#     user_input = input("Next? ")
#     if user_input == "n":
#         print('end')
#         break
    
#     print(f"Next is: {next(generator)}")


# gen = get_odds() 

# Вызов только 1 раз, потом генератор истощается
# print(*gen)
        
# for i, val in enumerate(gen):
#     if i == 2:
#         print(val)
from typing import TypedDict, Iterator


class User(TypedDict):
    id: int
    name: str
    active: bool
    
class UserMeta(User):
    user_id: int
    username: str
    
    
type Users = list[User]

# DB
rows: Users = [
    {"id": 1, "name": "  Alice ", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "  Charlie  ", "active": True},
]


# Эмулиция курсора
def source(data: Users) -> Iterator[User]:
    for row in data:
        yield row


# Очистка имен от лишних символов и пробелов + перевод в нижний регистр
def clean(rows: Iterator[User]) -> Iterator[User]:
    for row in rows:
        row["name"] = row["name"].strip().lower()
        yield row


# Фильтр по активным
def only_active(rows: Iterator[User]) -> Iterator[User]:
    for row in rows:
        if row["active"]:
            yield row
            
            
# Преобразуем в добный вид и наполняем данными
def transform(rows: Iterator[User]) -> Iterator[UserMeta]:
    for row in rows:
        yield {
            **row,
            "user_id": row["id"],
            "username": row["name"],
        }


pipeline = transform(only_active(clean(source(rows))))

for item in pipeline:
    print(item)
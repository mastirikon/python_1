from random import randbytes, randint
from typing import Generator, TypedDict, Callable

class User(TypedDict):
    name: str
    age: int
    say_hallo: Callable

def user_generator() -> Generator[User]:
    while True:
        name = randbytes(5).decode(errors="ignore")
        yield {
            "name": name,
            "age": randint(18, 85),
            "say_hallo": lambda name=name: f'Hello {name}'
        }
        
        
user_batch = user_generator()

for user in user_batch:
    print(f"{user['say_hallo']()}\n")
    if(user['age'] == 18):
        break
    
while True:
    input("Who is next? ")
    user = next(user_batch)
    print(f"{user['say_hallo']()}\n")
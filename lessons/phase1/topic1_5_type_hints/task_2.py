# Задача 2 (средняя) — Типизированный класс Stack[T]
#
# Напиши обобщённый стек с type hints:
# - Хранит элементы типа T в list
# - push(item: T) -> None
# - pop() -> T | None  (None если стек пуст)
# - peek() -> T | None (посмотреть верхний элемент без удаления)
# - is_empty -> bool  (свойство через @property)
#
# Используй TypeVar и Generic из typing.

from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    stack: list[T]
    
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, item: T) -> None:
        self.stack.append(item)
        
    def pop(self) -> T | None:
        if self.is_empty:
            return None
        el: T | None = self.stack[-1]
        del self.stack[-1]
        return el
    
    def peek(self) -> T | None:
        if self.is_empty:
            return None
        return self.stack[-1]
    
    @property
    def is_empty(self) -> bool:
        return not self.stack
    
    
    
    

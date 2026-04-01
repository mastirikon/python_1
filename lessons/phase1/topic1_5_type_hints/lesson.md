# Тема 1.5 — Type hints

---

## 1. Зачем нужны type hints

### Контекст

Python — динамически типизированный язык. Переменные не имеют типов — типы имеют *объекты*. Но начиная с **Python 3.5 (PEP 484)** появились аннотации типов — необязательные подсказки для инструментов статического анализа.

**Ключевое:** type hints **не влияют на выполнение программы**. Python их игнорирует в рантайме (по умолчанию).

```python
x: int = "hello"  # Python не ругается! Это просто аннотация
print(x)          # hello — всё работает
```

Зачем тогда нужны?

1. **Статические анализаторы** (`mypy`, `pyright`) проверяют типы *до* запуска
2. **IDE** (PyCharm, VS Code с Pylance) даёт autocomplete и подчёркивает ошибки
3. **Документация** — аннотации делают сигнатуры функций самодокументируемыми
4. **Runtime валидация** через библиотеки (`pydantic`, `FastAPI` — читают аннотации)

**JS-аналогия:** TypeScript vs JavaScript. Type hints = TypeScript-аннотации, но *без компиляции*. Интерпретатор их не проверяет — только сторонние инструменты.

---

## 2. Базовый синтаксис переменных

```python
# Переменная с аннотацией
x: int = 42
name: str = "Alice"
ratio: float = 3.14
active: bool = True
nothing: None = None

# Аннотация без присваивания (объявление намерения)
count: int          # переменная ещё не существует, но IDE знает тип
# print(count)      # NameError — переменной нет!

# Разница — count просто попадает в __annotations__, объект не создаётся
```

**Подкапотно:** аннотации хранятся в `__annotations__` — обычном словаре.

```python
class Config:
    host: str = "localhost"
    port: int = 8080

print(Config.__annotations__)
# {'host': <class 'str'>, 'port': <class 'int'>}
```

---

## 3. Аннотации функций

Это главное применение type hints в реальном коде.

```python
# Базовый синтаксис
def greet(name: str) -> str:
    return f"Hello, {name}"

# Несколько параметров
def add(a: int, b: int) -> int:
    return a + b

# Функция ничего не возвращает
def log_message(msg: str) -> None:
    print(msg)

# Параметры по умолчанию — тип пишется ДО знака =
def connect(host: str = "localhost", port: int = 8080) -> bool:
    ...  # многоточие — валидный body (как pass)
```

**Ловушка для JS-разработчика:** в TypeScript тип пишется *после* знака `:` для параметра, а `: type` стоит перед значением по умолчанию. В Python — аналогично, но синтаксис чуть другой:

```typescript
// TypeScript
function connect(host: string = "localhost", port: number = 8080): boolean { ... }
```

```python
# Python — то же самое, но без `:` для возвращаемого типа перед телом
def connect(host: str = "localhost", port: int = 8080) -> bool: ...
```

---

## 4. Optional — когда значение может быть None

Это самый частый паттерн в реальном коде. Раз тема 1.4 уже пройдена — вот как это выглядит с типами:

```python
from typing import Optional

# Optional[str] = str | None
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

# Python 3.10+ — более читаемый синтаксис через |
def find_user_modern(user_id: int) -> str | None:
    if user_id == 1:
        return "Alice"
    return None
```

**JS-аналогия:** `string | null` в TypeScript.

```typescript
// TypeScript
function findUser(userId: number): string | null { ... }
```

```python
# Python 3.10+
def find_user(user_id: int) -> str | None: ...
```

---

## 5. Коллекции — list, dict, tuple, set

### До Python 3.9 — импорт из `typing`

```python
from typing import List, Dict, Tuple, Set

def process(items: List[int]) -> Dict[str, int]:
    return {str(i): i for i in items}

def coords() -> Tuple[float, float]:
    return (1.0, 2.0)

def unique(items: List[str]) -> Set[str]:
    return set(items)
```

### Python 3.9+ — встроенные типы напрямую (рекомендуется)

```python
# Нижний регистр — без импорта!
def process(items: list[int]) -> dict[str, int]:
    return {str(i): i for i in items}

def coords() -> tuple[float, float]:
    return (1.0, 2.0)

def unique(items: list[str]) -> set[str]:
    return set(items)
```

**Ловушка:** В Python 3.8 и ниже `list[int]` вызовет `TypeError` в рантайме (если не использовать `from __future__ import annotations`). Для совместимости — используй `List[int]` из `typing` или добавь `from __future__ import annotations`.

```python
# Решение для обратной совместимости
from __future__ import annotations
# Теперь все аннотации — строки, вычисляются лениво. list[int] работает везде.
```

---

## 6. Union — несколько допустимых типов

```python
from typing import Union

# Старый стиль
def parse(value: Union[str, int]) -> str:
    return str(value)

# Python 3.10+ — новый синтаксис |
def parse_modern(value: str | int) -> str:
    return str(value)
```

---

## 7. Any — отключить проверку типов

```python
from typing import Any

def legacy_function(data: Any) -> Any:
    return data  # mypy не будет проверять

# Используется для постепенной миграции legacy-кода на типы
```

**Ловушка:** `Any` — это escape-hatch, не серебряная пуля. Если всё помечено `Any` — type hints бесполезны.

---

## 8. Callable — тип функции

```python
from typing import Callable

# Callable[[аргументы], возвращаемый_тип]
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

apply(lambda x, y: x + y, 1, 2)  # 3
```

**JS-аналогия:** `(a: number, b: number) => number` в TypeScript.

---

## 9. TypeVar — обобщённые функции (generics)

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

# mypy знает: если передать list[int] → вернётся int
result: int = first([1, 2, 3])       # OK
result2: str = first(["a", "b"])     # OK
```

**JS-аналогия:** generics в TypeScript: `function first<T>(items: T[]): T`.

---

## 10. TYPE_CHECKING — импорты только для анализаторов

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mymodule import HeavyClass  # не выполняется в рантайме

def process(obj: "HeavyClass") -> None:  # строка-аннотация
    ...
```

Используется для разрыва циклических импортов и ускорения старта приложения.

---

## 11. Реальный use-case — FastAPI читает аннотации в рантайме

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int
    email: str | None = None

@app.post("/users")
async def create_user(user: UserCreate) -> dict:
    # FastAPI автоматически:
    # 1. Парсит JSON из request body
    # 2. Валидирует типы через pydantic
    # 3. Генерирует OpenAPI документацию
    # Всё это — благодаря аннотациям!
    return {"id": 1, "name": user.name}
```

Это главное отличие от TypeScript: там аннотации стираются при компиляции. В Python — они *доступны в рантайме* через `__annotations__`, и библиотеки активно их используют.

---

## 12. Проверка типов — mypy

```bash
pip install mypy
mypy script.py
```

```python
# example.py
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(42)  # mypy: Argument 1 to "greet" has incompatible type "int"; expected "str"
```

Mypy не запускает код — только анализирует. Это статическая проверка, как tsc в TypeScript.

---

## Задачи

### Задача 1 (лёгкая) — Аннотируй функции

Есть три функции без аннотаций. Добавь type hints для параметров и возвращаемых значений:

```python
def multiply(a, b):
    return a * b

def get_first(items):
    return items[0] if items else None

def merge_dicts(d1, d2):
    return {**d1, **d2}
```

Сохрани в `task_1.py`.

---

### Задача 2 (средняя) — Типизируй класс

Напиши класс `Stack` с type hints:
- Хранит элементы типа `T` (TypeVar) в `list`
- Метод `push(item: T) -> None`
- Метод `pop() -> T | None` (возвращает `None` если стек пуст)
- Метод `peek() -> T | None`
- Свойство `is_empty: bool`

Используй `TypeVar` и `Generic` из `typing`.

Сохрани в `task_2.py`.

---

### Задача 3 (с подвохом) — Что выведет mypy?

```python
from typing import Optional

def process(value: Optional[int]) -> int:
    return value * 2  # проблема здесь?

result = process(None)
```

Объясни: почему mypy будет ругаться на эту функцию? Как исправить — 2 способа?

Сохрани объяснение и исправленный код в `task_3.py`.

---

## Конспект: Type hints

### Суть

Type hints — необязательные аннотации типов, добавленные в Python 3.5+. Интерпретатор их **игнорирует в рантайме** (по умолчанию), но их используют статические анализаторы (`mypy`, `pyright`), IDE и библиотеки вроде `pydantic`/`FastAPI`. Главное отличие от TypeScript: аннотации хранятся в `__annotations__` и доступны в рантайме — это делает возможным такие вещи как автоматическая валидация в FastAPI.

### Python → JS

| Python | Что делает | TypeScript |
|--------|-----------|-----------|
| `x: int = 42` | аннотация переменной | `let x: number = 42` |
| `def f(a: str) -> None:` | аннотация функции | `function f(a: string): void` |
| `str \| None` (3.10+) или `Optional[str]` | опциональный тип | `string \| null` |
| `str \| int` (3.10+) или `Union[str, int]` | union тип | `string \| number` |
| `list[int]` (3.9+) или `List[int]` | типизированный список | `Array<number>` |
| `dict[str, int]` | типизированный словарь | `Record<string, number>` |
| `tuple[int, str]` | типизированный кортеж | `[number, string]` |
| `Callable[[int], str]` | тип функции | `(a: number) => string` |
| `T = TypeVar("T"); def f(x: T) -> T:` | generic-функция | `function f<T>(x: T): T` |
| Типы остаются в `__annotations__` | доступны в рантайме | компилятор удаляет типы |

### Синтаксис / API

```python
# Переменная
x: int = 42
name: str

# Функция
def greet(name: str, age: int = 0) -> str: ...

# None-возврат
def log(msg: str) -> None: ...

# Optional (может быть None)
from typing import Optional
def find(id: int) -> Optional[str]: ...
def find_modern(id: int) -> str | None: ...  # Python 3.10+

# Union (несколько типов)
from typing import Union
def parse(v: Union[str, int]) -> str: ...
def parse_modern(v: str | int) -> str: ...  # Python 3.10+

# Коллекции (Python 3.9+)
def f(items: list[int]) -> dict[str, int]: ...
def g(data: tuple[float, float]) -> set[str]: ...

# Старый стиль (до 3.9)
from typing import List, Dict, Tuple, Set
def f(items: List[int]) -> Dict[str, int]: ...

# Any — отключить проверку
from typing import Any
def legacy(data: Any) -> Any: ...

# Callable — тип функции
from typing import Callable
def apply(fn: Callable[[int, int], int]) -> int: ...

# TypeVar — generics
from typing import TypeVar
T = TypeVar("T")
def first(items: list[T]) -> T: ...

# Обратная совместимость (list[int] в Python 3.8)
from __future__ import annotations
```

### Подкапотно

- Аннотации хранятся в `__annotations__` — обычный `dict` на классе или модуле
- В рантайме Python **не проверяет** соответствие типов (без сторонних инструментов)
- `from __future__ import annotations` (PEP 563) делает все аннотации строками — они вычисляются лениво, что ускоряет импорт и решает проблемы с forward references
- `typing.get_type_hints(obj)` — получить аннотации с разрешёнными forward references
- `pydantic`, `FastAPI`, `dataclasses` — читают `__annotations__` в рантайме для генерации кода

### Ловушки

```python
# Ловушка 1: list[int] в Python 3.8 вызовет TypeError в рантайме
# Неправильно (в 3.8):
def f(x: list[int]) -> None: ...  # TypeError при вызове!

# Правильно:
from typing import List
def f(x: List[int]) -> None: ...
# Или добавить в начало файла:
from __future__ import annotations

# Ловушка 2: аннотация без присваивания не создаёт переменную
x: int       # только запись в __annotations__
print(x)     # NameError: name 'x' is not defined

# Ловушка 3: Optional не проверяется автоматически
def double(x: Optional[int]) -> int:
    return x * 2  # mypy: "int | None" has no attribute __mul__ — нужна проверка!

# Правильно:
def double(x: Optional[int]) -> int:
    if x is None:
        return 0
    return x * 2

# Ловушка 4: type hints не влияют на поведение
x: int = "hello"  # работает! Python не бросает исключение
```

### Когда использовать

- **Всегда** для публичных функций и методов — это документация сигнатуры
- **Всегда** для аргументов FastAPI/pydantic — они читают аннотации в рантайме
- **В классах** — аннотируй поля, особенно в `@dataclass`
- **Постепенная миграция** — начни с `Any`, заменяй по мере понимания
- **`TYPE_CHECKING`** — для импортов только для анализатора (разрыв циклических зависимостей)
- **Не аннотируй** — очевидные локальные переменные внутри функций (избыточно): `i: int = 0` в цикле не нужно

# Тема 1.4 — `None` vs JS `null`/`undefined`

---

## 1. Что такое `None`

**JS-аналогия:** В JS есть два "пустых" значения — `null` (явное отсутствие) и `undefined` (не задано). В Python только одно — `None`. Оно покрывает оба случая.

```python
# JS: let x = null; let y = undefined;
# Python:
x = None

print(x)         # None
print(type(x))   # <class 'NoneType'>
```

**Подкапотно:** `None` — это синглтон. В памяти существует ровно один объект `NoneType`. Все переменные со значением `None` указывают на один и тот же объект.

```python
a = None
b = None
print(a is b)  # True — один и тот же объект в памяти
print(id(a) == id(b))  # True
```

**Используется:** возвращаемое значение функции по умолчанию, отсутствующий аргумент, "нет результата".

---

## 2. `is None` vs `== None`

**Ловушка из JS-опыта:** В JS сравнивают через `=== null`. В Python правило простое: **всегда используй `is None`**, никогда `== None`.

```python
x = None

# Правильно
if x is None:
    print("пусто")

# Неправильно — работает, но нарушает PEP 8 и может дать сюрприз
if x == None:
    print("пусто")
```

**Почему `== None` плохо:** оператор `==` можно переопределить через `__eq__`. Класс может вернуть `True` при сравнении с `None`, хотя объект не `None`.

```python
class Weird:
    def __eq__(self, other):
        return True  # всегда True

w = Weird()
print(w == None)  # True — но w не None!
print(w is None)  # False — правильный ответ
```

**`is not None` — тоже идиома:**
```python
def process(value):
    if value is not None:
        return value * 2
```

---

## 3. `None` как falsy

`None` — falsy-значение, как `null` в JS:

```python
x = None

if not x:
    print("falsy")  # выведет

# Но осторожно: 0, "", [], {} — тоже falsy
# Если нужно именно None — проверяй через is None
def get_count() -> int | None:
    return 0  # ← это не None, но тоже falsy!

result = get_count()

# Плохо — 0 будет воспринят как "нет результата"
if not result:
    print("нет данных")  # ← ошибка! 0 тоже сюда попадёт

# Хорошо
if result is None:
    print("нет данных")
```

---

## 4. `None` как возвращаемое значение

Функция без `return` возвращает `None` — как в JS функция без `return` возвращает `undefined`.

```python
def do_something():
    x = 1 + 1  # нет return

result = do_something()
print(result)         # None
print(result is None) # True
```

**Реальный use-case:** паттерн "функция возвращает результат или None" — стандартный способ сигнализировать об отсутствии результата без исключения:

```python
def find_user(user_id: int) -> dict | None:
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)  # вернёт None если не найдено

user = find_user(99)
if user is None:
    print("Пользователь не найден")
```

---

## 5. `Optional` — тайп-хинт для "None или тип"

**JS-аналогия:** как `string | null` в TypeScript.

```python
from typing import Optional

# Старый синтаксис (до Python 3.10)
def greet(name: Optional[str]) -> str:
    if name is None:
        return "Hello, stranger"
    return f"Hello, {name}"

# Новый синтаксис (Python 3.10+) — предпочтительный
def greet(name: str | None) -> str:
    if name is None:
        return "Hello, stranger"
    return f"Hello, {name}"
```

**Подкапотно:** `Optional[str]` — это просто синтаксический сахар для `Union[str, None]`. С Python 3.10 можно писать `str | None` напрямую.

```python
from typing import Optional, Union, get_args

print(get_args(Optional[str]))   # (<class 'str'>, <class 'NoneType'>)
print(get_args(str | None))      # (<class 'str'>, <class 'NoneType'>)
# Одно и то же
```

---

## 6. `None` как default-аргумент (важный паттерн)

**Ловушка:** никогда не используй mutable объект (list, dict) как default-аргумент — он создаётся один раз при определении функции. Вместо этого используй `None`:

```python
# ПЛОХО — баг: список разделяется между всеми вызовами
def add_item(item, storage=[]):
    storage.append(item)
    return storage

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] ← сюрприз!

# ХОРОШО — None как сигнал "создай новый список"
def add_item(item, storage=None):
    if storage is None:
        storage = []
    storage.append(item)
    return storage

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b'] ← правильно
```

Это один из самых частых питоновских паттернов — запомни его.

---

## Задачи

Сохраняй решения в `lessons/phase1/topic1_4_none/task_1.py`, `task_2.py`, `task_3.py`

**Задача 1 (лёгкая).** Напиши функцию `safe_divide(a: float, b: float) -> float | None`,
которая делит `a` на `b` и возвращает `None` если `b == 0`. Без исключений.

**Задача 2 (средняя).** Напиши функцию `first_non_none(values: list) -> any | None`,
которая возвращает первый элемент списка, который не является `None`.
Если все элементы `None` — вернуть `None`.
Не используй фильтрацию через `filter()` — только цикл с `is not None`.

**Задача 3 (с подвохом).** Напиши функцию `merge_defaults(data: dict, defaults: dict | None = None) -> dict`,
которая возвращает словарь: сначала значения из `defaults`, поверх — значения из `data`.
Если `defaults` не передан (None) — использовать `{"timeout": 30, "retries": 3}` как базовые.
Подвох: не мутируй входные словари.

---

## Конспект: `None` vs JS `null`/`undefined`

### Суть
`None` — единственное "пустое" значение в Python, синглтон типа `NoneType`. Заменяет и `null`, и `undefined` из JS. Всегда проверяй через `is None` / `is not None`, а не через `==`. Является falsy-значением, но не путай с `0`, `""`, `[]` — они тоже falsy, но не `None`.

### Python → JS

| Python | Что делает | JavaScript |
|--------|-----------|-----------|
| `None` | единственное пустое значение | `null` + `undefined` |
| `is None` | проверка через идентичность объекта | `=== null` |
| `is not None` | проверка наличия значения | `!== null` |
| `str \| None` или `Optional[str]` | тип hints для опционального значения | `string \| null` (TS) |
| `def f(): pass` → `None` | функция без return возвращает None | `function() {}` → `undefined` |

### Синтаксис / API

```python
x = None                    # присвоение

x is None                   # проверка — всегда так
x is not None               # обратная проверка

type(None)                  # <class 'NoneType'>

# Type hints
def f(x: str | None) -> int | None: ...       # Python 3.10+
def f(x: Optional[str]) -> Optional[int]: ... # до 3.10

# None как default вместо mutable
def f(items=None):
    if items is None:
        items = []
```

### Подкапотно
- `None` — синглтон: один объект на весь интерпретатор, все `None` указывают на него
- `is` проверяет идентичность объектов (`id(a) == id(b)`), а не значение — поэтому надёжнее `==` для `None`
- `Optional[str]` == `Union[str, None]` — просто синтаксический сахар
- Функция без `return` неявно выполняет `return None`

### Ловушки

```python
# 1. == None вместо is None — опасно
class Tricky:
    def __eq__(self, other): return True
t = Tricky()
t == None   # True — НЕВЕРНО
t is None   # False — верно

# 2. falsy != None
result = 0
if not result:  # 0 тоже falsy — ошибочно трактуем как None
    ...
if result is None:  # правильно

# 3. Mutable default argument
def bad(lst=[]):    # список создаётся ОДИН раз
    lst.append(1)
    return lst
bad()  # [1]
bad()  # [1, 1] — баг!

def good(lst=None): # правильно
    if lst is None:
        lst = []
    lst.append(1)
    return lst
```

### Когда использовать
- `is None` / `is not None` — всегда для проверки на None, никогда `== None`
- `str | None` как тип — когда функция может не вернуть результат (поиск, парсинг)
- `def f(arg=None)` — когда default должен быть list/dict (mutable default паттерн)
- `return None` явно — когда хочешь подчеркнуть, что функция ничего не возвращает (опционально)

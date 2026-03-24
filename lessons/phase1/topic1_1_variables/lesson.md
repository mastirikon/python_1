# Topic 1.1 — Переменные и типы: `int`, `float`, `bool`, `None`

---

## Часть 0: PEP — стандарты Python

### Что такое PEP

**PEP (Python Enhancement Proposal)** — официальный документ, описывающий новую фичу языка, процесс или соглашение. Аналог RFC в веб-стандартах или TC39 proposals в JS.

**Три типа PEP:**
| Тип | Описание | Пример |
|-----|----------|--------|
| Standards Track | Новые фичи языка или stdlib | PEP 572 — walrus `:=` |
| Informational | Руководства и соглашения | PEP 8 — стиль кода |
| Process | Изменение процессов в сообществе | PEP 1 — правила PEP |

**Статусы:** `Draft → Accepted → Final | Rejected | Withdrawn | Superseded`

---

### История Python

| Год | Событие |
|-----|---------|
| 1989 | Гвидо ван Россум начал писать Python на Рождество |
| 1991 | Python 0.9.0 опубликован |
| 2000 | Python 2.0: list comprehensions, garbage collection |
| 2006 | PEP 3000: план Python 3 (несовместимый с Python 2) |
| 2008 | Python 3.0: `print` стал функцией, `str` = unicode |
| 2018 | Гвидо уходит с поста **BDFL** после споров вокруг PEP 572 (walrus `:=`) |
| 2019 | Python управляется **Steering Council** (5 человек, ежегодные выборы) |
| 2020 | Python 2 официально умер |
| 2023 | Python 3.12: значительный прирост производительности |
| 2024 | Python 3.13: экспериментальный **free-threaded mode** (без GIL!) |

> **BDFL** = Benevolent Dictator For Life — так называли Гвидо 27 лет

---

### Ключевые PEP — знать обязательно

#### PEP 8 — Style Guide (2001)
Главный документ по стилю. Аналог ESLint rules.

| Правило | Пример |
|---------|--------|
| Отступы: 4 пробела | `def foo():` → тело с 4 пробелами |
| `snake_case` для переменных и функций | `my_variable`, `calculate_price()` |
| `PascalCase` для классов | `UserProfile`, `OrderService` |
| `UPPER_CASE` для констант | `MAX_RETRIES`, `BASE_URL` |
| 2 пустые строки между функциями верхнего уровня | |
| 1 пустая строка между методами класса | |
| Пробелы вокруг операторов | `x = 1`, не `x=1` |
| Без пробелов внутри скобок | `f(x, y)`, не `f( x, y )` |

Сегодня PEP 8 проверяют: `ruff`, `flake8`. Форматируют автоматически: `black`, `ruff format`.

```python
def calculate_total_price(base_price: float, tax_rate: float) -> float:  # snake_case
    return base_price * (1 + tax_rate)

class OrderService:           # PascalCase
    MAX_RETRIES = 3           # UPPER_CASE

    def process_order(self):  # snake_case
        pass
```

#### PEP 20 — The Zen of Python (2004)
19 принципов философии Python. Запустить: `python -c "import this"`

Самые важные:
- **"Explicit is better than implicit"** — нет магии, всё видно в коде (в JS много implicit: `this`, type coercion)
- **"Readability counts"** — код читают чаще чем пишут
- **"There should be one obvious way to do it"** — в отличие от JS, где есть несколько равнозначных способов
- **"If the implementation is hard to explain, it's a bad idea"** — сложный код = плохое решение

#### PEP 257 — Docstring Conventions (2001)
Как писать документацию. Аналог JSDoc, но встроен в язык.

```python
def calculate_tax(price: float, rate: float) -> float:
    """Calculate tax amount for a given price and rate.

    Args:
        price: Base price before tax.
        rate: Tax rate as a decimal (e.g., 0.2 for 20%).

    Returns:
        Tax amount (not the total price).

    Example:
        >>> calculate_tax(100.0, 0.2)
        20.0
    """
    return price * rate

print(calculate_tax.__doc__)  # доступно через __doc__
```

#### PEP 484 — Type Hints (2014)
Официальный синтаксис аннотаций типов. До него типы писали в docstring — неудобно. Основа для `mypy`, `pyright`.

#### PEP 526 — Variable Annotations (2016)
Расширил PEP 484 на переменные:
```python
counter: int = 0
items: list[str] = []
```

#### PEP 572 — Walrus Operator `:=` (2018, Python 3.8+)
Из-за этого PEP Гвидо ушёл с поста BDFL. Споры были настолько горячими, что он устал и передал управление. Сам PEP приняли.

```python
import re
text = "Error: connection timeout on port 8080"
if match := re.search(r"port (\d+)", text):  # присвоить и проверить
    print(f"Порт: {match.group(1)}")          # Порт: 8080
```

#### PEP 634 — Structural Pattern Matching (2020, Python 3.10+)
`match/case` — как `switch` в JS, но значительно мощнее. Подробно — в теме 1.9.

```python
def handle_status(status: int) -> str:
    match status:
        case 200: return "OK"
        case 404: return "Not Found"
        case _:   return "Unknown"
```

**Также:** PEP 405 — venv (2012), PEP 517/518 — `pyproject.toml` (2015/2016)

**Читать:** [peps.python.org](https://peps.python.org) | `python -c "import this"`

---

## Часть 1: Объявление переменных

### JS → Python

| JavaScript | Python |
|-----------|--------|
| `let x = 1` | `x = 1` |
| `const x = 1` | `X = 1` (соглашение UPPER_CASE, не язык) |
| `const [a, b] = [1, 2]` | `a, b = 1, 2` |
| `[a, b] = [b, a]` | `a, b = b, a` |

В Python нет `var`/`let`/`const` — просто присваивание:

```python
name = "Anton"
age = 28

# Переприсвоить можно в любой тип — Python не против
value = 42
value = "теперь строка"    # OK
value = [1, 2, 3]          # OK

# Несколько переменных сразу
x, y, z = 1, 2, 3

# Swap без temp-переменной
a, b = 10, 20
a, b = b, a   # a=20, b=10

# Одно значение многим
p = q = r = 0
```

**Подкапотно:** переменная в Python — это не "ячейка памяти с типом", а **ярлык (label)**, указывающий на объект в памяти. `value = 42` создаёт объект `int(42)`, и ярлык `value` начинает на него указывать. При `value = "строка"` старый `int(42)` удаляется GC, а ярлык переходит на `str`.

**Ловушка:** в Python нет `const`. `UPPER_CASE` — соглашение, не ограничение языка:
```python
MAX_CONNECTIONS = 100
MAX_CONNECTIONS = 999  # Python не бросит ошибку
```

---

## Часть 2: `int` — целые числа

### JS vs Python

В JS `Number` — всегда float (64-bit IEEE 754). `Number.MAX_SAFE_INTEGER = 9_007_199_254_740_991` — дальше теряется точность:
```js
9007199254740992 === 9007199254740993  // true — БАГ!
```

В Python `int` — **отдельный тип**, может расти **бесконечно**, точность не теряется.

```python
population = 8_000_000_000   # _ для читаемости (как в JS с ES2021)
googol = 10 ** 100           # работает точно

# Операторы
10 + 3    # 13
10 - 3    # 7
10 * 3    # 30
10 ** 3   # 1000  (в JS: Math.pow или **)
10 / 3    # 3.333... — ВСЕГДА float!
10 // 3   # 3     — целочисленное деление → int
10 % 3    # 1     — остаток
```

**Важно:** `/` в Python **всегда** возвращает `float`:
```python
type(10 / 2)   # <class 'float'>  → 5.0, не 5!
type(10 // 2)  # <class 'int'>    → 5
```

**Ловушка с отрицательным делением:**
```python
-7 // 2   # -4, не -3!
# Python округляет к минус бесконечности (floor division)
```

**Подкапотно:** в CPython числа от `-5` до `256` кэшируются как синглтоны:
```python
a = 256; b = 256
a is b   # True — один объект в памяти

a = 257; b = 257
a is b   # False — разные объекты
```
Поэтому числа **никогда** не сравнивают через `is`, только через `==`.

---

## Часть 3: `float` — дробные числа

Python `float` = double precision IEEE 754 = JS `Number`. Те же проблемы с точностью:

```python
0.1 + 0.2            # 0.30000000000000004
0.1 + 0.2 == 0.3     # False

# Правильное сравнение:
import math
math.isclose(0.1 + 0.2, 0.3)   # True

# Специальные значения (как в JS):
float('inf')   # бесконечность
float('nan')   # NaN
float('nan') == float('nan')  # False — NaN не равен себе
math.isnan(float('nan'))      # True — правильная проверка
```

### Decimal — когда нужна точность (деньги, финансы)

```python
from decimal import Decimal, ROUND_HALF_UP

# ВАЖНО: аргумент строкой, не float!
price = Decimal("19.99")   # точно
price = Decimal(19.99)     # НЕПРАВИЛЬНО — уже несёт погрешность float

tax_rate = Decimal("0.20")
tax = price * tax_rate     # Decimal * Decimal → OK

# Decimal дружит с int:
doubled = price * 2        # Decimal * int → OK → Decimal('39.98')

# Decimal НЕ дружит с float:
# price * 2.0  → TypeError!

# Получить обычный float обратно:
result = float(price * 2)  # 39.98 — дальше как обычный float

# Точное округление:
rounded = tax.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

**Подкапотно:** `Decimal` хранит число в **десятичной** системе (знак + цифры + экспонента), не в двоичной. Поэтому `0.1` хранится точно. Цена — больше вычислений и памяти. Использовать только для финансов.

---

## Часть 4: `bool` — сюрприз для JS-разработчика

В JS `boolean` — отдельный примитив. В Python `bool` — **подкласс `int`**:

```python
isinstance(True, int)   # True!
True == 1               # True
False == 0              # True
True + True             # 2
True * 10               # 10
```

**Реальный use-case:**
```python
scores = [85, 92, 40, 78, 95]
passed = sum(score >= 70 for score in scores)  # True считается как 1
print(f"Сдали: {passed} из {len(scores)}")     # Сдали: 4 из 5
```

### Falsy / Truthy

| Falsy | Truthy |
|-------|--------|
| `False`, `0`, `0.0` | Всё остальное |
| `""`, `b""` | `"0"` — непустая строка! |
| `[]`, `{}`, `set()`, `()` | Любая непустая коллекция |
| `None` | |

**Главное отличие от JS:**
```python
bool([])   # False  ← в JS: Boolean([]) === true
bool({})   # False  ← в JS: Boolean({}) === true
bool("0")  # True   ← в JS тоже true, но важно помнить
```

**Питоновский идиом для проверки пустоты:**
```python
items = []
if not items:       # правильно
    print("Пусто")

if len(items) == 0: # многословно, не по-питоновски
    print("Пусто")
```

**Ловушка:** `isinstance(True, int)` — `True`, поэтому:
```python
def process(value):
    if isinstance(value, int):
        print(f"Число: {value}")

process(True)   # Число: True — неожиданно!

# Если важно различать — type() is:
if type(value) is int:   # строгая проверка без наследования
    ...
```

---

## Часть 5: `None`

В JS два пустых значения: `null` (явное) и `undefined` (не инициализировано). В Python только **`None`** — единый синглтон.

```python
result = None

# Правильная проверка — через `is` (PEP 8):
if result is None:
    print("Нет значения")

if result is not None:
    print("Есть значение")

# `== None` тоже работает, но `is None` — стандарт
```

**Паттерн опционального аргумента:**
```python
def create_user(name: str, role: str | None = None):
    if role is None:
        role = "user"
    return {"name": name, "role": role}

create_user("Anton")          # {'name': 'Anton', 'role': 'user'}
create_user("Admin", "admin") # {'name': 'Admin', 'role': 'admin'}
```

**Подкапотно:** `None` — синглтон класса `NoneType`. `id(None)` одинаков везде в процессе. Именно поэтому `is None` корректнее `== None`.

**Ловушка:**
```python
def do_something():
    x = 1 + 1
    # нет return!

result = do_something()
print(result)   # None — не ошибка, но частый источник багов
```

---

## Часть 6: Type Hints — аннотации типов

Как TypeScript, но:
1. Полностью **опциональные**
2. **Не проверяются** Python в runtime
3. Используются IDE, `mypy`, `pyright` для статического анализа

```python
def add(a: int, b: int) -> int:
    return a + b

def find_user(user_id: int) -> dict | None:  # Python 3.10+
    if user_id == 1:
        return {"name": "Anton"}
    return None

def process(value: int | str) -> str:        # вместо Union[int, str]
    return str(value)

# Аннотации переменных:
counter: int = 0
username: str = "anton"
```

Python **не бросит ошибку** при несовпадении типов — только `mypy`/`pyright` увидят проблему.

**Подкапотно:** аннотации хранятся в `__annotations__`:
```python
print(add.__annotations__)
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

---

## Часть 7: Встроенные функции для типов

```python
# Узнать тип:
type(42)        # <class 'int'>
type(None)      # <class 'NoneType'>

# Проверка с учётом наследования:
isinstance(True, int)          # True (bool наследует int!)
isinstance(42, (int, str))     # True — проверка против кортежа

# Строгая проверка без наследования:
type(True) is bool   # True
type(True) is int    # False

# Приведение типов:
int("42")      # 42
int(3.9)       # 3  — truncate, не round!
float(42)      # 42.0
str(100)       # "100"
bool([])       # False
bool("false")  # True — непустая строка!
```

**Ловушка: `int()` vs `round()`:**
```python
int(3.9)    # 3  — отрезает дробь
round(3.9)  # 4  — округляет
round(3.5)  # 4
round(2.5)  # 2  — banker's rounding! Округляет к чётному числу
```

---

## Задачи

**Задача 1 (лёгкая):** Напиши функцию `format_price(amount: float, currency: str = "USD") -> str`, которая принимает сумму и валюту, и возвращает строку вида `"19.99 USD"`. Используй `Decimal` для точности и `f-string` для форматирования. Проверь что `format_price(19.987)` возвращает `"19.99 USD"` (округление до 2 знаков).

**Задача 2 (средняя):** Напиши функцию `stats(numbers: list) -> dict`, которая принимает список чисел и возвращает словарь с ключами: `total` (сумма), `count` (кол-во), `positive` (кол-во положительных), `has_none` (есть ли None в списке). Список может содержать `int`, `float` и `None`. `None` не входит в сумму и count.

**Задача 3 (с подвохом):** Что выведет следующий код и почему?
```python
a = 1000
b = 1000
print(a is b)

def check():
    x = 1000
    y = 1000
    print(x is y)

check()
```
Объясни разницу между двумя вызовами `is`. Запусти и проверь — результат может тебя удивить.

---

## Конспект: Переменные и типы

### Суть
В Python переменная — это **ярлык (label)** на объект в памяти, а не ячейка с фиксированным типом. Тип принадлежит объекту, а не переменной — поэтому одному имени можно присвоить сначала `int`, потом `str`. Тип проверяется в runtime, type hints — только для IDE и статических анализаторов (`mypy`, `pyright`), Python их не исполняет.

Два главных сюрприза для JS-разработчика: `bool` является **подклассом `int`** (`True == 1`, `False == 0`), и пустые коллекции (`[]`, `{}`) — **falsy** (в JS они truthy). `None` — единственный "пустой" тип, синглтон, проверяется через `is`, а не `==`.

---

### JS → Python

| JavaScript | Python | Отличие |
|-----------|--------|---------|
| `let x = 1` / `const x = 1` | `x = 1` | Нет ключевых слов объявления |
| `const` — защита от перезаписи | `UPPER_CASE` — только соглашение | Python не запрещает перезапись "констант" |
| `Number` (всегда 64-bit float) | `int` + `float` | `int` в Python — бесконечной точности, не переполняется |
| `9007199254740992 === 9007199254740993 // true` | `10**100` работает точно | JS теряет точность на больших числах |
| `10 / 2 === 5` (number) | `10 / 2 == 5.0` (float) | `/` в Python **всегда** возвращает `float` |
| нет аналога | `10 // 3 == 3` | Целочисленное деление — отдельный оператор `//` |
| `Math.pow(2, 10)` / `2**10` (ES2016) | `2 ** 10` | Оператор степени |
| `null` + `undefined` | `None` | Одно значение вместо двух |
| `Boolean([]) === true` | `bool([]) == False` | Пустые коллекции — falsy |
| `Boolean({}) === true` | `bool({}) == False` | Пустой dict — falsy |
| `typeof true === 'boolean'` | `isinstance(True, int) == True` | `bool` наследует `int` |
| `const [a, b] = [1, 2]` | `a, b = 1, 2` | Деструктуризация без ключевых слов |
| `[a, b] = [b, a]` | `a, b = b, a` | Swap без temp-переменной |

---

### Синтаксис / API

```python
# --- Переменные ---
x = 42                    # присваивание, нет let/const
x: int = 42               # с аннотацией типа
a, b = 1, 2               # множественное присваивание
a, b = b, a               # swap без temp
p = q = r = 0             # одно значение нескольким

# --- int ---
10 // 3                   # 3   — целочисленное деление (результат int)
10 % 3                    # 1   — остаток
2 ** 10                   # 1024 — степень
10 / 2                    # 5.0 — ВСЕГДА float!
-7 // 2                   # -4  — floor division (к минус бесконечности)
1_000_000                 # читаемая запись числа (как JS ES2021)

# --- float ---
import math
math.isclose(0.1 + 0.2, 0.3)          # True — правильное сравнение float
math.isclose(a, b, rel_tol=1e-9)      # с заданной точностью
float('inf')                           # бесконечность
math.isnan(float('nan'))               # True — проверка NaN

# --- Decimal ---
from decimal import Decimal, ROUND_HALF_UP
Decimal("0.1")                         # точная дробь (строкой!)
Decimal(str(amount))                   # конвертация из float через str
price * Decimal("0.2")                 # Decimal * Decimal → OK
price * 2                              # Decimal * int → OK
float(price)                           # обратно в float
price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # округление

# --- bool ---
True + True                            # 2 — bool это int!
sum(x > 0 for x in nums)              # подсчёт True через sum
bool([])                               # False — пустая коллекция falsy
if not items:                          # питоновский идиом проверки пустоты

# --- None ---
x is None                              # правильная проверка (PEP 8)
x is not None                          # проверка наличия значения
def f(x: str | None = None): ...       # опциональный аргумент

# --- type checking ---
type(x)                                # <class 'int'> — узнать тип
isinstance(x, int)                     # True/False — с учётом наследования
isinstance(x, (int, str))             # проверка против кортежа типов
type(x) is int                         # строгая проверка без наследования

# --- Приведение типов ---
int("42")                              # 42
int(3.9)                               # 3 (truncate, не round!)
round(3.9)                             # 4
round(2.5)                             # 2 (banker's rounding!)
float("3.14")                          # 3.14
str(100)                               # "100"
bool("false")                          # True (непустая строка!)

# --- Type hints ---
def add(a: int, b: int) -> int: ...    # функция
def f(x: int | str) -> str: ...        # union (Python 3.10+)
def f(x: str | None = None): ...       # опционально
add.__annotations__                    # {'a': int, 'b': int, 'return': int}
```

---

### Подкапотно

**Переменная как ярлык:**
CPython хранит объекты в куче (heap). Переменная — это запись в словаре пространства имён (`locals()` / `globals()`), которая указывает на адрес объекта. При `x = 42` создаётся объект `int(42)` в памяти, и в словарь пространства имён записывается `{"x": <адрес объекта>}`. При `x = "str"` ярлык переезжает, старый объект подпадает под GC если на него нет других ссылок.

**Кэш маленьких int (-5..256):**
CPython при старте создаёт 262 объекта `int` (от -5 до 256) и держит их постоянно в памяти. Любой `int` в этом диапазоне — один и тот же объект:
```python
a = 256; b = 256; a is b   # True — один объект
a = 257; b = 257; a is b   # False — разные объекты
```
Внутри функции компилятор может оптимизировать и сделать `is True` даже для больших чисел — поведение непредсказуемо. **Никогда не сравнивай числа через `is`**.

**bool наследует int:**
`bool` — это подкласс `int` в иерархии классов CPython. `True` хранится как `int(1)`, `False` как `int(0)`. Поэтому `True + True == 2` — это не магия, а обычная арифметика int.

**None как синглтон:**
`NoneType` намеренно устроен так, что его нельзя инстанцировать повторно. `id(None)` одинаков в любой точке программы. Именно это делает `is None` надёжным: ты сравниваешь адрес объекта, а не значение.

**Decimal — десятичная арифметика:**
Обычный `float` хранится в двоичной системе (IEEE 754), из-за чего `0.1` не представимо точно. `Decimal` хранит число как тройку `(знак, цифры, экспонента)` в **десятичной** системе — поэтому `Decimal("0.1")` точно. Цена — ~50x медленнее float и больше памяти.

**Type hints в runtime:**
Аннотации хранятся в `__annotations__` как обычный `dict` и доступны в runtime, но Python их **не исполняет**. Функция с `-> str` может вернуть `int` — ошибки не будет. Проверку делают `mypy`/`pyright` статически или `beartype`/`pydantic` в runtime.

---

### Ловушки

**1. `Decimal` из float — скрытая погрешность:**
```python
Decimal(0.1)          # НЕПРАВИЛЬНО: Decimal('0.1000000000000000055511...')
Decimal("0.1")        # правильно:   Decimal('0.1')
Decimal(str(amount))  # правильно: если amount — переменная float
```

**2. `/` всегда возвращает float:**
```python
10 / 2        # 5.0 — float, не int!
10 // 2       # 5   — int, если нужно целое
type(10 / 2)  # <class 'float'>
```

**3. Отрицательное целочисленное деление:**
```python
-7 // 2   # -4, не -3! (floor — к минус бесконечности)
7 // -2   # -4, не -3! (тоже floor)
# В JS: Math.trunc(-7/2) === -3 (к нулю — другая логика!)
```

**4. `int()` — это truncate, не round:**
```python
int(3.9)    # 3  — отбрасывает дробь
int(-3.9)   # -3 — тоже отбрасывает (не -4!)
round(3.9)  # 4  — округляет
round(2.5)  # 2  — banker's rounding: к ближайшему чётному!
round(3.5)  # 4  — к чётному
```

**5. `isinstance(True, int)` — True:**
```python
def process(value):
    if isinstance(value, int):   # bool сюда тоже попадёт!
        return value * 2

process(True)   # 2 — неожиданно?

# Решение — строгая проверка:
if type(value) is int:   # bool не пройдёт
    ...
```

**6. Пустые коллекции — falsy (в отличие от JS):**
```python
bool([])   # False  ← JS: Boolean([]) === true
bool({})   # False  ← JS: Boolean({}) === true
bool(())   # False
bool(set()) # False
# Непустые — truthy: bool([0]) == True, bool({0: 0}) == True
```

**7. Функция без `return` возвращает `None`:**
```python
def save_user(user):
    db.save(user)
    # забыли return user

result = save_user(user)
result.name   # AttributeError: 'NoneType' object has no attribute 'name'
```

**8. `is` ненадёжен для чисел вне кэша (-5..256):**
```python
a = 1000; b = 1000
a is b   # False в глобальном скопе
# НО:
def check():
    x = 1000; y = 1000
    x is y   # может быть True! (оптимизация компилятора)
# Вывод: всегда используй == для сравнения чисел
```

---

### Когда использовать

| Инструмент | Когда |
|-----------|-------|
| `int` | Счётчики, индексы, ID, всё что не требует дроби |
| `float` | Координаты, проценты, физические величины — там где небольшая погрешность допустима |
| `Decimal` | Деньги, налоги, финансовые расчёты — где погрешность недопустима |
| `math.isclose()` | Сравнение float в тестах, бизнес-логике, алгоритмах |
| `bool` как int | Подсчёт истинных значений через `sum()` — питоновская идиома |
| `is None` / `is not None` | Везде где проверяется опциональное значение (параметры, результаты БД) |
| `type(x) is int` | Когда нужно отличить `bool` от `int` (редко, но бывает) |
| `isinstance(x, T)` | Проверка типа в функциях с полиморфным входом |
| `if not items:` | Проверка пустоты коллекции — вместо `len(x) == 0` |
| Type hints | Всегда в публичных функциях и классах — для IDE и `mypy` |

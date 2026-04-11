# Тема 1.9 — Управляющие конструкции

## if / elif / else

В Python нет `{}` — блоки определяются отступами. `else if` → `elif`.

```python
x = 42

if x > 100:
    print("big")
elif x > 10:
    print("medium")   # выведет это
else:
    print("small")
```

**JS-аналогия:** то же самое, но без скобок вокруг условия и без фигурных скобок.

```python
# Python:               аналог в JS:
and                   # &&
or                    # ||
not                   # !

if x > 0 and x < 100 and not done:
    ...
```

**Питоновская фишка — chained comparison (в JS такого нет):**

```python
if 0 < x < 100:   # читается как математика
    ...
# JS: x > 0 && x < 100
```

**Подкапотно:** `0 < x < 100` разворачивается в `0 < x and x < 100`, `x` вычисляется один раз.

**Используется:** везде. Chained comparison особенно удобен для проверки диапазонов — валидация входных данных, границы индексов.

---

## Тернарный оператор

```python
label = "positive" if x > 0 else "negative"
# JS: const label = x > 0 ? "positive" : "negative"

# Порядок: значение_если_true  if  условие  else  значение_если_false
```

**Ловушка:** порядок обратный относительно JS. Новички пишут `x > 0 ? a : b` и получают SyntaxError.

```python
# Можно вкладывать, но лучше не злоупотреблять:
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

**Используется:** короткие присваивания, аргументы функций, list comprehensions.

---

## match / case (Python 3.10+)

Это не просто `switch` — это **structural pattern matching**. Намного мощнее.

### Простой случай — как switch

```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not found")
    case 500:
        print("Server error")
    case _:           # default — wildcard
        print("Unknown")
```

### Деструктуризация tuple

```python
point = (1, 0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On X axis at {x}")   # x захватывается из значения
    case (0, y):
        print(f"On Y axis at {y}")
    case (x, y):
        print(f"Point at {x}, {y}")
```

**JS-аналог:** деструктуризация в `switch` в JS недоступна — там нет аналога.

### Деструктуризация dict

```python
response = {"status": 200, "data": [1, 2, 3]}

match response:
    case {"status": 200, "data": data}:
        print(f"Success: {data}")
    case {"status": 404}:
        print("Not found")
    case {"status": code}:
        print(f"Error code: {code}")
```

**Важно:** `case {"status": 404}` сработает даже если в словаре есть другие ключи — dict-паттерн проверяет наличие ключей, а не точное совпадение.

### Guard — явное условие в case

```python
match value:
    case x if x > 0:    # guard: сработает только если x > 0
        print(f"Positive: {x}")
    case x if x < 0:
        print(f"Negative: {x}")
    case _:
        print("Zero")
```

### OR в паттернах

```python
match status:
    case 400 | 401 | 403:   # несколько значений через |
        print("Client error")
    case 500 | 502 | 503:
        print("Server error")
```

**Ловушка — переменная в case это захват, не сравнение:**

```python
x = 5
match value:
    case x:   # ЗАХВАТЫВАЕТ value в x, не сравнивает с x=5!
        ...   # сработает всегда — это как default

# Правильно — guard:
match value:
    case v if v == x:
        ...
```

**Подкапотно:** match/case компилируется в байткод эффективнее цепочки if/elif — интерпретатор может строить jump-таблицу для литеральных значений.

**Используется:** обработка команд CLI, парсинг API-ответов, state machine, роутинг событий в event-driven архитектуре.

---

## Конспект

### Суть
Python использует отступы вместо `{}`. `elif` вместо `else if`. Тернарный оператор имеет обратный порядок относительно JS. `match/case` — структурный паттерн-матчинг с деструктуризацией, намного мощнее `switch`.

### Python → JS
| Python | Что делает | JavaScript |
|---|---|---|
| `elif` | ветка условия | `else if` |
| `and` / `or` / `not` | логические операторы | `&&` / `\|\|` / `!` |
| `0 < x < 10` | chained comparison | `x > 0 && x < 10` |
| `a if x else b` | тернарный оператор | `x ? a : b` |
| `match/case` | структурный паттерн-матчинг | `switch/case` (слабее) |
| `case (x, 0):` | деструктуризация + захват | нет аналога |

### Синтаксис / API

```python
# if/elif/else
if x > 0:
    ...
elif x == 0:
    ...
else:
    ...

# chained comparison
if 0 < x < 100: ...

# тернарный
result = "yes" if condition else "no"

# match/case — литералы
match status:
    case 200: ...
    case 404: ...
    case _: ...         # default / wildcard

# match/case — OR паттерн
match status:
    case 400 | 401 | 403: ...

# match/case — деструктуризация tuple
match point:
    case (0, 0): ...
    case (x, 0): ...    # x захватывается

# match/case — dict
match data:
    case {"status": 200, "data": d}: ...

# guard — явное условие в case
match value:
    case v if v > 0: ...
```

### Ловушки

```python
# 1. Тернарный — обратный порядок
result = "yes" if condition else "no"   # НЕ condition ? "yes" : "no"

# 2. case с переменной — захват, не сравнение
x = 5
match val:
    case x: ...   # захватит val в x, сработает всегда!
    # правильно:
    case v if v == x: ...

# 3. Порядок case важен — более специфичные паттерны выше
match point:
    case (x, y): ...    # если поставить первым — поглотит все остальные
    case (0, 0): ...    # никогда не сработает!

# 4. match/case требует Python 3.10+ — на 3.9 SyntaxError
```

### Когда использовать
- `if/elif/else` — стандартная ветвящаяся логика
- тернарный — короткие однострочные присваивания, аргументы функций
- `match/case` — парсинг команд/событий, обработка API-ответов, state machine, роутинг
- chained comparison — проверка диапазонов (валидация, границы)

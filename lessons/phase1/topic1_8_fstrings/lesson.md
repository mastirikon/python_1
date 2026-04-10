# Тема 1.8 — f-strings

---

## 1. Базовый синтаксис

**JS-аналогия:** Template literals в JS — `` `Hello, ${name}!` `` → в Python: `f"Hello, {name}!"`

Отличия:
- Префикс `f` перед строкой (или `F` — оба работают)
- Фигурные скобки `{}` вместо `${}`
- Внутри `{}` — любое Python-выражение, не только переменная

```python
name = "Anton"
age = 30

# JS: `Hello, ${name}! You are ${age} years old.`
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Hello, Anton! You are 30 years old.

# Выражения прямо внутри {}
print(f"Next year: {age + 1}")     # Next year: 31
print(f"Upper: {name.upper()}")    # Upper: ANTON
print(f"Type: {type(age)}")        # Type: <class 'int'>
```

**Подкапотно:** f-string — это не строковая операция во время компиляции (как в C#), а вычисление выражений в runtime. Интерпретатор компилирует f-string в серию конкатенаций через `str()` под капотом. Быстрее `%`-форматирования и `.format()` — потому что нет парсинга строки в runtime.

**Ловушки:**
```python
# Нельзя использовать тот же тип кавычек внутри {} (до Python 3.12)
name = "Anton"
# print(f"Hello, {"Anton"}")  # SyntaxError в Python < 3.12

# Решение — другой тип кавычек
print(f"Hello, {'Anton'}")    # OK
print(f'Hello, {"Anton"}')    # OK

# В Python 3.12+ — можно любые кавычки внутри {}
```

---

## 2. Форматирование чисел

**JS-аналогия:** В JS для форматирования чисел нужен `toFixed()`, `toLocaleString()` или `Intl.NumberFormat`. В Python — форматные спецификаторы прямо внутри `{}` через двоеточие: `{value:spec}`.

```python
pi = 3.14159265
price = 1234567.89
ratio = 0.1234

# Количество знаков после запятой
print(f"{pi:.2f}")          # 3.14
print(f"{pi:.4f}")          # 3.1416  (с округлением!)

# Ширина поля (выравнивание)
print(f"{42:10d}")          # '        42'  (правое выравнивание, ширина 10)
print(f"{42:<10d}")         # '42        '  (левое)
print(f"{42:^10d}")         # '    42    '  (центр)
print(f"{'hi':^10}")        # '    hi    '

# Заполнитель
print(f"{42:0>10d}")        # '0000000042'
print(f"{42:*^10d}")        # '****42****'

# Разделитель тысяч
print(f"{price:,.2f}")      # 1,234,567.89
print(f"{price:_.2f}")      # 1_234_567.89  (Python 3.6+)

# Проценты
print(f"{ratio:.1%}")       # 12.3%

# Экспоненциальная нотация
print(f"{0.000123:.2e}")    # 1.23e-04

# Бинарное, октальное, hex представление
n = 255
print(f"{n:b}")             # 11111111
print(f"{n:o}")             # 377
print(f"{n:x}")             # ff
print(f"{n:X}")             # FF
print(f"{n:#x}")            # 0xff  (с префиксом)
```

**Используется:** форматирование денежных сумм, процентов, вывод таблиц с выравниванием, логирование числовых метрик.

---

## 3. Отладочный режим `=` (Python 3.8+)

**JS-аналогия:** В JS пишут `console.log("value:", value)` или `console.log({ value })`. В Python 3.8+ появился `f"{value=}"` — выводит и имя переменной, и её значение.

```python
x = 42
name = "Anton"
items = [1, 2, 3]

# Без =: просто значение
print(f"{x}")           # 42

# С =: имя переменной + значение (убийца print-дебаггинга)
print(f"{x=}")          # x=42
print(f"{name=}")       # name='Anton'
print(f"{items=}")      # items=[1, 2, 3]

# Работает с выражениями!
print(f"{x * 2=}")      # x * 2=84
print(f"{len(items)=}") # len(items)=3
print(f"{x > 10=}")     # x > 10=True

# Можно комбинировать с форматированием
pi = 3.14159
print(f"{pi=:.2f}")     # pi=3.14

# Типичный паттерн при дебаггинге функции:
def calculate(a, b):
    result = a * b + a
    print(f"{a=}, {b=}, {result=}")  # a=3, b=4, result=15
    return result

calculate(3, 4)
```

**Подкапотно:** `f"{x=}"` — это синтаксический сахар, который Python разворачивает в `"x=" + repr(x)`. Именно `repr()`, а не `str()` — поэтому строки выводятся с кавычками (`name='Anton'`), а не без.

**Ловушки:**
```python
name = "Anton"
print(f"{name}")    # Anton      (str())
print(f"{name=}")   # name='Anton'  (repr() — с кавычками!)
```

---

## 4. `!r`, `!s`, `!a` — явный вызов repr/str/ascii

```python
name = "Антон"
pi = 3.14159

# !s — вызывает str() (по умолчанию)
print(f"{name!s}")   # Антон

# !r — вызывает repr() (как f"{name=}" для значения)
print(f"{name!r}")   # 'Антон'  (с кавычками)
print(f"{pi!r}")     # 3.14159

# !a — вызывает ascii() — не-ASCII символы экранируются
print(f"{name!a}")   # '\u0410\u043d\u0442\u043e\u043d'
```

**Используется:** `!r` — при логировании строк, когда важно видеть кавычки и спецсимволы; `!a` — при отладке Unicode-проблем.

---

## 5. Многострочные f-strings и вложенность

```python
# Многострочный f-string
user = {"name": "Anton", "age": 30, "city": "Moscow"}

report = f"""
User Report:
  Name: {user['name']}
  Age:  {user['age']}
  City: {user['city']}
"""
print(report)

# Вложенные выражения
items = [3, 1, 4, 1, 5, 9]
print(f"Max: {max(items)}, Min: {min(items)}, Sum: {sum(items)}")

# Условие внутри {}
score = 75
print(f"Result: {'pass' if score >= 60 else 'fail'}")  # Result: pass

# Вызов функции внутри {}
def greet(n): return f"Hey, {n}"
print(f"Message: {greet('world')}")  # Message: Hey, world

# Вложенные f-strings (редко нужны, но работают)
width = 10
value = 42
print(f"{value:{width}d}")   # '        42'  — ширина из переменной
```

---

## 6. f-string vs другие способы форматирования

```python
name, age = "Anton", 30

# 1. % — старый стиль (C-style), не используй в новом коде
print("Hello, %s! Age: %d" % (name, age))

# 2. .format() — Python 2.6+, многословно
print("Hello, {}! Age: {}".format(name, age))
print("Hello, {name}! Age: {age}".format(name=name, age=age))

# 3. f-string — Python 3.6+, рекомендуемый способ
print(f"Hello, {name}! Age: {age}")

# Когда .format() всё ещё нужен:
# — шаблон приходит как строка (из конфига, БД)
template = "Hello, {name}!"
print(template.format(name=name))  # f-string здесь не поможет

# — i18n / локализация: строки переводятся, f-string не подходит
```

**Подкапотно:** Скорость форматирования: f-string ≈ % > .format(). f-string быстрее `.format()` примерно в 2 раза, потому что не нужно парсить строку-шаблон в runtime.

---

## Конспект: f-strings

### Суть
f-strings — рекомендуемый способ форматирования строк в Python 3.6+. Аналог template literals в JS (`\`${}\``), но с двоеточием для форматных спецификаторов. Вычисляются в runtime, поддерживают любые выражения внутри `{}`. Быстрее `.format()` и `%`-форматирования.

### JS → Python

| Python | Что делает | JavaScript |
|--------|-----------|------------|
| `f"Hello, {name}"` | Подстановка переменной | `` `Hello, ${name}` `` |
| `f"{x + 1}"` | Выражение в строке | `` `${x + 1}` `` |
| `f"{pi:.2f}"` | Форматный спецификатор | `pi.toFixed(2)` |
| `f"{n:,}"` | Разделитель тысяч | `n.toLocaleString()` |
| `f"{x=}"` | Имя + значение (дебаг) | `console.log({x})` (частичный аналог) |
| `f"{s!r}"` | repr() строки | `JSON.stringify(s)` (частичный аналог) |
| `"Hello, {name}".format(name=n)` | Шаблон из переменной | нет прямого аналога |

### Синтаксис / API

```python
# Базовый
f"{expr}"               # str(expr)

# Форматирование чисел
f"{pi:.2f}"             # 2 знака после запятой → "3.14"
f"{n:d}"                # целое
f"{n:05d}"              # с ведущими нулями → "00042"
f"{n:10d}"              # ширина поля 10, правое выравнивание
f"{n:<10d}"             # левое выравнивание
f"{n:^10d}"             # центрирование
f"{n:,}"                # разделитель тысяч → "1,234,567"
f"{r:.1%}"              # проценты → "12.3%"
f"{n:#x}"               # hex с префиксом → "0xff"
f"{n:b}"                # бинарное → "11111111"

# Отладка (Python 3.8+)
f"{x=}"                 # "x=42" — repr(x) с именем переменной
f"{x=:.2f}"             # "x=3.14" — с форматированием

# Модификаторы
f"{s!s}"                # str(s) — явно
f"{s!r}"                # repr(s) — с кавычками
f"{s!a}"                # ascii(s) — экранировать не-ASCII

# Условие внутри {}
f"{'yes' if cond else 'no'}"

# Ширина из переменной
f"{value:{width}.{precision}f}"

# Многострочный
f"""
  Name: {name}
  Age:  {age}
"""
```

### Подкапотно
- f-string компилируется в байткод как серия конкатенаций через `str()` — без парсинга строки в runtime
- `f"{x=}"` разворачивается в `"x=" + repr(x)` — поэтому строки с кавычками
- Скорость: f-string > % > .format() — .format() медленнее, т.к. парсит шаблон в runtime
- До Python 3.12: нельзя использовать одинаковые кавычки внутри `{}` и снаружи
- Python 3.12+: ограничение снято, любые кавычки внутри `{}`

### Ловушки

```python
# 1. Кавычки (до 3.12)
name = "Anton"
# f"Hello {"Anton"}"   # SyntaxError
f"Hello {'Anton'}"     # OK — другой тип кавычек

# 2. f"{x=}" использует repr(), не str()
s = "hello"
f"{s}"    # hello       (str)
f"{s=}"   # s='hello'   (repr — с кавычками!)

# 3. f-string не подходит для шаблонов из переменных
template = "Hello, {name}!"
# f"{template}"  # выведет строку как есть, не подставит name
template.format(name="Anton")  # правильно

# 4. Обратный слэш нельзя использовать внутри {} (до 3.12)
items = ["a", "b"]
# f"{'\n'.join(items)}"  # SyntaxError
sep = "\n"
f"{sep.join(items)}"    # OK — через переменную
```

### Когда использовать
- **f-string** — для всего нового кода: логи, вывод, сборка строк
- **`.format()`** — когда шаблон приходит как строка (из конфига, БД, i18n)
- **`%`** — только при поддержке legacy-кода, нигде больше
- **`f"{x=}"`** — вместо `print("x =", x)` при отладке
- **`f"{n:,.2f}"`** — форматирование денег, чисел с разделителями
- **`f"{r:.1%}"`** — вывод процентов из долей (0.123 → "12.3%")

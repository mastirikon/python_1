# Тема 1.7 — Строки: методы, str vs bytes

---

## 1. Поиск и проверка

### `find` / `rfind` / `index`

```python
s = "hello world hello"

s.find("hello")      # 0 — первое вхождение, -1 если нет
s.rfind("hello")     # 12 — последнее вхождение
s.find("xyz")        # -1 — не найдено (не кидает ошибку)
s.index("hello")     # 0 — как find, но кидает ValueError если нет
s.index("xyz")       # ValueError: substring not found

s.find("hello", 5)   # 12 — искать начиная с позиции 5
s.find("hello", 5, 15)  # 12 — искать в диапазоне [5, 15)
```

**JS-аналогия:** `indexOf` → `find`, `lastIndexOf` → `rfind`. Разница: в JS `-1` при неудаче, в Python то же самое — но `index()` кидает исключение.

**Используется:** парсинг, поиск позиции для вставки/замены, валидация формата.

---

### `startswith` / `endswith`

```python
s = "hello.py"

s.startswith("hello")   # True
s.endswith(".py")       # True
s.endswith(".js")       # False

# Можно передать кортеж вариантов
s.endswith((".py", ".pyw", ".pyx"))   # True — хотя бы один совпал
"image.jpg".endswith((".jpg", ".png", ".gif"))  # True
```

**JS-аналогия:** `startsWith` / `endsWith` — то же самое. Фича с кортежем — питоновская.

**Используется:** проверка расширений файлов, префиксов URL, протоколов.

---

### `count`

```python
s = "hello world hello"

s.count("hello")    # 2
s.count("l")        # 5
s.count("xyz")      # 0
s.count("l", 5)     # 3 — считать начиная с позиции 5
```

**JS-аналогия:** нет прямого аналога, в JS — `s.split("x").length - 1`.

---

## 2. Трансформация

### `replace`

```python
s = "hello world hello"

s.replace("hello", "hi")         # 'hi world hi' — все вхождения
s.replace("hello", "hi", 1)      # 'hi world hello' — только первое
s.replace("xyz", "abc")          # 'hello world hello' — нет вхождений, без ошибки
```

**JS-аналогия:** `s.replace(/hello/g, "hi")` — в JS без флага `g` заменяет только первое. В Python по умолчанию заменяет все.

**Подкапотно:** возвращает новую строку, оригинал не меняется (иммутабельность).

---

### `split` / `rsplit`

```python
s = "a,b,c,d"

s.split(",")         # ['a', 'b', 'c', 'd']
s.split(",", 2)      # ['a', 'b', 'c,d'] — максимум 2 разбиения
s.rsplit(",", 2)     # ['a,b', 'c', 'd'] — разбивать с конца

# Без аргументов — split по пробельным символам (пробел, \t, \n)
"  hello   world  ".split()    # ['hello', 'world'] — убирает пробелы!
"  hello   world  ".split(" ") # ['', '', 'hello', '', '', 'world', '', ''] — не то!
```

**JS-аналогия:** `split(",")` — то же самое. **Ловушка:** `split()` без аргументов в Python умнее — он разбивает по любым пробельным символам и игнорирует ведущие/конечные пробелы. В JS `"  hi  ".split(" ")` даёт `["", "", "hi", "", ""]`.

**Используется:** парсинг CSV (простой), разбивка путей, токенизация.

---

### `join`

```python
words = ["hello", "world", "python"]

" ".join(words)     # 'hello world python'
",".join(words)     # 'hello,world,python'
"".join(words)      # 'helloworldpython'
"\n".join(words)    # многострочная строка

# Работает с любым итерируемым
"-".join(str(i) for i in range(5))  # '0-1-2-3-4'
```

**JS-аналогия:** `arr.join(" ")` — но в Python разделитель стоит **перед** методом, а массив передаётся **в** метод. Поначалу непривычно.

**Ловушка:** `join` принимает только строки. Если в списке числа — `TypeError`:
```python
",".join([1, 2, 3])            # TypeError
",".join(str(x) for x in [1, 2, 3])  # '1,2,3' — правильно
```

---

### `strip` / `lstrip` / `rstrip`

```python
s = "  \t hello \n  "

s.strip()    # 'hello' — убирает пробельные символы с обоих концов
s.lstrip()   # 'hello \n  ' — только слева
s.rstrip()   # '  \t hello' — только справа

# Можно указать конкретные символы для удаления
"***hello***".strip("*")    # 'hello'
"/path/to/".strip("/")      # 'path/to'
"xxhelloxx".strip("x")      # 'hello'
```

**JS-аналогия:** `trim()` → `strip()`, `trimStart()` → `lstrip()`, `trimEnd()` → `rstrip()`.

**Подкапотно:** `strip(chars)` удаляет **любую комбинацию** указанных символов с краёв, не подстроку:
```python
"abcba".strip("ab")   # 'c' — удаляет 'a' и 'b' с краёв в любом порядке
"abcba".strip("ba")   # 'c' — то же самое
```

**Ловушка:** легко перепутать с удалением подстроки:
```python
"https://example.com".strip("https://")  # 'example.com' — случайно!
# Правильно для удаления префикса — removeprefix (Python 3.9+):
"https://example.com".removeprefix("https://")  # 'example.com'
```

---

### `removeprefix` / `removesuffix` (Python 3.9+)

```python
"hello_world".removeprefix("hello_")   # 'world'
"hello_world".removesuffix("_world")   # 'hello'
"hello_world".removeprefix("xyz")      # 'hello_world' — без изменений
```

В отличие от `strip` — удаляет именно подстроку, а не набор символов.

---

## 3. Регистр

```python
s = "Hello World"

s.lower()       # 'hello world'
s.upper()       # 'HELLO WORLD'
s.title()       # 'Hello World' — каждое слово с заглавной
s.capitalize()  # 'Hello world' — только первый символ строки
s.swapcase()    # 'hELLO wORLD' — инвертировать регистр

# Проверки
"hello".islower()   # True
"HELLO".isupper()   # True
"Hello World".istitle()  # True
```

**JS-аналогия:** `toLowerCase` → `lower()`, `toUpperCase` → `upper()`. `title()` и `capitalize()` — в JS нет встроенных.

---

## 4. Выравнивание и заполнение

```python
s = "hi"

s.ljust(10)         # 'hi        ' — выровнять влево, дополнить пробелами
s.rjust(10)         # '        hi' — выровнять вправо
s.center(10)        # '    hi    ' — по центру
s.ljust(10, "-")    # 'hi--------' — заполнить символом
s.zfill(5)          # '00hi' — заполнить нулями слева (для чисел)

"42".zfill(5)       # '00042'
```

**Используется:** форматирование таблиц в консоли, генерация отчётов, паддинг чисел.

---

## 5. Проверки (`is*` методы)

```python
"hello".isalpha()    # True — все буквы
"hello1".isalpha()   # False
"123".isdigit()      # True — все цифры
"12.3".isdigit()     # False — точка не цифра
"hello world".isalnum()   # False — пробел не буква/цифра
"hello123".isalnum()      # True
"   ".isspace()      # True — все пробельные символы
"Hello".istitle()    # True
```

---

## 6. str vs bytes — подробнее

```python
# str — Unicode текст
s = "Привет"
type(s)    # <class 'str'>

# bytes — последовательность байт 0-255
b = b"Hello"
type(b)    # <class 'bytes'>

# Конвертация
s.encode("utf-8")          # str → bytes
s.encode("utf-16")         # другая кодировка
b.decode("utf-8")          # bytes → str
b.decode("latin-1")        # другая кодировка

# bytearray — мутабельная версия bytes
ba = bytearray(b"hello")
ba[0] = 72                 # можно менять байты
bytes(ba)                  # b'Hello'
```

**Ловушка — кодировки:**
```python
s = "café"
s.encode("utf-8")     # b'caf\xc3\xa9' — 5 байт
s.encode("latin-1")   # b'caf\xe9' — 4 байта
len(s)                # 4 символа во всех случаях
```

**Когда что использовать:**
- `str` — всегда для текста
- `bytes` — сеть (HTTP, TCP), бинарные файлы (изображения, PDF), шифрование, хэши
- `bytearray` — когда нужно модифицировать байты на месте (парсинг бинарных протоколов)

---

---

## Конспект: Строки — методы

### Суть
Python предоставляет богатый набор методов строк, все они возвращают новую строку (иммутабельность). Ключевые отличия от JS: `split()` без аргументов умно обрабатывает пробелы, `replace()` по умолчанию заменяет все вхождения, `strip(chars)` удаляет набор символов а не подстроку.

### Python → JS
| Python | Что делает | JavaScript |
|--------|-----------|-----------|
| `s.find("x")` | индекс первого вхождения или -1 | `indexOf("x")` |
| `s.rfind("x")` | индекс последнего вхождения или -1 | `lastIndexOf("x")` |
| `s.index("x")` | индекс или ValueError | нет прямого аналога |
| `"x" in s` | проверка вхождения | `includes("x")` |
| `s.startswith("x")` | начинается ли с x (принимает tuple) | `startsWith("x")` |
| `s.endswith("x")` | заканчивается ли на x (принимает tuple) | `endsWith("x")` |
| `s.replace("x", "y")` | заменить все вхождения | `replace(/x/g, "y")` |
| `s.replace("x", "y", 1)` | заменить только первое | `replace("x", "y")` |
| `s.split(",")` | разбить по разделителю | `split(",")` |
| `s.split()` | разбить по пробелам, убрать лишние | `trim().split(/\s+/)` |
| `",".join(arr)` | собрать строку из списка | `arr.join(",")` |
| `s.strip()` | убрать пробелы с обоих краёв | `trim()` |
| `s.lstrip()` | убрать пробелы слева | `trimStart()` |
| `s.rstrip()` | убрать пробелы справа | `trimEnd()` |
| `s.lower()` | в нижний регистр | `toLowerCase()` |
| `s.upper()` | в верхний регистр | `toUpperCase()` |
| `s.title()` | каждое слово с заглавной | нет встроенного |
| `s.capitalize()` | только первый символ заглавный | нет встроенного |
| `s.removeprefix("x")` | убрать префикс (3.9+) | нет встроенного |
| `s.removesuffix("x")` | убрать суффикс (3.9+) | нет встроенного |

### Синтаксис / API
```python
# Поиск
s.find("x")           # индекс или -1
s.rfind("x")          # последнее вхождение
s.index("x")          # индекс или ValueError
s.count("x")          # количество вхождений
s.startswith("x")     # bool, принимает tuple
s.endswith("x")       # bool, принимает tuple

# Трансформация
s.replace("a", "b")          # заменить все
s.replace("a", "b", 1)       # заменить первое
s.split(",")                  # по разделителю
s.split()                     # по пробельным символам
",".join(["a", "b"])          # собрать строку
s.strip()                     # убрать пробелы с краёв
s.strip("*")                  # убрать символы с краёв
s.removeprefix("pre")         # убрать префикс (3.9+)
s.removesuffix("suf")         # убрать суффикс (3.9+)

# Регистр
s.lower() / s.upper()
s.title()       # Each Word Capitalized
s.capitalize()  # Only first char

# Выравнивание
s.ljust(10) / s.rjust(10) / s.center(10)
s.zfill(5)      # '00042'

# Проверки
s.isalpha() / s.isdigit() / s.isalnum() / s.isspace()

# str <-> bytes
s.encode("utf-8")    # str → bytes
b.decode("utf-8")    # bytes → str
```

### Подкапотно
- Все методы возвращают **новый объект** `str` — иммутабельность.
- `split()` без аргументов использует специальный алгоритм: разбивает по `\t`, `\n`, `\r`, пробелам, игнорирует ведущие/конечные пробелы.
- `strip(chars)` — удаляет **любую комбинацию** символов из `chars`, не подстроку. Работает слева и справа независимо.
- `join` принимает любой итерируемый, но все элементы должны быть `str`.

### Ловушки
```python
# 1. strip удаляет символы, не подстроку
"https://site.com".strip("https://")  # может срезать лишнее!
"https://site.com".removeprefix("https://")  # правильно (3.9+)

# 2. split(" ") vs split()
"  hi  ".split(" ")   # ['', '', 'hi', '', ''] — плохо
"  hi  ".split()      # ['hi'] — хорошо

# 3. join требует строки
",".join([1, 2, 3])              # TypeError
",".join(str(x) for x in [1, 2, 3])  # '1,2,3'

# 4. replace заменяет все по умолчанию
"aaa".replace("a", "b")    # 'bbb' — не 'baa'!
"aaa".replace("a", "b", 1) # 'baa' — только первое

# 5. index vs find
s.index("xyz")   # ValueError — если не найдено
s.find("xyz")    # -1 — безопаснее
```

### Когда использовать
- `split()` без аргументов — токенизация строк с непредсказуемыми пробелами
- `",".join(list)` — всегда вместо конкатенации в цикле
- `strip()` — очистка пользовательского ввода
- `removeprefix/removesuffix` — безопасное удаление известного префикса/суффикса (3.9+)
- `startswith(tuple)` — проверка нескольких вариантов вместо `or`
- `find` — когда отсутствие не ошибка; `index` — когда отсутствие — баг
- `bytes` / `encode` / `decode` — сеть, файлы, шифрование

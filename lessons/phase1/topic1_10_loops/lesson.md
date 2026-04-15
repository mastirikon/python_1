# Тема 1.10 — Циклы

## for

В Python `for` всегда итерирует по итерируемому объекту — нет классического `for (i=0; i<n; i++)`.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# JS: for (const fruit of fruits)
```

Если нужен индекс — `enumerate`:

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana

# JS: for (const [i, fruit] of fruits.entries())

# Старт индекса можно задать:
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)   # 1 apple, 2 banana, ...
```

Числовой диапазон — `range`:

```python
for i in range(5):          # 0, 1, 2, 3, 4
for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  — шаг 2
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1  — обратный

# JS: for (let i = 0; i < 5; i++)
```

**Подкапотно:** `range` — ленивый объект, не создаёт список. `range(10_000_000)` занимает ~48 байт памяти — хранит только start/stop/step.

**Используется:** итерация по коллекциям, диапазонам, файлам, генераторам — везде.

---

## while

```python
x = 10

while x > 0:
    print(x)
    x -= 2
# JS: while (x > 0) { ... }
```

**Питоновская фишка:** нет `do/while`. Эмулируется через `while True` + `break`:

```python
while True:
    data = input("Введи число: ")
    if data.isdigit():
        break
# JS: do { ... } while (!data.isDigit())
```

---

## break и continue

```python
for i in range(10):
    if i == 3:
        continue   # пропустить итерацию — как в JS
    if i == 7:
        break      # выйти из цикла — как в JS
    print(i)
# 0 1 2 4 5 6
```

Работают так же как в JS — без сюрпризов.

---

## else у цикла — уникальная питоновская фишка

`else` у `for`/`while` выполняется если цикл завершился **без `break`**:

```python
# break не случился — else выполнится:
for i in range(5):
    if i == 10:
        break
else:
    print("не нашли")  # выведет это

# break случился — else не выполнится:
for i in range(5):
    if i == 3:
        break
else:
    print("не выведется")
```

**JS-аналога нет.** В JS нужна флаговая переменная:

```python
# Python — чисто:
for item in items:
    if is_valid(item):
        break
else:
    raise ValueError("не нашли валидный элемент")

# JS — некрасиво:
# let found = false
# for (const item of items) {
#     if (isValid(item)) { found = true; break }
# }
# if (!found) throw new Error("не нашли")
```

**Используется:** поиск в коллекции — цикл ищет элемент, `else` срабатывает если ничего не нашёл.

---

## Вложенные циклы и break

`break` выходит только из **ближайшего** цикла:

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break       # выходит только из внутреннего
    print(i)            # внешний продолжается
# 0 1 2
```

Чтобы выйти из всех уровней сразу — вынеси в функцию и используй `return`:

```python
def find_pair(matrix, target):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == target:
                return (i, j)   # выходим из обоих циклов сразу
    return None
```

---

## Конспект

### Суть
`for` в Python итерирует по объектам, не по индексам. Числовые диапазоны — через `range` (ленивый, не список). `else` у цикла — уникальная фишка Python, срабатывает когда не было `break`. `do/while` нет — заменяется `while True` + `break`.

### Python → JS
| Python | Что делает | JavaScript |
|---|---|---|
| `for x in iterable` | итерация по объекту | `for (const x of iterable)` |
| `for i, x in enumerate(lst)` | итерация с индексом | `for (const [i, x] of lst.entries())` |
| `range(n)` | ленивый диапазон 0..n-1 | `Array.from({length: n}, (_, i) => i)` |
| `range(a, b, step)` | диапазон с шагом | `for (let i=a; i<b; i+=step)` |
| `while cond` | цикл с условием | `while (cond)` |
| `while True` + `break` | do/while эмуляция | `do { } while (cond)` |
| `for ... else` | блок если не было break | нет аналога |
| `break` / `continue` | выход / пропуск итерации | `break` / `continue` |

### Синтаксис / API

```python
# for по коллекции
for x in collection: ...

# for с индексом
for i, x in enumerate(collection): ...
for i, x in enumerate(collection, start=1): ...

# range
range(stop)
range(start, stop)
range(start, stop, step)

# while
while condition: ...

# do/while через while True
while True:
    ...
    if condition:
        break

# break / continue
for x in collection:
    if ...: continue
    if ...: break

# else у цикла
for x in collection:
    if found(x):
        break
else:
    # сработает если break не было
    ...
```

### Ловушки

```python
# 1. Изменение списка во время итерации — пропускает элементы
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        items.remove(item)  # ПЛОХО
# Правильно: итерировать по копии
for item in items[:]:
    ...

# 2. range не включает конец
range(1, 5)  # 1, 2, 3, 4 — без 5

# 3. else у цикла НЕ означает "если коллекция пустая"
for x in []:
    ...
else:
    print("сработает!")  # break не было — else выполнится

# 4. break выходит только из ближайшего цикла
for i in range(3):
    for j in range(3):
        break   # только внутренний, внешний продолжается
```

### Когда использовать
- `for` — итерация по коллекции, всегда предпочтительнее `while`
- `while` — когда число итераций неизвестно заранее (ввод, polling, парсинг)
- `for/else` — поиск элемента без флаговой переменной
- `range` — числовые диапазоны, повторение N раз
- `while True` + `break` — бесконечный цикл с выходом по условию

# 1.3 — `bool` как подкласс `int`

## bool — это int

`bool` в Python — не отдельный тип, а **подкласс `int`**. `True` и `False` — буквально целые числа `1` и `0`.

```python
isinstance(True, int)   # True
isinstance(False, int)  # True

type(True)   # <class 'bool'>
type(1)      # <class 'int'>

True == 1    # True
False == 0   # True

True is 1    # False  ← разные объекты, просто равны по значению
```

**Подкапотно:** `bool` наследует весь арифметический протокол `int`. Интерпретатор не делает никакого кастинга — `True` физически хранится как `int` со значением `1`.

---

## Арифметика с bool

```python
True + True        # 2
True + False       # 1
True * 5           # 5
False * 100        # 0

sum([True, True, False, True])  # 3
```

**Реальный use-case** — подсчёт количества выполненных условий:

```python
scores = [85, 42, 91, 67, 55]

passing = sum(score >= 60 for score in scores)
print(passing)  # 3
```

`sum()` по генератору булевых значений = подсчёт True — питоновская идиома.

---

## Тип результата арифметики

```python
type(True + True)   # <class 'int'>  ← не bool!
type(True or True)  # <class 'bool'>
```

Арифметика возвращает `int`, логические операторы — `bool`.

---

## Ловушки

### 1. isinstance не отличает bool от int

```python
isinstance(True, int)  # True — bool проходит проверку

# Если нужно явно отклонить bool:
type(value) is not int  # bool не пройдёт
```

### 2. bool в словаре — перезапись ключей

```python
d = {1: "один", True: "правда"}
print(d)  # {1: 'правда'}  ← True == 1, ключ перезаписался!

d = {0: "ноль", False: "ложь"}
print(d)  # {0: 'ложь'}
```

### 3. bool(-1) это True

```python
bool(-1)   # True  ← не только 1!
bool(-42)  # True

x = -1
if x:
    print("истина")  # напечатает
```

### 4. bool в индексах (антипаттерн)

```python
data = ["нет", "да"]
data[True]   # "да"  — работает, но не пиши так
```

---

## Truthy / Falsy

```python
# Falsy:
bool(0), bool(0.0), bool(""), bool([]), bool({}), bool(None)  # всё False

# Truthy — всё остальное:
bool(-1)    # True
bool("  ")  # True  ← строка с пробелом не пустая
bool([0])   # True  ← список с элементом
```

---

## Задачи

Сохраняй решения в `lessons/phase1/topic1_3_bool/task_1.py`, `task_2.py`, `task_3.py`

**Задача 1 (лёгкая).** Напиши функцию `count_passing(scores: list[int], threshold: int) -> int`,
которая считает количество оценок, строго превышающих порог.
Используй `sum()` с генератором — без `for`-цикла и счётчика.

**Задача 2 (средняя).** Напиши функцию `first_true(values: list) -> int`,
которая возвращает индекс первого truthy-значения в списке.
Если таких нет — вернуть `-1`. Подсказка: `enumerate`.

**Задача 3 (с подвохом).** Что выведет этот код и почему? Объясни в комментариях:

```python
d = {}
d[False] = "zero"
d[0] = "int zero"
d[0.0] = "float zero"
print(d)
print(len(d))
```

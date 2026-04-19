# 1.13 — Словари (`dict`)

## Создание

```python
# Литерал — самый частый способ
user = {"name": "Anton", "age": 30}

# dict() — через именованные аргументы
user = dict(name="Anton", age=30)

# Из списка пар (key, value)
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)  # {"a": 1, "b": 2}

# dict comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**JS-аналогия:** `{}` в JS — то же самое. Но в Python с 3.7+ порядок ключей **гарантированно** сохраняется (в JS — de facto, но не по спеке).

**Подкапотно:** `dict` — хэш-таблица. При вставке ключ хэшируется через `hash(key)`, значение кладётся в слот по индексу `hash % capacity`. Поиск, вставка, удаление — O(1) в среднем. При заполнении ~66% словарь **resize** — удваивается и перехэшируется.

**Ловушки:**
```python
# Ключ должен быть hashable — неизменяемый тип
d[[1, 2]] = "x"  # TypeError: unhashable type: 'list'
d[(1, 2)] = "x"  # OK — tuple hashable
```

---

## Доступ к значениям

```python
user = {"name": "Anton", "age": 30}

# Прямой доступ — KeyError если ключа нет
user["name"]       # "Anton"
user["missing"]    # KeyError!

# .get() — безопасный доступ (аналог user?.name ?? default в JS)
user.get("age")          # 30
user.get("missing")      # None
user.get("missing", 0)   # 0 — дефолтное значение
```

**Ловушка:** В JS `obj.missing` → `undefined`. В Python `d["missing"]` → **KeyError**. Всегда используй `.get()` когда ключ может отсутствовать.

---

## Основные методы

```python
d = {"a": 1, "b": 2, "c": 3}

d.keys()    # dict_keys(["a", "b", "c"])   — view, не список
d.values()  # dict_values([1, 2, 3])
d.items()   # dict_items([("a", 1), ("b", 2), ("c", 3)])

# Итерация — самый частый паттерн
for key, value in d.items():
    print(key, value)

# Проверка наличия ключа — O(1)
"a" in d    # True
"z" in d    # False

# Удаление
del d["a"]           # KeyError если нет
d.pop("b")           # возвращает значение, KeyError если нет
d.pop("z", None)     # безопасно — не бросает KeyError

# setdefault — вернуть значение по ключу; если нет — создать с дефолтом
d.setdefault("x", 0)   # вернёт 0 и добавит {"x": 0} в словарь
d.setdefault("a", 99)  # вернёт существующее значение, словарь не изменит
```

**Подкапотно:** `.keys()`, `.values()`, `.items()` возвращают **view-объекты** — живые срезы словаря, не копии. Если словарь изменится — view отразит это немедленно:

```python
keys = d.keys()
d["new"] = 99
print(keys)  # dict_keys([..., "new"]) — видит новый ключ!
```

**Ловушка — изменение словаря во время итерации:**
```python
for k in d:
    del d[k]  # RuntimeError: dictionary changed size during iteration

# Решение — итерировать по копии
for k in list(d.keys()):
    del d[k]  # OK
```

---

## Merge словарей

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

# Оператор | (Python 3.9+) — создаёт новый словарь
merged = a | b   # {"x": 1, "y": 3, "z": 4}  — b перезаписывает a

# |= — обновляет на месте
a |= b           # a = {"x": 1, "y": 3, "z": 4}

# До 3.9 — spread-синтаксис
merged = {**a, **b}  # аналог {...a, ...b} в JS
```

---

## Типичные паттерны

```python
# Счётчик
words = ["a", "b", "a", "c", "b", "a"]
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
# {"a": 3, "b": 2, "c": 1}

# Группировка через setdefault
users = [
    {"name": "Anna", "role": "admin"},
    {"name": "Bob",  "role": "user"},
    {"name": "Eve",  "role": "admin"},
]
by_role = {}
for u in users:
    by_role.setdefault(u["role"], []).append(u["name"])
# {"admin": ["Anna", "Eve"], "user": ["Bob"]}

# Диспатчинг вместо if/elif
def handle_create(): ...
def handle_delete(): ...

handlers = {
    "create": handle_create,
    "delete": handle_delete,
}
handlers.get(action, lambda: None)()
```

---

## Конспект

### Суть
`dict` — хэш-таблица с гарантированным порядком вставки (Python 3.7+). Ключи должны быть hashable. Доступ, вставка, удаление — O(1) в среднем. Никогда не обращайся по ключу напрямую если не уверен в его наличии — используй `.get()`.

### Python | Что делает | JavaScript
| Python | Что делает | JavaScript |
|--------|-----------|-----------|
| `d["key"]` | доступ, KeyError если нет | `obj.key` (undefined если нет) |
| `d.get("key", default)` | безопасный доступ | `obj.key ?? default` |
| `d.items()` | пары (key, value) — view | `Object.entries(obj)` |
| `d.keys()` | ключи — view | `Object.keys(obj)` |
| `d.values()` | значения — view | `Object.values(obj)` |
| `"k" in d` | проверка ключа O(1) | `"k" in obj` |
| `d.pop("k")` | удалить и вернуть | `delete obj.k` (не возвращает) |
| `d.setdefault("k", v)` | установить если нет | нет прямого аналога |
| `a \| b` | merge (3.9+) | `{...a, ...b}` |
| `a \|= b` | merge на месте | `Object.assign(a, b)` |

### Ловушки

```python
# KeyError при прямом доступе — используй .get()
d["missing"]          # KeyError
d.get("missing", 0)   # 0

# list не может быть ключом
d[[1, 2]] = 1         # TypeError: unhashable type: 'list'
d[(1, 2)] = 1         # OK

# view меняется вместе со словарём
keys = d.keys()
d["new"] = 1
"new" in keys         # True — неожиданно если думать что это список

# Итерация и изменение одновременно
for k in d:
    del d[k]          # RuntimeError
for k in list(d):
    del d[k]          # OK
```

### Когда использовать
- **Счётчик** — `d.get(k, 0) + 1` (или `collections.Counter`)
- **Группировка** — `setdefault(key, []).append(val)` (или `collections.defaultdict`)
- **Конфиги** — merge через `base | override`
- **Кэш** — `{key: result}` для мемоизации
- **Диспатчинг** — `{"action": handler_func}` вместо длинных `if/elif`

# Python Learning Progress

> Этот файл — живой трекер обучения. Обновляется после каждой сессии.
> Перед началом новой сессии Claude читает этот файл, чтобы быть в контексте.

---

## Текущий статус

**Фаза:** 1 — Синтаксис и встроенные типы
**Текущая тема:** 1.3 — `bool` как подкласс `int`
**Следующий шаг:** Phase 1, Topic 1.3 — `bool` как подкласс `int`: `True + True == 2`, `isinstance(True, int)`

---

## Учебный план

### Phase 1: Синтаксис и встроенные типы
- [x] 1.1 — Переменные и типы: `int`, `float`, `bool`, `None`, `complex` — как они устроены, динамическая типизация
- [x] 1.2 — Числа подробно: целочисленная арифметика без переполнения, `//`, `%`, `**`, `Decimal`, `round()`
- [ ] 1.3 — `bool` как подкласс `int` — питоновский сюрприз: `True + True == 2`
- [ ] 1.4 — `None` vs JS `null`/`undefined`: проверка `is None`, `Optional`-паттерн
- [ ] 1.5 — Type hints: базовый синтаксис, `x: int`, `-> str`, зачем нужны
- [ ] 1.6 — Строки: иммутабельность, индексация, срезы `s[1:3]`, `s[::-1]`
- [ ] 1.7 — Строки: методы (`split`, `join`, `strip`, `replace`, `startswith`), `str` vs `bytes`
- [ ] 1.8 — f-strings: форматирование, выражения внутри `{}`, `=` для отладки (`f"{x=}"`)
- [ ] 1.9 — Управляющие конструкции: `if/elif/else`, тернарный оператор, `match/case` (3.10+)
- [ ] 1.10 — Циклы: `for`, `while`, `break`, `continue`, `else` у циклов (редкая фича)
- [ ] 1.11 — Списки: создание, индексация, срезы, `append`, `extend`, `insert`, `pop`, `sort`
- [ ] 1.12 — Кортежи: иммутабельность, именованные кортежи (`namedtuple`, `typing.NamedTuple`)
- [ ] 1.13 — Словари: создание, методы, `dict.get()`, `.items()`, `.keys()`, `.values()`, merge (`|`)
- [ ] 1.14 — Множества: `set`, `frozenset`, операции (`&`, `|`, `-`, `^`), когда использовать
- [ ] 1.15 — `bytes` и `bytearray`: что это, encode/decode, зачем нужны
- [ ] 1.16 — Встроенные функции: `len`, `type`, `isinstance`, `repr`, `id`, `hash`, `dir`
- [ ] 1.17 — Встроенные функции итерации: `enumerate`, `zip`, `range`, `reversed`, `sorted`, `map`, `filter`
- [ ] 1.18 — List/dict/set comprehensions + генераторные выражения
- [ ] 1.19 — Распаковка: `a, b = ...`, `*rest`, swap без temp, распаковка в вызовах
- [ ] 1.20 — Walrus operator `:=`, `match/case` расширенный синтаксис (3.10+)
- [ ] 1.21 — Файловый ввод/вывод: `open()`, режимы, `with`, `pathlib.Path`

### Phase 2: Функции и ООП
- [ ] 2.1 — Функции: `def`, positional, keyword, default-аргументы
- [ ] 2.2 — `*args` и `**kwargs`: сбор и распаковка, порядок параметров
- [ ] 2.3 — Positional-only (`/`) и keyword-only (`*`) параметры — синтаксис Python 3.8+
- [ ] 2.4 — Ловушка mutable default argument + `None`-паттерн как решение
- [ ] 2.5 — Lambda, `map`, `filter`, `sorted` с `key`
- [ ] 2.6 — Области видимости: LEGB, `global`, `nonlocal`, замыкания
- [ ] 2.7 — Функции как объекты первого класса: передача, хранение, возврат
- [ ] 2.8 — Классы: `class`, `__init__`, методы, `self` — отличия от JS-классов
- [ ] 2.9 — Наследование, `super()`, MRO (C3-линеаризация)
- [ ] 2.10 — Множественное наследование и миксины
- [ ] 2.11 — Dunder-методы: `__str__`, `__repr__`, `__eq__`, `__hash__`, `__len__`, `__contains__`
- [ ] 2.12 — Dunder-методы: арифметика (`__add__`, `__mul__`), сравнение (`__lt__`, `__le__`)
- [ ] 2.13 — `@property`, `@classmethod`, `@staticmethod` — когда что использовать
- [ ] 2.14 — Датаклассы (`@dataclass`): поля, `field()`, `frozen`, `__post_init__`
- [ ] 2.15 — `Enum`: перечисления, `IntEnum`, `auto()`, использование в продакшне
- [ ] 2.16 — ABC: абстрактные классы (`ABC`, `abstractmethod`)
- [ ] 2.17 — `Protocol` — структурная типизация (duck typing по-питоновски)
- [ ] 2.18 — `typing` модуль: `Optional`, `Union`, `Any`, `TypeVar`, `Generic`, `Literal`, `TypeAlias`
- [ ] 2.19 — Исключения: `try/except/else/finally`, иерархия, кастомные, `raise from`
- [ ] 2.20 — Модули и пакеты: `import`, `__init__.py`, `__all__`, относительные импорты

### Phase 3: Python изнутри (internals)
- [ ] 3.1 — Как Python хранит объекты: всё — объект, `id()`, `is` vs `==`
- [ ] 3.2 — Управление памятью: reference counting, cyclic GC
- [ ] 3.3 — GIL (Global Interpreter Lock): что это, почему, последствия; экспериментальный no-GIL режим в 3.13
- [ ] 3.4 — Итераторы и протокол итерации (`__iter__`, `__next__`)
- [ ] 3.5 — Генераторы (`yield`, `yield from`, `send()`)
- [ ] 3.6 — Декораторы: функциональные, с аргументами, `functools.wraps`
- [ ] 3.7 — Контекстные менеджеры (`with`, `__enter__/__exit__`, `contextlib`)
- [ ] 3.8 — `functools` модуль: `lru_cache`, `partial`, `reduce`, `cached_property`
- [ ] 3.9 — `itertools` модуль: `chain`, `islice`, `groupby`, `product`, `takewhile`
- [ ] 3.10 — Дескрипторы и `__slots__`
- [ ] 3.11 — Метаклассы и `__new__`

### Phase 4: Асинхронный Python
- [ ] 4.1 — `asyncio`: event loop, coroutines, `async/await`
- [ ] 4.2 — `asyncio.gather`, `asyncio.create_task`, таймауты
- [ ] 4.3 — Асинхронные итераторы и контекстные менеджеры
- [ ] 4.4 — Многопоточность (`threading`) vs многопроцессность (`multiprocessing`)
- [ ] 4.5 — `concurrent.futures`, пулы потоков/процессов
- [ ] 4.6 — Free-threaded Python (no-GIL, 3.13+): как включить, что изменилось, thread safety, race conditions, когда использовать и когда нет; сравнение с классическим GIL и `multiprocessing`

### Phase 5: Экосистема и инструменты
- [ ] 5.1 — Виртуальные окружения: `venv`, `pyenv`, `pyproject.toml`, `uv` — с первого дня
- [ ] 5.2 — Качество кода: `ruff` (linter+formatter), `mypy`/`pyright` (type checking)
- [ ] 5.3 — `mypy` на практике: аннотирование реального кода, `--strict`, игнорирование ошибок
- [ ] 5.4 — Отладка: `pdb`, `breakpoint()`, отладка в VS Code
- [ ] 5.5 — Профилирование: `cProfile`, `line_profiler`, `py-spy` — находить узкие места в коде
- [ ] 5.6 — HTTP клиенты: `requests`, `httpx` (async)
- [ ] 5.7 — `logging` модуль: уровни, handlers, форматирование
- [ ] 5.8 — Тестирование: `pytest`, фикстуры, моки (`unittest.mock`)
- [ ] 5.9 — Скриптинг и автоматизация: `pathlib`, `subprocess`, `os`, `shutil`
- [ ] 5.10 — Web: FastAPI (обзор, пример async REST API)
- [ ] 5.11 — Данные: `pandas`, `numpy` (поверхностно)
- [ ] 5.12 — Популярные области: ML/AI, DevOps/автоматизация, парсинг, бэкенд

### Phase 6: Алгоритмы и структуры данных

> Цель — уверенно проходить алгоритмическую часть собеседований и понимать сложность операций в реальном коде. Все примеры на Python.

**Основы:**
- [ ] 6.1 — Big O нотация: O(1), O(n), O(log n), O(n²) — разбор на питоновских примерах
- [ ] 6.2 — `collections` модуль: `deque`, `Counter`, `defaultdict`, `OrderedDict`
- [ ] 6.3 — `heapq`: min-heap, max-heap, задачи на приоритеты
- [ ] 6.4 — `bisect`: бинарный поиск в отсортированном списке

**Структуры данных:**
- [ ] 6.5 — Массив и связный список: реализация односвязного списка на Python
- [ ] 6.6 — Стек и очередь: через `list` и `deque`, когда что
- [ ] 6.7 — Хэш-таблица: как устроен `dict` изнутри, коллизии, load factor
- [ ] 6.8 — Бинарное дерево: реализация, обходы (in-order, pre-order, post-order)
- [ ] 6.9 — Бинарное дерево поиска (BST): вставка, поиск, удаление
- [ ] 6.10 — Куча (Heap): структура, `heapify`, применение
- [ ] 6.11 — Граф: представление через матрицу смежности и список рёбер

**Алгоритмы сортировки:**
- [ ] 6.12 — Bubble, Selection, Insertion sort: реализация и сложность
- [ ] 6.13 — Merge sort и Quick sort: реализация, рекурсия, сложность
- [ ] 6.14 — Timsort: почему `list.sort()` быстрый и когда это важно

**Алгоритмы поиска и обхода:**
- [ ] 6.15 — Линейный и бинарный поиск
- [ ] 6.16 — BFS (обход в ширину): граф и дерево, очередь
- [ ] 6.17 — DFS (обход в глубину): граф и дерево, стек и рекурсия

**Алгоритмические техники:**
- [ ] 6.18 — Рекурсия и мемоизация: `functools.lru_cache`, ручной кэш
- [ ] 6.19 — Два указателя (Two Pointers): типовые задачи
- [ ] 6.20 — Скользящее окно (Sliding Window): типовые задачи
- [ ] 6.21 — Динамическое программирование (DP): основная идея, top-down vs bottom-up
- [ ] 6.22 — Жадные алгоритмы (Greedy): когда работают, типовые задачи

### Phase 7: Паттерны проектирования (GoF + Python-идиомы)

> Упор на то, как паттерны выглядят именно в Python — многие из них реализуются иначе, чем в Java/JS, благодаря возможностям языка.

**Порождающие (Creational):**
- [ ] 7.1 — Singleton: через модуль, через metaclass, через `__new__`
- [ ] 7.2 — Factory Method и Abstract Factory
- [ ] 7.3 — Builder: пошаговое создание объекта, `dataclass`-вариант
- [ ] 7.4 — Prototype: `copy.copy` vs `copy.deepcopy`

**Структурные (Structural):**
- [ ] 7.5 — Decorator: языковой `@decorator` vs паттерн-обёртка — в чём разница
- [ ] 7.6 — Adapter: обёртка над несовместимым интерфейсом
- [ ] 7.7 — Facade: упрощение сложной подсистемы
- [ ] 7.8 — Proxy: ленивая инициализация, кэширование, контроль доступа
- [ ] 7.9 — Composite: деревья объектов с единым интерфейсом

**Поведенческие (Behavioral):**
- [ ] 7.10 — Strategy: замена `if/else` через объекты или функции первого класса
- [ ] 7.11 — Observer: паттерн событий, сигналы Django как пример
- [ ] 7.12 — Command: инкапсуляция действия, undo/redo
- [ ] 7.13 — Template Method: базовый алгоритм + переопределяемые шаги
- [ ] 7.14 — Chain of Responsibility: цепочка обработчиков (middleware-паттерн)
- [ ] 7.15 — State: конечный автомат через классы или `enum`
- [ ] 7.16 — Iterator: уже знаем протокол — теперь как паттерн проектирования

**Python-специфика:**
- [ ] 7.17 — Какие GoF-паттерны в Python не нужны и почему (first-class functions, duck typing)
- [ ] 7.18 — Питоновские идиомы как паттерны: `context manager`, `descriptor`, `mixin`

### Phase 8: Django + Django REST Framework
- [ ] 8.1 — Django: обзор, MTV vs MVC (аналог Express/Fastify), структура проекта
- [ ] 8.2 — Настройка: `settings.py`, `django-environ`, разделение конфигов
- [ ] 8.3 — Models: ORM, типы полей, `Meta`, `__str__`
- [ ] 8.4 — Migrations: `makemigrations`, `migrate`, схема изменений
- [ ] 8.5 — Django ORM: запросы (`filter`, `exclude`, `annotate`, `aggregate`)
- [ ] 8.6 — ORM: связи (FK, M2M, O2O), `select_related`, `prefetch_related`
- [ ] 8.7 — N+1 запросы: что это, как диагностировать (`django-silk`), как устранять
- [ ] 8.8 — Views и URLs: function-based views, `urlpatterns`, `include`
- [ ] 8.9 — Class-based views (CBV): `View`, `ListView`, `DetailView`, когда что
- [ ] 8.10 — Middleware в Django: принцип, кастомный middleware
- [ ] 8.11 — Django Admin: регистрация моделей, кастомизация
- [ ] 8.12 — DRF: Serializers — валидация, трансформация, вложенность
- [ ] 8.13 — DRF: `APIView`, generic views (`ListCreateAPIView`, etc.)
- [ ] 8.14 — DRF: ViewSets + Routers — автоматический routing
- [ ] 8.15 — DRF: Authentication (`SessionAuth`, `TokenAuth`, `JWT`)
- [ ] 8.16 — DRF: Permissions — встроенные и кастомные
- [ ] 8.17 — DRF: Pagination, filtering (`django-filter`), ordering
- [ ] 8.18 — Django async: async views, ORM async API (`aget`, `afilter`)
- [ ] 8.19 — Тестирование Django: `pytest-django`, `APIClient`, фабрики (`factory_boy`)
- [ ] 8.20 — Celery: асинхронные задачи, очереди, beat-scheduler
- [ ] 8.21 — Redis в Django: кэширование (`django-redis`), сессии, rate limiting
- [ ] 8.22 — Деплой: Docker + `gunicorn`/`uvicorn`, `nginx`, переменные окружения в продакшне

### Phase 9: Архитектура Python-проектов + DDD
- [ ] 9.1 — Обзор: почему в Python нет "одного NestJS" — культура свободы vs конвенции
- [ ] 9.2 — Django-way: "apps" как модули, структура app (models/views/services/urls)
- [ ] 9.3 — Layered architecture: Router → Service → Repository (FastAPI/Django без ORM)
- [ ] 9.4 — Repository pattern в Python: абстракция над ORM/БД
- [ ] 9.5 — Service layer: бизнес-логика отдельно от views/serializers
- [ ] 9.6 — Dependency Injection в Python: ручной DI vs `dependency-injector` библиотека
- [ ] 9.7 — Clean Architecture / Hexagonal: ports & adapters, инверсия зависимостей
- [ ] 9.8 — DDD (обзорно): Entity, Value Object, Aggregate, Domain Event
- [ ] 9.9 — DDD (обзорно): Repository, Domain Service vs Application Service, Bounded Context

### Phase 10: Production & Scale

> Читается после Phase 8. Требует понимания async (Phase 4), Django ORM (8.3–8.7) и деплоя (8.22).

#### 10A: High RPS — 10 000+ запросов в секунду

- [ ] 10.1 — Узкие места Python под нагрузкой: GIL, I/O-bound vs CPU-bound — что масштабируется
- [ ] 10.2 — Async I/O стек для высокого RPS: `uvicorn`, `asyncpg`, `aioredis`
- [ ] 10.3 — Connection pooling: настройка пула БД (`asyncpg`, `psycopg3`, SQLAlchemy pool)
- [ ] 10.4 — Кэширование: Redis, `lru_cache`, `cachetools`, стратегии инвалидации
- [ ] 10.5 — Workers и процессы: `gunicorn` + `uvicorn`, количество воркеров, `--workers` vs `--threads`
- [ ] 10.6 — Индексы БД: составные, частичные, покрывающие — как и когда создавать
- [ ] 10.7 — `EXPLAIN ANALYZE` в PostgreSQL: читать план запроса, находить seq scan
- [ ] 10.8 — Rate limiting, circuit breaker, таймауты — защита сервиса под нагрузкой
- [ ] 10.9 — Нагрузочное тестирование: `locust` — написать сценарий, интерпретировать результаты

#### 10B: Большие данные — 100M+ записей

- [ ] 10.10 — Проблема OFFSET на больших таблицах и cursor-based пагинация как решение
- [ ] 10.11 — Django ORM: `iterator()`, `only()`, `defer()`, `values()`, `values_list()` — экономия памяти
- [ ] 10.12 — Chunked processing: обработка данных частями через генераторы
- [ ] 10.13 — `bulk_create` и `bulk_update`: пакетные операции вместо N INSERT/UPDATE
- [ ] 10.14 — Raw SQL в Django: `connection.execute()`, `RawQuerySet` — когда ORM становится узким местом
- [ ] 10.15 — Streaming HTTP response: отдавать данные частями, `StreamingHttpResponse`
- [ ] 10.16 — pandas с большими данными: `chunksize` в `read_sql`, `read_csv`, обработка по частям
- [ ] 10.17 — Партиционирование таблиц PostgreSQL: range, list, hash — когда и зачем
- [ ] 10.18 — ETL-паттерн на Python: extract → transform → load батчами, прогресс и возобновление

---

## Журнал сессий

| Дата | Тема | Результат |
|------|------|-----------|
| — | — | Старт проекта, план составлен |
| 2026-03-24 | 1.1 — Переменные и типы | Пройдено: int, float, bool, None, type hints, PEP. Решены 3 задачи. |
| 2026-03-26 | 1.2 — Числа подробно | Пройдено: //, %, **, Decimal, round(), banker's rounding. Решены 3 задачи. |

---

## LeetCode

| Дата | # | Название | Сложность | Язык |
|------|---|----------|-----------|------|
| 2026-03-24 | 1 | Две суммы | Easy | Python |
| 2026-03-24 | 9 | Число-палиндром | Easy | Python |

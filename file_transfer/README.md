````md id="o3qvkj"
# File Transfer

Лёгкий HTTP-сервер на Python для загрузки и скачивания файлов.

## Возможности

- Upload файлов через HTTP
- Download файлов по имени
- Локальное хранение файлов
- Простая архитектура без тяжёлых зависимостей
- Подходит для обучения работе с HTTP, потоками байтов и файлами

---

## Структура проекта

```text
file_transfer/
├── .venv/
├── src/
│   ├── main.py
│   ├── server.py
│   ├── routes.py
│   ├── services/
│   └── core/
├── tests/
├── uploads/
├── pyproject.toml
└── README.md
````

---

## Установка

### 1. Создать окружение

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

или если используется `pyproject.toml`

```bash
pip install -e .
```

---

## Запуск

```bash
python src/main.py
```

После запуска сервер доступен:

```text
http://localhost:8000
```

---

## API

## Upload файла

```http
POST /upload
Content-Type: multipart/form-data
```

Пример:

```bash
curl -F "file=@photo.png" http://localhost:8000/upload
```

---

## Скачать файл

```http
GET /download/photo.png
```

Пример:

```bash
curl -O http://localhost:8000/download/photo.png
```

---

## Где хранятся файлы

Все загруженные файлы сохраняются в:

```text
uploads/
```

---

## Разработка

### Запуск тестов

```bash
pytest
```

### Форматирование

```bash
black .
```

### Линтер

```bash
ruff .
```

---

## Планы развития

* Drag & Drop UI
* Progress bar upload
* Chunk upload больших файлов
* Авторизация
* Ограничение размера файла
* Логи запросов
* Docker support

---

## Технологии

* Python 3.12+
* HTTP
* File I/O
* Multipart Form Data

---

## Цель проекта

Изучение:

* как работает HTTP upload/download
* передача байтовых потоков
* работа Python с файлами
* структура backend-приложений

---

```
```

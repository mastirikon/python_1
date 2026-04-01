# Задача 2 (средняя) — Нормализация и форматирование имён
#
# Напиши функцию normalize_name(raw: str) -> str
#
# Правила:
# - Убрать лишние пробелы по краям и между словами (несколько пробелов → один)
# - Каждое слово с заглавной буквы
# - Убрать точки в инициалах: "J. K. Rowling" → "J K Rowling"
# - Если строка пустая или только пробелы — вернуть ""
#
# Примеры:
# normalize_name("  john   doe  ")         -> "John Doe"
# normalize_name("J. K.   Rowling")        -> "J K Rowling"
# normalize_name("IVAN PETROV")            -> "Ivan Petrov"
# normalize_name("   ")                    -> ""
# normalize_name("anna")                   -> "Anna"

def normalize_name(raw: str) -> str:
    raw_title = raw.title()
    raw_dot = raw_title.replace('.', ' ')
    return " ".join(raw_dot.split())
     

normalize_name("  john   doe  ")
normalize_name("J. K.   Rowling")
normalize_name("IVAN PETROV")
normalize_name("   ")
normalize_name("anna")
# Задача 1 (лёгкая) — Анализ строки
#
# Напиши функцию analyze(s: str) -> dict, которая возвращает словарь:
# {
#   "length": длина строки,
#   "first": первый символ (или None если строка пустая),
#   "last": последний символ (или None если строка пустая),
#   "reversed": строка задом наперёд,
#   "middle": средний символ если длина нечётная, иначе два средних символа
# }
#
# Примеры:
# analyze("python") -> {"length": 6, "first": "p", "last": "n", "reversed": "nohtyp", "middle": "th"}
# analyze("hi")     -> {"length": 2, "first": "h", "last": "i", "reversed": "ih", "middle": "hi"}
# analyze("x")      -> {"length": 1, "first": "x", "last": "x", "reversed": "x", "middle": "x"}
# analyze("")       -> {"length": 0, "first": None, "last": None, "reversed": "", "middle": ""}

def analyze(s: str) -> dict:
    return {
        "length": len(s),
        "first": s[0] if s else None,
        "last": s[-1] if s else None,
        "reversed": s[::-1],
        "middle": "" if not s else s[len(s) // 2 - 1] + s[(len(s) // 2)] if len(s) % 2 == 0 else s[(len(s) // 2)]
    }
    
print(analyze("pythonX"))
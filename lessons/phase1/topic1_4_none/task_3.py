# Задача 3 (с подвохом)
# Напиши функцию merge_defaults(data: dict, defaults: dict | None = None) -> dict,
# которая возвращает словарь: сначала значения из defaults, поверх — значения из data.
# Если defaults не передан (None) — использовать {"timeout": 30, "retries": 3} как базовые.
# Подвох: не мутируй входные словари.

def merge_defaults(data: dict, defaults: dict | None = None) -> dict:
    result = {}
    if defaults is None:
        defaults = {
            "timeout": 30, 
            "retries": 3
        }
    result |= defaults | data
    return result
    
    
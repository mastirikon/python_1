# Задача 2 — Средняя: merge конфигов
#
# Есть базовый конфиг и пользовательский.
# Пользовательский должен переопределять значения базового,
# но только для ключей верхнего уровня (глубокий merge не нужен).
#
# Напиши функцию merge_configs(base: dict, override: dict) -> dict,
# которая возвращает новый словарь (не мутирует исходные).
#
# Пример:
#   base     = {"debug": False, "host": "localhost", "port": 8000, "timeout": 30}
#   override = {"debug": True, "port": 9000}
#
#   merge_configs(base, override)
#   → {"debug": True, "host": "localhost", "port": 9000, "timeout": 30}
#
# Проверь: base и override после вызова не изменились.

def merge_configs(base: dict, override: dict) -> dict:
    return {**base, **override}
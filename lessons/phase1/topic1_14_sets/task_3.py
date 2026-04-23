# Задача 3 — С подвохом: дедупликация списка словарей
#
# Дан список пользователей, некоторые дублируются по полю "email".
# Напиши функцию deduplicate(users) -> list,
# которая возвращает список без дублей (по email), сохраняя порядок первого вхождения.
#
# Пример:
#   users = [
#       {"name": "Alice", "email": "alice@example.com"},
#       {"name": "Bob",   "email": "bob@example.com"},
#       {"name": "Alice2","email": "alice@example.com"},  # дубль по email
#       {"name": "Carol", "email": "carol@example.com"},
#   ]
#   deduplicate(users)
#   → [
#       {"name": "Alice", "email": "alice@example.com"},
#       {"name": "Bob",   "email": "bob@example.com"},
#       {"name": "Carol", "email": "carol@example.com"},
#   ]
#
# Подвох: dict нельзя положить в set напрямую — он не hashable.
# Подумай как использовать set для отслеживания уже встреченных email.


users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob",   "email": "bob@example.com"},
    {"name": "Alice2","email": "alice@example.com"},  # дубль по email
    {"name": "Carol", "email": "carol@example.com"},
]
  
  
def deduplicate(users) -> list:
    seen = set()
    result = []
    for user in users:
        if user["email"] not in seen:
            seen.add(user["email"])
            result.append(user)
    return result
    

print(deduplicate(users))
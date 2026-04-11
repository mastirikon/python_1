# Задача 2 — Средняя: Роутер HTTP-ответов
#
# Напиши функцию describe_response(response: dict) -> str,
# которая принимает словарь с ключами "status" и опционально "error"
# и возвращает описание ответа.
#
# Правила (используй match/case):
# - {"status": 200}                       -> "OK"
# - {"status": 201}                       -> "Created"
# - {"status": 400, "error": msg}         -> f"Bad request: {msg}"
# - {"status": 401}                       -> "Unauthorized"
# - {"status": 404}                       -> "Not found"
# - {"status": 500, "error": msg}         -> f"Server error: {msg}"
# - {"status": код} где 500 <= код < 600  -> f"Server error: {код}"
# - всё остальное                         -> "Unknown response"
#
# Примеры:
#   describe_response({"status": 200})                        -> "OK"
#   describe_response({"status": 400, "error": "Bad input"})  -> "Bad request: Bad input"
#   describe_response({"status": 503})                        -> "Server error: 503"
#   describe_response({"status": 418})                        -> "Unknown response"


def describe_response(response: dict) -> str:
    match response:
        case {"status": 200}:
            return "OK"
        case {"status": 201}:
            return "Created"
        case {"status": 400, "error": msg}:
            return f"Bad request: {msg}"
        case {"status": 400}:
            return "Bad request"
        case {"status": 401, "error": msg}:
            return f"Unauthorized: {msg}"
        case {"status": 401}:
            return "Unauthorized"
        case {"status": 404, "error": msg}:
            return f"Not found: {msg}"
        case {"status": 404}:
            return "Not found"
        case {"status": 500, "error": msg}:
            return f"Server error: {msg}"
        case {"status": code} if 500 <= code < 600:
            return f"Server error: {code}"
        case _:
            return "Unknown response"



print(describe_response({"status": 200}))
print(describe_response({"status": 400, "error": "Bad input"}))
print(describe_response({"status": 503}))
print(describe_response({"status": 418})) 
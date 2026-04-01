# Задача 1 (лёгкая) — Парсинг строки подключения к БД
#
# Дана строка подключения к БД в формате:
# "postgresql://user:password@host:port/dbname"
#
# Напиши функцию parse_dsn(dsn: str) -> dict, которая возвращает:
# {
#   "scheme": "postgresql",
#   "user": "user",
#   "password": "password",
#   "host": "host",
#   "port": "5432",
#   "dbname": "dbname"
# }
#
# Используй только split() и find()/index() — без регулярных выражений.
#
# Примеры:
# parse_dsn("postgresql://anton:secret@localhost:5432/mydb")
# -> {"scheme": "postgresql", "user": "anton", "password": "secret",
#     "host": "localhost", "port": "5432", "dbname": "mydb"}


def parse_dsn(dsn: str) -> dict:
    scheme, rest = dsn.split('://') # postgresql, anton:secret@localhost:5432/mydb
    credentials, rest = rest.split("@") # anton:secret, localhost:5432/mydb
    user, password = credentials.split(":") # anton, secret
    host, rest = rest.split(":") # localhost, 5432/mydb
    port, dbname = rest.split("/") # 5432, mydb
    
    
    return {
        "scheme": scheme,
        "user": user,
        "password": password,
        "host": host,
        "port": port,
        "dbname": dbname
    }

print(parse_dsn("postgresql://anton:secret@localhost:5432/mydb"))
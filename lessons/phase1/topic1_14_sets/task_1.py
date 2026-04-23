# Задача 1 — Лёгкая: уникальные теги
#
# Дан список постов, каждый пост — dict с полем "tags" (список строк).
# Напиши функцию all_tags(posts) -> set,
# которая возвращает множество всех уникальных тегов по всем постам.
#
# Пример:
#   posts = [
#       {"title": "A", "tags": ["python", "django"]},
#       {"title": "B", "tags": ["python", "fastapi"]},
#       {"title": "C", "tags": ["django", "sql"]},
#   ]
#   all_tags(posts)
#   → {"python", "django", "fastapi", "sql"}

posts = [
    {"title": "A", "tags": ["python", "django"]},
    {"title": "B", "tags": ["python", "fastapi"]},
    {"title": "C", "tags": ["django", "sql"]},
]


def all_tags(posts) -> set:
    # 1 вариант:
    # result = set()
    # for post in posts:
    #     result.update(post["tags"])
    # return result
    
    # 2 вариант (короче):
    return set().union(*[p["tags"] for p in posts])

print(all_tags(posts))
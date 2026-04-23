# Задача 2 — Средняя: права доступа
#
# Есть роли с наборами прав. Напиши функцию effective_permissions(roles, role_permissions),
# которая принимает список ролей пользователя и словарь прав по ролям,
# и возвращает множество всех прав пользователя (объединение).
#
# Также напиши функцию missing_permissions(user_roles, required, role_permissions),
# которая возвращает множество прав, которых не хватает пользователю.
#
# Пример:
#   role_permissions = {
#       "viewer":    {"read"},
#       "editor":    {"read", "write"},
#       "moderator": {"read", "write", "delete"},
#   }
#
#   effective_permissions(["viewer", "editor"], role_permissions)
#   → {"read", "write"}
#
#   missing_permissions(["viewer"], {"read", "write", "delete"}, role_permissions)
#   → {"write", "delete"}

from typing import Literal, TypedDict

type Role = Literal["viewer", "editor", "moderator"]
type Permission = Literal["read", "write", "delete"]
type RolePermissions = dict[Role, set[Permission]]


role_permissions: RolePermissions = {
    "viewer":    {"read"},
    "editor":    {"read", "write"},
    "moderator": {"read", "write", "delete"},
}


def effective_permissions(roles: list[Role], role_permissions: RolePermissions) -> set[str]:
    # 1 более короткий вариант решения 
    return set().union(*[role_permissions[role]for role in roles])

    # 2 стандартный вариант
    # x = set()
    # for role in roles:
        # x.update(role_permissions[role])
    # return x
    


# print(effective_permissions(["viewer"], role_permissions))
# print(effective_permissions(["viewer", "editor"], role_permissions))
# print(effective_permissions(["viewer", "editor", "moderator"], role_permissions))


def missing_permissions(user_roles: list[Role], required: set[Permission], role_permissions: RolePermissions) -> set[Permission]:
    user_permissions = set().union(*[role_permissions[role] for role in user_roles])
    return required - user_permissions


print(missing_permissions(["viewer"], {"read", "write", "delete"}, role_permissions))
print(missing_permissions(["viewer", "editor"], {"read", "write", "delete"}, role_permissions))
print(missing_permissions(["viewer", "moderator"], {"delete"}, role_permissions))
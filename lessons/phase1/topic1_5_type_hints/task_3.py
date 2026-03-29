# Задача 3 (с подвохом) — Что не так с этим кодом?
#
# Объясни в комментарии: почему mypy будет ругаться на функцию process?
# Исправь двумя разными способами.

from typing import Optional

# Проблема в отсутствии проверки на None
# 1 вариант
def process(value: Optional[int]) -> int | None:
    if value is None:
        return None
    return value * 2

def process2(value: Optional[int]) -> Optional[int]:
    return value * 2 if isinstance(value, int) else None


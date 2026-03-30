# Задача 3 (с подвохом) — Что выведет этот код и почему?
#
# Часть A: объясни в комментарии результат каждого выражения
#
# s = "abcdef"
# print(s[1:10])    # ? "bcdef" - с элемента под индексом 1 и до 9 (вкл), не дает ошибки IndexExcept по тому как срезы не возвращают ошибку по uot of range
# print(s[-2:-5])   # ? Результат "" (пустая строка). Шаг по умолчанию +1 — идёт слева направо. -2 это индекс 4, -5 это индекс 1. Идти от 4 до 1 вперёд — невозможно, результат пустая строка.      
# print(s[4:1:-1])  # ? Результат "edc".  Шаг -1 означает идти справа налево: от индекса 4 ("e") до индекса 2 ("c", индекс 1 не включается). Итог: "edc".
# print(s[::0])     # ? Это ValueError: slice step cannot be zero. Шаг 0 — всегда ошибка.
#
# Часть B: напиши функцию every_nth(s: str, n: int) -> str
# Возвращает каждый n-й символ строки начиная с первого.
# Если n <= 0 — raise ValueError("n must be positive")
#
# Примеры:
# every_nth("abcdef", 2)  -> "ace"
# every_nth("abcdef", 3)  -> "ad"
# every_nth("abcdef", 1)  -> "abcdef"
# every_nth("abcdef", 0)  -> ValueError
def every_nth(s: str, n: int) -> str:
    if n <= 0:
        raise ValueError("s must be positive")
    return s[0::n]
    
#
# Часть C: напиши функцию rotate(s: str, k: int) -> str
# Сдвигает строку на k позиций влево (отрицательный k — вправо).
# Подсказка: реализуй через срезы без циклов.
#
# Примеры:
# rotate("abcdef", 2)   -> "cdefab"
# rotate("abcdef", -2)  -> "efabcd"
# rotate("abcdef", 0)   -> "abcdef"
# rotate("abcdef", 9)   -> "defabc"  (9 % 6 = 3)

def rotate(s: str, k: int) -> str:
    main_rotate = k % len(s)
    rotate_chars = s[:main_rotate]
    static_chars = s[main_rotate:]
    return static_chars + rotate_chars

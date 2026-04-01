# Задача 3 (с подвохом) — Подсчёт слов без split
#
# Часть A: что вернёт этот код? Объясни в комментарии.
#
# print("  hello  world  ".split()) # ["hello", "world"]
# print("  hello  world  ".split(" ")) # ["", "", "hello", "", "", "world", "", ""]
# print("a,,b,,c".split(",")) # ["a", "", "b", "", "c"]
# print("a,,b,,c".split(",,")) # ["a", "b", "c"]
# print("hello".split("x")) # ["hello"]
#
# Часть B: напиши функцию word_count(text: str) -> dict
# Возвращает словарь {слово: количество_вхождений}
# - Регистронезависимо ("Hello" и "hello" — одно слово)
# - Игнорировать знаки препинания: . , ! ? ; :
# - Пустая строка → {}
#
# Примеры:
# word_count("hello world hello")
# -> {"hello": 2, "world": 1}
#
# word_count("Hello, hello! World.")
# -> {"hello": 2, "world": 1}
#
# word_count("")
# -> {}
#
# Подсказка: используй replace() для удаления знаков препинания, затем split()

def word_count(text: str) -> dict:
    cleared_text = text.lower()
    for el in ".,!?;:":
        cleared_text = cleared_text.replace(el, "")
    
    result = {}
    for word in cleared_text.split():
        result[word] = result.get(word, 0) + 1
        
    return result

word_count("Hello, hello! World.")
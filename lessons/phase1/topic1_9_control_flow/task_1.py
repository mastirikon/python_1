# Задача 1 — Лёгкая: FizzBuzz с тернарным оператором
#
# Напиши функцию fizzbuzz(n: int) -> str, которая возвращает:
# - "FizzBuzz" если n делится на 3 и на 5
# - "Fizz"     если n делится на 3
# - "Buzz"     если n делится на 5
# - str(n)     в остальных случаях
#
# Требования:
# - Использовать только тернарный оператор (без if/elif/else блоков)
# - Одно выражение
#
# Примеры:
#   fizzbuzz(15)  -> "FizzBuzz"
#   fizzbuzz(9)   -> "Fizz"
#   fizzbuzz(10)  -> "Buzz"
#   fizzbuzz(7)   -> "7"

def fizzbuzz(n: int) -> str:
    result = ( 
        "FizzBuzz"
            if not n % 3 and not n % 5 
            else "Fizz"
                if not n % 3
                else "Buzz"
                    if not n % 5
                    else str(n)
    )
        
    return result

print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(10))
print(fizzbuzz(7))
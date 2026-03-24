def stats(numbers: list) -> dict:
    pure_numbers = [num for num in numbers if num is not None]
    return {
        "total": sum(pure_numbers),
        "count": len(pure_numbers),
        "positive": sum([num > 0 for num in pure_numbers]),
        "has_none": bool(len(numbers) - len(pure_numbers))
    }


print(stats([12, -2, 423, 64, 3, 5, 23]))
print(stats([12, -2, -423, 64, 3]))
print(stats([12, 2, 423, 64, 3, 5, 23]))
print(stats([12, None, 10, -5]))


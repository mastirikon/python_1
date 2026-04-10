# Задача 1 — Лёгкая: Форматирование таблицы товаров
#
# У тебя есть список товаров. Выведи таблицу в следующем формате:
#
# | №  | Товар              | Цена         | Остаток |
# |----|--------------------|-----------:|--------:|
# |  1 | MacBook Pro        | 199 990,00₽ |       5 |
# |  2 | iPhone 15          |  89 990,00₽ |      12 |
# |  3 | AirPods Pro        |  24 990,00₽ |       0 |
#
# Требования:
# - Номер: ширина 2, правое выравнивание
# - Название: ширина 18, левое выравнивание
# - Цена: ширина 12, 2 знака после запятой, с разделителем тысяч, правое выравнивание
# - Остаток: ширина 7, правое выравнивание

from decimal import Decimal

products = [
    ("MacBook Pro", 199990.0, 5),
    ("iPhone 15", 89990.0, 12),
    ("AirPods Pro", 24990.0, 0),
]

def format_price(price: float) -> str:
    """Форматирование цены по условию: 2 знака после запятой, с разделителем тысяч

    Args:
        price (float): Входной параметр - цена

    Returns:
        str: форматированная в нужный формат строка
    """
    return f"{Decimal(str(price)):_.2f}".replace("_", " ").replace(".", ",") + "₽"


def gen_rows(rows: list[tuple[str, float, int]]) -> str:
    """Генерация строк для таблицы

    Args:
        rows (list[tuple[str, float, int]]): Лист кортежей с информацией для таблицы

    Returns:
        str: Форматированные под таблицу строки
    """
    result: str = ''
    
    for ind, value in enumerate(rows):
        row_num = str(ind + 1)
        name: str = value[0]
        price: str = format_price(value[1])
        remains: str = str(value[2])
        
        result += row_format([row_num, name, price, remains])
        
    return result


def row_format(rows: list[str], ph: str = " ") -> str:
    """Форматирование отдельной строки

    Args:
        rows (list[str]): Значения каждой колонки текущей строки
        ph (str, optional): Заполнитель пробелов. Defaults to " ".

    Returns:
        str: Отформатированная под таблицу строка
    """
    return  "| " + rows[0].rjust(2, ph) + " | " + rows[1].ljust(18, ph) + " |" + rows[2].rjust(12, ph) + " | " + rows[3].rjust(7, ph) + " | \n"


def gen_table(rows: list[tuple]) -> str:
    """Генерация таблицы с заголовком, разделителем и строками

    Args:
        rows (list[tuple]): Лист кортежей с информацией для таблицы

    Returns:
        str: Строковое представление готовой таблицы
    """
    header = row_format(["№", "Товар", "Цена", "Остаток"])
    underline = row_format(["", "", ":", ":"], '-')
    return header + underline + gen_rows(rows)

print(gen_table(products))

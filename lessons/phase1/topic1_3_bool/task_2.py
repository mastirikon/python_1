def first_true(values: list) -> int:
    """Возвращает индекс первого truthy значения списка

    Args:
        values (list): Список для перебора

    Returns:
        int: Индекс первого truthy значения списка или -1
    """
    for i, val in enumerate(values):
        if val: return i
    return -1
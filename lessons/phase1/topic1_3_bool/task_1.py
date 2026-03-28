def count_passing(scores: list[int], threshold: int) -> int:
    """Считает кол-во оценок, строго выше порога

    Args:           
        scores (list[int]): Список числовых оценок  
        threshold (int): Пороговое значение, не включительно

    Returns:
        int: Количество оценок, превышающее threshold
    """
    return sum(score > threshold for score in scores)

result = count_passing([15, 4, 7, 22, 0, 1, -5, -100, 125], -3)
print(result)
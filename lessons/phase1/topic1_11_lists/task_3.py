# Задача 3 — С подвохом: Матрица rotate
#
# Напиши функцию rotate_matrix(matrix: list[list[int]]) -> list[list[int]]
# которая поворачивает квадратную матрицу на 90° по часовой стрелке.
# Возвращает новую матрицу, оригинал не изменять.
#
# Пример:
#   matrix = [
#       [1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9],
#   ]
#   rotate_matrix(matrix)
#   →  [[7, 4, 1],
#        [8, 5, 2],
#        [9, 6, 3]]
#
# Подвох: в решении нужно создать новую матрицу через [[0]*n for _ in range(n)].
# Попробуй сначала через [[0]*n]*n — посмотри что сломается и почему.
#
# Подсказка: элемент result[j][n-1-i] = matrix[i][j]

def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_list = []
    for line in zip(*matrix):
        new_list.append(list(line)[::-1])
    return new_list


matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
  ]
print(rotate_matrix(matrix))
#   →  [[7, 4, 1],
#        [8, 5, 2],
#        [9, 6, 3]]
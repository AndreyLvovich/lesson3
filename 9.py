# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE = 5
MIN_ITEM = -100
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
print(*matrix, sep='\n')

max = matrix[0][0]

for i in range(len(matrix[0])):
    min = matrix[0][i]
    for j in range(len(matrix)):
        if matrix[j][i] < min:
            min = matrix[j][i]
    print('Минимальный - ',min,' - в столбце - ', i)
    if max < min:
        max = min

print('Максимальный элемент среди минимальных - ',max)



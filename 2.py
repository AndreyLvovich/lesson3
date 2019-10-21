# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

SIZE = 20
MIN_ITEM = 1
MAX_ITEM = 100
matrix = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(matrix)

matrix_2 = []

for i in range(len(matrix)):
    if matrix[i] % 2 == 0:
        matrix_2.append(i)

print(matrix_2)
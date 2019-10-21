# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

# import random

# SIZE = 4
# MIN_ITEM = 0
# MAX_ITEM = 100
#matrix = [[random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE+1)] for _ in range(SIZE)]
matrix = []

print('Введите числа в массив ')

for i in range(5):
    line = []
    summ = 0
    for j in range(4):
        temp = int(input(''))
        summ = summ + temp
        line.append(temp)
    line.append(summ)
    matrix.append(line)

print(*matrix, sep='\n')

print('*' * 50)

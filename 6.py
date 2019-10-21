# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max = array[0]
min = array[0]
pos = 0
max_pos = 0
min_pos = 0

for i in array:
    if i > max:
        max = i
        max_pos = pos
    elif i < min:
        min = i
        min_pos = pos
    pos += 1

# print(max,' ',max_pos)
# print(min,' ',min_pos)
# if max_min > max_pos:
#     max_pos, max_min = max_min, max_pos

summ = 0
for i in range(min_pos + 1, max_pos - 1):
    summ = summ + array[i]

print('Cумма элементов находящихся между минимальным и максимальным элементами = ',summ)
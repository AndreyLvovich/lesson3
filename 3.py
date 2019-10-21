# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max = array[0]
min = array[0]

max_pos = 0
min_pos = 0

j = 0
for i in array:
    if i > max:
        max = i
        max_pos = j
    elif i < min:
        min = i
        min_pos = j
    j += 1

print(max,' ',min)
print(max_pos,' ',min_pos)

array[max_pos] = min
array[min_pos] = max
print(array)


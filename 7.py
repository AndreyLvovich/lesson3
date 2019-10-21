# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min1 = 0
min2 = 1


for i in range(len(array)):
    if array[i] < array[min1]:
        temp = min1
        min1 = i
        if array[temp] < array[min2]:
            min2 = temp
    elif array[i] < array[min2]:
        min2 = i

print('Певрое минимальное ',array[min1])
print('Второе минимальное ',array[min2])



# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count = 1
value = array[0]
a = 0
for i in array:
    temp_count = 0
    a += 1
    # print(i)
    # print(array[a::])
    for j in array[a::]:
        if i == j:
            temp_count += 1
    if temp_count > count:
        count = temp_count
        value = array[i]


print(f'Число {value} встречает {count} раз')

# print(array[1::])



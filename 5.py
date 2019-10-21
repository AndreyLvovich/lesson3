# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

def negative(max_negative):
    max_pos = 0
    a = 0
    for i in array:
        if i < 0 and abs(i) < abs(max_negative):
            max_negative = i
            max_pos = a
        a = a + 1
    print('Максимальный отрицательнй элемент - ',max_negative)
    print('Позиция этого жлемента в массиве - ',max_pos)

# Находим первое отрицательное число и проверяем есть ли вообще такие
max = 0
for i in array:
    if i < 0:
        max = i
        negative(max)
        break
else:
    print('Отрицательных значений нет')

# max_pos = 0
# a = 0
# for i in array:
#     #print('i - ',i,' ','a - ', a,' ','max_pos - ', max_pos)
#     if i < 0 and abs(i) < abs(max):
#         max = i
#         max_pos = a
#     a = a + 1

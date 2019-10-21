# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


NUMBER_1 = 2
NUMBER_2 = 99

RANGE_1 = 2
RANGE_2 = 9

for i in range(NUMBER_1, NUMBER_2+1):
    count = 0
    print(i,' ', end='')
    for j in range(RANGE_1, RANGE_2 + 1):
        if i % j == 0:
            count += 1
    print(f'Числу {i} кратно {count} чисел')

# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Входные данные
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.
# 15 --> 3
# 35 --> 5

n = int(input("Введите число: "))
if n > 1 and n < 106:
    for i in range(2, n):
        if n % i == 0:
            print(i)
            break
else:
    print("Ошибка! Вы ввели неправильное число!")

# Входные данные
# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – число монеток.
# В каждой из последующих N строк содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint

n = int(input("Введите число:"))
n = [randint(0, 1) for i in range(n)]
print(n)
count=0
for i in n:
    if n[i] == 0:
        count += 1
        i += 1
    else:
        i += 1
print(count)

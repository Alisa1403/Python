# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

X1 = int(input("Введите X1:"))
Y1 = int(input("Введите Y1:"))
X2 = int(input("Введите X2:"))
Y2 = int(input("Введите Y2:"))

result = math.sqrt(math.pow(X1-X2, 2)+math.pow(Y1-Y2, 2))
print(result)

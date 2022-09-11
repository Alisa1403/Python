# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math 

start = [1.1, 1.2, 3.1, 5, 10.01]
new = [] 
for i in range(len(start)): 
    frac_num, integral_num = math.modf(start[i]) 
    if frac_num != 0: 
        new.append(round(frac_num, 3)) 
print(max(new) - min(new))
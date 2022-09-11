# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

inital = [2, 3, 4, 5, 6]
new = []
temp = 0
size = int(len(inital))
if size % 2 == 0:
    for i in range(size//2):
        temp = inital[i]*inital[-1-i]
        new.append(temp)
    print(new)
else:
    for i in range(size//2+1):
        temp = inital[i]*inital[-1-i]
        new.append(temp)
    print(new)

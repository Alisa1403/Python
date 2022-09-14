# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


list = [1, 5, 6, 2, 1, 2, 5, 5]
unique = []

for list in list:
    if list in unique:
        continue
    else:
         unique.append(list)
print(unique)


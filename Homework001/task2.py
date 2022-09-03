# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not x) or (not y) or (not z)) == (not x) and (not y) and (not z) == 1:
                print(x, y, z, 1)
            else:
                print(x, y, z, 0)

# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

n = int(input())
k = 0
pi = (1/16**k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))

for k in range(1,n):
    pi += (1/16**k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))

print(round(pi,n))
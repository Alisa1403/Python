# Таблица умножения/сложения/возведения в степень

def table(op, rows=9, col=9):
    for i in range(1, rows+1):
        for k in range(1, col+1):
            print(op(i, k), end='\t')
        print('')


table(lambda x, y: x+y)

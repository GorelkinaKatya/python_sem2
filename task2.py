S = int (input('Введите сумму чисел: '))
P = int (input('Введите произведение чисел: '))

print('Возможные пары чисел:')
for i in range(0,1000):
    for j in range(0,1000):
        if i + j == S and i * j == P:
            print(f'X = {i} Y = {j}')
coins_number = int (input('Введите количество монет: '))

count_0 = 0
count_1 = 0

print('Сгенерированные монеты:')
from random import randint
for _ in range(coins_number):
    coin = randint(0,1)
    print(coin, end=' ')
    if coin == 0:
        count_0 += 1
    else:
        count_1 += 1

print()
if count_0 > count_1:
    print(f'Минимальное количество монет, которые нужно перевернуть: {count_1}')
else:
    print(f'Минимальное количество монет, которые нужно перевернуть: {count_0}')
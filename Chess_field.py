# Определение цвета клетки поля
print('Введите координаты клетки')
koor = input()
koor = list(koor)
# Проверка на имя поля
if koor[0] == 'a':
    index = 1
elif koor[0] == 'b':
    index = 2
elif koor[0] == 'c':
    index = 3
elif koor[0] == 'd':
    index = 4
elif koor[0] == 'e':
    index = 5
elif koor[0] == 'f':
    index = 6
elif koor[0] == 'g':
    index = 7
else:
    index = 8

# Вычисляем координату и проверяем

koor_chess = index * int(koor[1])
if (koor_chess % 2) == 1:
    print('Черное')
else:
    print('Белое')

# -*- coding: cp1251 -*-
try:
    R = float(input('Введите R='))
    x = float(input('Введите X='))
    y = float(input('Введите Y='))
except ValueError:
    print('Некорректный ввод: нужно ввести вещественные числа')
    exit()

flag = (x >= 0 and y >= 0 and x <= 2*R and y <= 2*R and x**2 + y**2 >= R**2) or \
       (x <= 0 and y <= 0 and x + y >= -2*R)

print("X={0:.2f} Y={1:.2f} R={2:.2f}: ".format(x, y, R), end="")
if flag:
    print('Попадает')
else:
    print('Не попадает')
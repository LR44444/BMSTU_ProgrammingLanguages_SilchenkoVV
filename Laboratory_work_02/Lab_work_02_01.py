from math import sqrt

try:
    x = float(input('Введите значение x='))
except ValueError:
    print('Некорректный ввод: нужно ввести вещественное число')
    exit()

if x < -1:
    y = -x - 1
elif x < 1:
    y = 0
elif x < 5:
    y = sqrt(4 - (x - 3)**2)
else:
    y = -(x - 5) / 2

print("X={0:.2f} Y={1:.2f}".format(x, y))
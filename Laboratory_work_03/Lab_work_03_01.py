from math import sqrt

print('Введите Xbeg, Xend и Dx')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))

if dx <= 0:
    print('Некорректные данные: шаг Dx должен быть больше 0')
    exit()

print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print("  Dx={0: 7.2f}".format(dx))

xt = xb
print("+--------+--------+")
print("I   X    I   Y    I")
print("+--------+--------+")
while xt <= xe:
    if xt < -1:
        y = -xt - 1
    elif xt < 1:
        y = 0
    elif xt < 5:
        y = sqrt(4 - (xt - 3)**2)
    else:
        y = -(xt - 5) / 2
    print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    xt += dx
print("+--------+--------+")

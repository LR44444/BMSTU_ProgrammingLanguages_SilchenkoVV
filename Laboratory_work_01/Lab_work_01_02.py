from math import sqrt

try:
    a1, a2 = map(float, input("Введите a1 и a2 через пробел: ").split())

    d = a1**2 - a2**2

    if d <= 0:
        print("Некорректные данные: a1^2 - a2^2 должно быть больше 0")
    else:
        z1 = (a1**2 + a2**2 + a1 * a2) / sqrt(d) * (a1 - a2)**2
        z2 = d / 4

        print("z1 = {:.4f}".format(z1))
        print("z2 = {:.4f}".format(z2))

except ValueError:
    print("Некорректный ввод: введите два вещественных числа через пробел")
print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))

if not (-1 < xb < 1 and -1 < xe < 1) or dx <= 0:
    print('Некорректные данные: интервал должен лежать в (-1, 1), Dx > 0')
    exit()

print("Xnach={0: 5.2f}  Xkon={1: 5.2f}  Dx={2: 4.2f}  Eps={3:.6f}".format(xb, xe, dx, eps))
print("+--------+--------+-----+")
print("I   X    I   Y    I  N I")
print("+--------+--------+-----+")
xt = xb
while xt <= xe:
    an = xt          # первый член ряда a0 = x
    n = 0
    y = an
    while True:
        k = (xt**2) * (2*n + 1)**2 / ((2*n + 2) * (2*n + 3))
        an = an * k
        y = y + an
        n = n + 1
        if abs(an) < eps:
            break
    print("I{0: 7.2f} I{1: 7.3f} I{2: 4} I".format(xt, y, n))
    xt = xt + dx
print("+--------+--------+-----+")
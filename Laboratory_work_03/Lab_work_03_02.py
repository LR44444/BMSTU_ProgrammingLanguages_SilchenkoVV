from random import uniform

try:
    R = float(input('Введите R='))
except ValueError:
    print('Некорректный ввод: R должно быть числом')
    exit()

print("      X       Y    Res")
print("-------------------------")
for n in range(10):
    x = uniform(-2*R, 2*R)
    y = uniform(-2*R, 2*R)

    if (x >= 0 and y >= 0 and x <= 2*R and y <= 2*R and x**2 + y**2 >= R**2) or \
            (x <= 0 and y <= 0 and x + y >= -2*R):
        flag = 1
    else:
        flag = 0

    print("{0: 7.2f}{1: 7.2f}  ".format(x, y), end="")
    if flag:
        print("Yes")
    else:
        print("No")
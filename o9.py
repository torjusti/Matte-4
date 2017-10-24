import math


def approximate_polynomial():
    def polynomial(x): return x ** 3 - x ** 2 + x + 2

    def derivative(x): return 3 * x ** 2 - 2 * x + 1

    x = -1

    for i in range(3):
        x -= polynomial(x) / derivative(x)

    return x


print(approximate_polynomial())


def trig(x):
    return x - math.cos(x)


def secant():
    a, b, i = 0, 1, 0
    while abs(a - b) >= 5e-5:
        i += 1
        a, b = a - trig(a) * (a - b) / (trig(a) - trig(b)), a
    return a, i


print(secant())


def nm2d():
    def f(x, y): return x ** 2 + y ** 2 - 4

    def g(x, y): return x * y - 1

    x, y = 2, 0

    for i in range(3):
        determinant = 1 / (2 * x ** 2 - 2 * y ** 2)
        x = x - determinant * (f(x, y) * x - 2 * y * g(x, y))
        y = y - determinant * (g(x, y) * 2 * x - f(x, y) * y)
    
    return x, y


nm2d()

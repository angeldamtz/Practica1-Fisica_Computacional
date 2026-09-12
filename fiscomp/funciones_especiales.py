from .precision_numerica import EPS


def factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


def seno(x):
    suma = 0.0
    n = 0

    while True:
        termino = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

        if abs(termino) < EPS:
            break

        suma += termino
        n += 1

    return suma


def coseno(x):
    suma = 0.0
    n = 0

    while True:
        termino = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)

        if abs(termino) < EPS:
            break

        suma += termino
        n += 1

    return suma


def exponencial(x):
    suma = 0.0
    n = 0

    while True:
        termino = (x ** n) / factorial(n)

        if abs(termino) < EPS:
            break

        suma += termino
        n += 1

    return suma


def ln(x):

    if x <= 0:
        raise ValueError("ln(x) solo está definido para x > 0")

    if x == 1:
        return 0.0

    y = (x - 1) / (x + 1)

    suma = 0.0
    n = 0

    while True:
        termino = 2 * (y ** (2 * n + 1)) / (2 * n + 1)

        if abs(termino) < EPS:
            break

        suma += termino
        n += 1

    return suma
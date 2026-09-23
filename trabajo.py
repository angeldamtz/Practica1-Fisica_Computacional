#! /usr/bin/python3

from fiscomp.funciones_especiales import seno, coseno

from fiscomp.precision_numerica import EPS


# ============================================================
# DERIVADAS NUMÉRICAS
# ============================================================

def diff_forward(f, x0, h):
    return (f(x0 + h) - f(x0)) / h


def diff_backward(f, x0, h):
    return (f(x0) - f(x0 - h)) / h


def diff_central(f, x0, h):
    return (f(x0 + h/2) - f(x0 - h/2)) / h


# ============================================================
# FUNCIONES
# ============================================================

def const_5(x):
    return 5


def ident(x):
    return x


def sqr(x):
    return x**2


def sin_x2(x):
    return seno(x**2)


# ============================================================
# DERIVADAS EXACTAS
# ============================================================

def d_const_5(x):
    return 0


def d_ident(x):
    return 1


def d_sqr(x):
    return 2*x


def d_sin_x2(x):
    return 2*x*coseno(x**2)


# ============================================================
# ERROR RELATIVO
# ============================================================

def error_relativo(aproximado, exacto):

    if exacto == 0:

        if aproximado == 0:
            return 0.0
        else:
            return float("inf")

    return abs(aproximado - exacto) / abs(exacto)


# ============================================================
# LISTA DE FUNCIONES
# ============================================================

funciones = [
    ("f(x)=5", const_5, d_const_5),
    ("f(x)=x", ident, d_ident),
    ("f(x)=x^2", sqr, d_sqr),
    ("f(x)=sin(x^2)", sin_x2, d_sin_x2)
]


# ============================================================
# COMPARACIÓN DE DERIVADAS
# ============================================================

x0 = 6.0
h = 0.1

print()
print("===== COMPARACION DE DERIVADAS =====")

for nombre, funcion, derivada in funciones:

    exacta = derivada(x0)

    forward = diff_forward(funcion, x0, h)
    backward = diff_backward(funcion, x0, h)
    central = diff_central(funcion, x0, h)

    error_forward = error_relativo(forward, exacta)
    error_backward = error_relativo(backward, exacta)
    error_central = error_relativo(central, exacta)

    print()
    print(nombre)

    print("Derivada exacta:", exacta)

    print("Forward:", forward)
    print("Backward:", backward)
    print("Central:", central)

    print("Error relativo Forward:", error_forward)
    print("Error relativo Backward:", error_backward)
    print("Error relativo Central:", error_central)


# ============================================================
# ESTUDIO DE LA DERIVADA DE sin(x^2)
# ============================================================

# ============================================================
# EJERCICIO 3 - BARRIDO DE h
# ============================================================

from pathlib import Path

x0 = 1.0
h = 1.0

carpeta_datos = Path(__file__).resolve().parent / "datos"
carpeta_datos.mkdir(exist_ok=True)

nombre_archivo = carpeta_datos / "derivada_sin_x2.dat"

exacta = d_sin_x2(x0)

archivo = open(nombre_archivo, "w")

archivo.write("# h diff_forward error_forward diff_central error_central\n")

for i in range(50):

    h = h / 2

    forward = diff_forward(sin_x2, x0, h)
    central = diff_central(sin_x2, x0, h)

    error_forward = error_relativo(forward, exacta)
    error_central = error_relativo(central, exacta)

    archivo.write(
        f"{h} {forward} {error_forward} {central} {error_central}\n"
    )

archivo.close()

print()
print("===== EJERCICIO 3 =====")
print("Archivo generado:")
print(nombre_archivo)

# ============================================================
# EJERCICIO 4 - h OPTIMO
# ============================================================

# Buscar el h que produjo el menor error
mejor_forward = None
mejor_central = None

h = 1.0

for i in range(50):

    h = h / 2

    forward = diff_forward(sin_x2, x0, h)
    central = diff_central(sin_x2, x0, h)

    error_forward = error_relativo(forward, exacta)
    error_central = error_relativo(central, exacta)

    if mejor_forward is None or error_forward < mejor_forward[1]:
        mejor_forward = (h, error_forward)

    if mejor_central is None or error_central < mejor_central[1]:
        mejor_central = (h, error_central)


# Valores teóricos
h_opt_forward = (4 * EPS) ** 0.5
h_opt_central = (24 * EPS) ** (1/3)


print()
print("===== EJERCICIO 4 =====")

print()
print("Forward:")
print("h óptimo medido:", mejor_forward[0])
print("error mínimo:", mejor_forward[1])
print("h óptimo teórico:", h_opt_forward)

print()
print("Central:")
print("h óptimo medido:", mejor_central[0])
print("error mínimo:", mejor_central[1])
print("h óptimo teórico:", h_opt_central)
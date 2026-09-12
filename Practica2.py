import math
from fiscomp.precision_numerica import error_relativo


def aproximar_pi(N):
    suma = 0.0

    for k in range(N):
        termino = ((-1) ** k) / (2 * k + 1)
        suma += termino

    return 4 * suma


# ==================================
# EJERCICIO 2 - PI DE LEIBNIZ
# ==================================

N = int(input("Número de términos: "))

pi_aproximado = aproximar_pi(N)

pi_real = math.pi

error = error_relativo(pi_aproximado, pi_real)


# ==================================
# MOSTRAR RESULTADOS
# ==================================

print()
print("===== APROXIMACIÓN DE PI =====")

print(f"Número de términos: {N}")
print(f"Pi aproximado: {pi_aproximado:.15f}")
print(f"Pi de math: {pi_real:.15f}")
print(f"Error relativo: {error:.6e}")
print(f"Error relativo (%): {error * 100:.6e} %")


# ==================================
# GUARDAR PI EN CONSTANTES.PY
# ==================================

with open("fiscomp/constantes.py", "w") as archivo:

    archivo.write("# Constantes calculadas en la Práctica 1\n")
    archivo.write("# Aproximación de pi mediante la serie de Leibniz\n")
    archivo.write("#\n")
    archivo.write("# La serie de Leibniz converge lentamente. El error\n")
    archivo.write("# disminuye aproximadamente como 1/N, por lo que\n")
    archivo.write("# alcanzar el epsilon de la máquina requeriría una\n")
    archivo.write("# cantidad de términos poco práctica.\n")
    archivo.write("#\n")

    archivo.write(f"PI = {pi_aproximado:.15f}\n")
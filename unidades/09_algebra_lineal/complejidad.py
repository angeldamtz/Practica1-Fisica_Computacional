
"""
Ejercicio 3: complejidad, conteo de operaciones y tiempos.

Conteos teóricos:
- Producto punto de n componentes: n productos y n-1 sumas,
  por lo que cuesta 2*n - 1 flops, es O(n).
- Producto matriz-vector: n productos punto,
  por lo que cuesta n*(2*n - 1) = 2*n**2 - n, es O(n**2).
- Producto matriz-matriz: n**2 productos punto,
  por lo que cuesta n**2*(2*n - 1) = 2*n**3 - n**2, es O(n**3).
- Sustitución triangular: n**2 flops, es O(n**2).
"""
import sys
from pathlib import Path
from time import perf_counter
import random

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from fiscomp.matrices import Matrix, LowerTriangularMatrix
from fiscomp.algebra_lineal import (
    SistemaTriangular,
    producto_punto,
    mat_vec,
)


# Carpeta donde guardaremos los resultados.
CARPETA_DATOS = Path(__file__).resolve().parent / "datos"
CARPETA_DATOS.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 3b. Funciones que cuentan operaciones
# --------------------------------------------------

def producto_punto_contando(x, y):
    """Regresa (producto punto, número de flops)."""
    if len(x) != len(y):
        raise ValueError("Los vectores deben tener la misma longitud.")

    resultado = 0
    for a, b in zip(x, y):
        resultado += a * b

    flops = 2 * len(x) - 1
    return resultado, flops


def mat_vec_contando(A, x):
    """Regresa (producto matriz-vector, número de flops)."""
    if not A or len(A[0]) != len(x):
        raise ValueError("Dimensiones incompatibles.")

    resultado = []
    flops = 0

    for fila in A:
        valor, operaciones = producto_punto_contando(fila, x)
        resultado.append(valor)
        flops += operaciones

    return resultado, flops


def mat_mat_contando(A, B):
    """Regresa (producto matriz-matriz, número de flops)."""
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("Dimensiones incompatibles.")

    columnas_B = [
        [B[i][j] for i in range(len(B))]
        for j in range(len(B[0]))
    ]

    resultado = []
    flops = 0

    for fila in A:
        fila_resultado = []
        for columna in columnas_B:
            valor, operaciones = producto_punto_contando(
                fila, columna
            )
            fila_resultado.append(valor)
            flops += operaciones
        resultado.append(fila_resultado)

    return resultado, flops


# --------------------------------------------------
# 3b. Comparar conteos con las fórmulas teóricas
# --------------------------------------------------

def contar_flops():
    archivo = CARPETA_DATOS / "conteo_flops.dat"
    tamanos = [1, 2, 4, 8, 16, 32, 64]

    with archivo.open("w", encoding="utf-8") as f:
        f.write("# n producto_punto mat_vec mat_mat sustitucion\n")

        for n in tamanos:
            x = [1.0] * n
            A = [[1.0] * n for _ in range(n)]
            B = [[1.0] * n for _ in range(n)]

            _, pp = producto_punto_contando(x, x)
            _, mv = mat_vec_contando(A, x)
            _, mm = mat_mat_contando(A, B)

            L = LowerTriangularMatrix([
                [1.0 if i == j else 0.0 for j in range(n)]
                for i in range(n)
            ])
            sistema = SistemaTriangular(L, x)
            sistema.resolver()
            sustitucion = n**2

            # Comprobación exacta de las fórmulas.
            assert pp == 2 * n - 1
            assert mv == 2 * n**2 - n
            assert mm == 2 * n**3 - n**2
            assert sustitucion == n**2

            f.write(
                f"{n} {pp} {mv} {mm} {sustitucion}\n"
            )

            print(
                f"n={n:2d} | producto punto={pp:7d} "
                f"| mat_vec={mv:9d} | mat_mat={mm:10d} "
                f"| sustitución={sustitucion:7d}"
            )

    print(f"\nConteos guardados en: {archivo}")


# --------------------------------------------------
# 3c. Medir tiempos y estimar exponentes
# --------------------------------------------------

def medir_tiempo(funcion, repeticiones=3):
    """Regresa el menor tiempo medido, en segundos."""
    tiempos = []

    for _ in range(repeticiones):
        inicio = perf_counter()
        funcion()
        fin = perf_counter()
        tiempos.append(fin - inicio)

    return min(tiempos)


def medir_tiempos():
    archivo = CARPETA_DATOS / "tiempos.dat"
    tamanos = [25, 50, 100, 200]
    resultados = []

    with archivo.open("w", encoding="utf-8") as f:
        f.write("# n t_sustitucion t_mat_mat\n")

        for n in tamanos:
            # Matriz triangular inferior con diagonal no nula.
            L_datos = [
                [
                    (random.random() if j < i else (2.0 if i == j else 0.0))
                    for j in range(n)
                ]
                for i in range(n)
            ]
            L = LowerTriangularMatrix(L_datos)
            b = [1.0] * n
            sistema = SistemaTriangular(L, b)

            # Matrix usa el operador * para multiplicación matricial.
            A = Matrix([
                [random.random() for _ in range(n)]
                for _ in range(n)
            ])
            B = Matrix([
                [random.random() for _ in range(n)]
                for _ in range(n)
            ])

            t_sust = medir_tiempo(sistema.resolver)
            t_mat = medir_tiempo(lambda: A * B)

            resultados.append((n, t_sust, t_mat))
            f.write(f"{n} {t_sust:.10e} {t_mat:.10e}\n")

            print(
                f"n={n:3d} | sustitución={t_sust:.6e} s "
                f"| matriz-matriz={t_mat:.6e} s"
            )

    print(f"\nTiempos guardados en: {archivo}")

    print("\nExponentes estimados p:")
    for i in range(1, len(resultados)):
        n1, sust1, mat1 = resultados[i - 1]
        n2, sust2, mat2 = resultados[i]

        p_sust = (
            __import__("math").log(sust2 / sust1, 2)
            / __import__("math").log(n2 / n1, 2)
        )
        p_mat = (
            __import__("math").log(mat2 / mat1, 2)
            / __import__("math").log(n2 / n1, 2)
        )

        print(
            f"{n1} -> {n2}: "
            f"p_sustitución={p_sust:.2f}, "
            f"p_matriz-matriz={p_mat:.2f}"
        )


# --------------------------------------------------
# 3d. Respuestas a las preguntas de la práctica
# --------------------------------------------------

# 1. Los exponentes deberían acercarse a 2 para la sustitución
# y a 3 para el producto matriz-matriz cuando n es grande.
# Para n pequeño, el tiempo también depende de crear listas,
# llamar funciones, recorrer ciclos y otros costos de Python.
#
# 2. Ambas operaciones son O(n**2), pero la sustitución cuesta
# n**2 flops y el producto matriz-vector cuesta 2*n**2 - n.
# Para n grande, el producto matriz-vector requiere aproximadamente
# el doble de operaciones que la sustitución.
#
# 3. Al pasar de n=1000 a n=10000, la sustitución tardaría
# aproximadamente 100 veces más, por ser O(n**2).
# El producto matriz-matriz tardaría aproximadamente 1000 veces
# más, por ser O(n**3). La complejidad importa porque el crecimiento
# del costo cambia drásticamente para tamaños grandes.


if __name__ == "__main__":
    print("=== Ejercicio 3: conteo de operaciones ===")
    contar_flops()

    print("\n=== Ejercicio 3: medición de tiempos ===")
    medir_tiempos()

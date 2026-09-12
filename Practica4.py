import math

from fiscomp.funciones_especiales import (
    seno,
    coseno,
    exponencial,
    ln
)

from fiscomp.precision_numerica import error_relativo


# ==========================================
# VALORES PARA CADA FUNCIÓN
# ==========================================

valores_trigonometricos = [
    0.0,
    0.1,
    0.5,
    1.0,
    1.5,
    2.0
]

valores_exponencial = [
    -2.0,
    -1.0,
    0.0,
    0.5,
    1.0,
    2.0
]

valores_ln = [
    0.1,
    0.5,
    0.9,
    1.0,
    1.1,
    2.0
]


# ==========================================
# LISTA PARA GUARDAR LOS RESULTADOS
# ==========================================

resultados = []


# ==========================================
# SENO
# ==========================================

for x in valores_trigonometricos:

    aproximado = seno(x)
    real = math.sin(x)

    error = error_relativo(aproximado, real)

    resultados.append(
        ("seno", x, aproximado, real, error)
    )


# ==========================================
# COSENO
# ==========================================

for x in valores_trigonometricos:

    aproximado = coseno(x)
    real = math.cos(x)

    error = error_relativo(aproximado, real)

    resultados.append(
        ("coseno", x, aproximado, real, error)
    )


# ==========================================
# EXPONENCIAL
# ==========================================

for x in valores_exponencial:

    aproximado = exponencial(x)
    real = math.exp(x)

    error = error_relativo(aproximado, real)

    resultados.append(
        ("exponencial", x, aproximado, real, error)
    )


# ==========================================
# LOGARITMO NATURAL
# ==========================================

for x in valores_ln:

    aproximado = ln(x)
    real = math.log(x)

    error = error_relativo(aproximado, real)

    resultados.append(
        ("ln", x, aproximado, real, error)
    )


# ==========================================
# MOSTRAR RESULTADOS EN PANTALLA
# ==========================================

print()
print("===== EJERCICIO 4 =====")
print("COMPARACIÓN DE FUNCIONES ESPECIALES")
print()

for funcion, x, aproximado, real, error in resultados:

    print(
        f"{funcion:12s} "
        f"x = {x:6.2f}   "
        f"propia = {aproximado:.15e}   "
        f"math = {real:.15e}   "
        f"error = {error:.6e}"
    )


# ==========================================
# CREAR REPORTE
# ==========================================

with open("reporte_ejercicio4.txt", "w") as archivo:

    archivo.write("============================================\n")
    archivo.write("REPORTE DEL EJERCICIO 4\n")
    archivo.write("ERROR DE LAS FUNCIONES ESPECIALES\n")
    archivo.write("============================================\n\n")

    archivo.write(
        "Se comparan las funciones implementadas en "
        "fiscomp.funciones_especiales\n"
    )

    archivo.write(
        "contra las funciones equivalentes del modulo math.\n\n"
    )


    # --------------------------------------
    # RESULTADOS
    # --------------------------------------

    archivo.write("===== RESULTADOS =====\n\n")

    for funcion, x, aproximado, real, error in resultados:

        archivo.write(f"Funcion: {funcion}\n")
        archivo.write(f"x = {x}\n")
        archivo.write(
            f"Valor calculado: {aproximado:.15e}\n"
        )
        archivo.write(
            f"Valor de math:   {real:.15e}\n"
        )
        archivo.write(
            f"Error relativo:  {error:.6e}\n"
        )
        archivo.write(
            f"Error relativo (%): {error * 100:.6e} %\n"
        )

        archivo.write("\n")


    # --------------------------------------
    # ANÁLISIS
    # --------------------------------------

    archivo.write("===== ANALISIS =====\n\n")

    archivo.write(
        "En general, las funciones implementadas presentan "
        "valores muy cercanos a los obtenidos con el modulo math.\n\n"
    )

    archivo.write(
        "Puede aparecer un error relativo sorprendentemente "
        "alto cuando el valor real de la funcion esta muy "
        "cerca de cero.\n\n"
    )

    archivo.write(
        "Esto ocurre porque el error relativo se calcula como:\n"
    )

    archivo.write(
        "|aproximado - exacto| / |exacto|\n\n"
    )

    archivo.write(
        "Cuando el valor exacto es muy pequeno, una diferencia "
        "absoluta pequena puede producir un error relativo "
        "grande debido a que se divide entre un numero cercano "
        "a cero.\n\n"
    )

    archivo.write(
        "Por esta razon, un error relativo grande no significa "
        "necesariamente que la aproximacion sea mala; tambien "
        "es necesario considerar el error absoluto.\n"
    )
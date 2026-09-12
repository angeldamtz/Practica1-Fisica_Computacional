import math
from fiscomp.precision_numerica import error_relativo

nombre_experimento = input("Nombre del experimento: ")
responsable = input("responsable: ")


voltaje = float(input("Voltaje aplicado (V): "))
distancia = float(input("Distancia entre placas (m): "))
viscosidad = float(input("Viscosidad del aceite (Pa·s): "))

numero_gotas = int(input("Número de gotas: "))


condiciones = (voltaje, distancia, viscosidad)

cargas_medidas = []

for i in range(numero_gotas):
    carga = float(input(f"Carga de la gota {i + 1} (C): "))
    cargas_medidas.append(carga)

cargas_unicas = set(cargas_medidas)

gotas_validas = all(carga > 0 for carga in cargas_medidas)

def estimar_carga_electron(cargas_medidas):
    e_aproximada = min(cargas_medidas)

    estimaciones = []
    detalles_gotas = []

    for carga in cargas_medidas:
        n = round(carga / e_aproximada)
        estimacion = carga / n

        estimaciones.append(estimacion)

        detalles_gotas.append((carga, n, estimacion))


    promedio = sum(estimaciones) / len(estimaciones)

    suma = 0

    for estimacion in estimaciones:
        suma += (estimacion - promedio) ** 2

    desviacion_estandar = math.sqrt(suma / len(estimaciones))

    return promedio, desviacion_estandar, detalles_gotas

carga_estimada, desviacion, detalles_gotas = estimar_carga_electron(cargas_medidas)
carga_electron_aceptada = 1.602176634e-19

error = error_relativo(carga_estimada, carga_electron_aceptada)

resumen = {
    "experimento": nombre_experimento,
    "responsable": responsable,
    "condiciones": condiciones,
    "cargas_medidas": cargas_medidas,
    "cargas_unicas": cargas_unicas,
    "gotas_validas": gotas_validas,
    "carga_estimada": carga_estimada,
    "desviacion_estandar": desviacion,
    "error_relativo": error
}

print()
print("===== RESULTADOS =====")

print(f"Carga estimada del electrón: {carga_estimada:.6e} C")

print(f"Desviación estándar: {desviacion:.6e} C")

print(f"Error relativo: {error:.6e}")

print(f"Error relativo (%): {error * 100:.6f} %")


print()
print("===== DETALLE DE LAS GOTAS =====")

for i, detalle in enumerate(detalles_gotas, 1):

    carga, n, estimacion = detalle

    print(f"Gota {i}:")
    print(f"  Carga medida: {carga:.6e} C")
    print(f"  Número de electrones (n): {n}")
    print(f"  Estimación individual de e: {estimacion:.6e} C")

with open("reporte_recoleccion.txt", "w") as archivo:

    archivo.write("===== REPORTE DEL EXPERIMENTO DE MILLIKAN =====\n\n")

    archivo.write(f"Experimento: {resumen['experimento']}\n")
    archivo.write(f"Responsable: {resumen['responsable']}\n\n")

    archivo.write("===== CONDICIONES =====\n")
    archivo.write(f"Voltaje aplicado: {resumen['condiciones'][0]} V\n")
    archivo.write(f"Distancia entre placas: {resumen['condiciones'][1]} m\n")
    archivo.write(f"Viscosidad del aceite: {resumen['condiciones'][2]} Pa·s\n\n")

    archivo.write("===== CARGAS MEDIDAS =====\n")

    for i, carga in enumerate(resumen["cargas_medidas"], 1):
        archivo.write(f"Gota {i}: {carga:.6e} C\n")

    archivo.write("\n")

    archivo.write("===== RESULTADOS =====\n")
    archivo.write(f"Carga estimada del electrón: {resumen['carga_estimada']:.6e} C\n")
    archivo.write(f"Desviación estándar: {resumen['desviacion_estandar']:.6e} C\n")
    archivo.write(f"Error relativo: {resumen['error_relativo']:.6e}\n")
    archivo.write(f"Error relativo (%): {resumen['error_relativo'] * 100:.6f} %\n\n")

    archivo.write("===== DETALLE DE LAS GOTAS =====\n")

    for i, detalle in enumerate(detalles_gotas, 1):

        carga, n, estimacion = detalle

        archivo.write(f"Gota {i}:\n")
        archivo.write(f"  Carga medida: {carga:.6e} C\n")
        archivo.write(f"  Número de electrones (n): {n}\n")
        archivo.write(f"  Estimación individual de e: {estimacion:.6e} C\n\n")
        
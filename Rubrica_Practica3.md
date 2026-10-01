# Rúbrica — Práctica 3 (Diferencias finitas)

- **Alumno:** Angel Damián Martínez Vera
- **Repositorio:** Practica1-Fisica_Computacional
- **Fecha de revisión:** 30 de septiembre de 2026

Revisión de la Práctica 3

## Resultado de las pruebas automáticas

Corrí tu script de diferencias finitas y revisé el archivo `datos/derivada_sin_x2.dat` que genera con los mismos criterios de `pruebas_practica_03.py`. Resultado: `OK`, `FALLÓ`, `ERROR` (el archivo no se pudo leer) u `OMITIDA` (la prueba no se pudo hacer porque una anterior falló).

| Prueba | Ejercicio | Resultado | Detalle |
| --- | --- | --- | --- |
| `test_corre_sin_errores` | 3 | OK |  |
| `test_genera_el_archivo_de_datos` | 3 | OK |  |
| `test_formato_de_columnas` | 3 | OK |  |
| `test_central_es_mas_precisa_que_adelante_para_h_grande` | 1 y 3 | OK |  |
| `test_el_error_baja_al_reducir_h_al_principio` | 3 | OK |  |

## Ejercicio 1 — `diff_backward` y `diff_central` — 20 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| `diff_backward` correcta: `(f(x0) - f(x0 - h)) / h` | 8 | 8 |
| `diff_central` correcta: `(f(x0 + h/2) - f(x0 - h/2)) / h` | 10 | 10 |
| Docstrings o comentarios en las dos funciones | 2 | 1 |
| **Subtotal Ejercicio 1** | **20** | **19** |

**Observaciones**
- Tus `diff_backward` y `diff_central` son correctas: probé `f(x) = x^2` en `x0 = 6`, `h = 0.1` (dan 11.9 y 12.0) y `sin(x^2)` en `x0 = 1`, y la central usa `h/2`, como en las notas.
- `diff_backward` no tiene ni docstring ni comentario.

## Ejercicio 2 — Derivadas exactas y tabla comparativa — 20 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Las cuatro derivadas exactas son correctas (`sin_x2_prima` con la regla de la cadena y `coseno`) | 8 | 8 |
| Tabla que compara `diff_forward`, `diff_backward` y `diff_central` contra la exacta, con `h` fija | 8 | 8 |
| `error_relativo(aproximado, exacto)` con los argumentos en ese orden | 4 | 4 |
| **Subtotal Ejercicio 2** | **20** | **20** |

**Observaciones**
- Tu tabla del Ejercicio 2 está completa y las derivadas exactas son correctas.

## Ejercicio 3 — Barrido de h: truncamiento contra redondeo — 30 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| El script corre completo, sin errores, en una copia limpia de tu repositorio | 6 | 6 |
| Barrido desde `h = 1.0`, dividiendo entre 2 unas 50 veces, con `diff_forward`, `diff_central` y su error relativo | 8 | 7 |
| Los valores del archivo son correctos | 6 | 6 |
| El archivo queda en `datos/` junto al script (`Path(__file__)`), creando la carpeta si no existe | 5 | 5 |
| Formato: una línea de encabezado que empieza con `#` y cinco columnas separadas por espacios | 5 | 5 |
| **Subtotal Ejercicio 3** | **30** | **29** |

**Observaciones**
- Tu barrido genera un archivo correcto con encabezado y cinco columnas, pero empieza en `h = 0.5` (divides antes de escribir la primera fila) en lugar de `h = 1.0`.

## Ejercicio 4 — ¿Dónde está el h óptimo? — 25 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Encuentras con código la `h` que da el menor error para cada método | 8 | 8 |
| Imprimes el valor medido y el de la fórmula (`sqrt(4*EPS)` y `(24*EPS)**(1/3)`) para los dos métodos | 7 | 7 |
| Explicas que la fórmula supone `f` y sus derivadas de orden 1, y que para `sin(x^2)` en `x0 = 1` no lo son | 5 | 0 |
| Explicas que el barrido solo prueba potencias de 1/2, no cualquier valor de `h` | 5 | 0 |
| **Subtotal Ejercicio 4** | **25** | **15** |

**Observaciones**
- Encuentras con código la `h` de menor error y la comparas con las fórmulas.
- Faltó la respuesta a las preguntas del ejercicio: si los valores coinciden y por qué no tendrían que coincidir.

## Calidad — 5 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Código claro y organizado: secciones por ejercicio, nombres claros, una sola versión del script | 5 | 5 |
| **Subtotal Calidad** | **5** | **5** |

**Observaciones**
- Tu código es claro.

## Ejercicio 5 (opcional) — crédito adicional (hasta 5 pts)

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Generaste la gráfica del error contra `h` y la subiste al repositorio | 3 | 0 |
| Comentas cómo se compara la línea de la `h_opt` teórica con el punto donde tu curva da vuelta | 2 | 0 |
| **Subtotal Ejercicio 5** | **5** | **0** |

**Observaciones**
- El Ejercicio 5 era opcional; no lo entregaste.

## Penalizaciones (criterios transversales)

| Concepto | Rango | Aplicado |
| --- | --- | ---: |
| Entrega difícil de seguir: varias versiones del script y no se distingue cuál es la final | −1 a −2 | 0 |

No descuento por los nombres de tus archivos ni por las carpetas que elegiste, mientras se entienda dónde está cada cosa y funcione.

**Observaciones**
- Sin penalizaciones.

## Calificación final

| Concepto | Máx | Obtenido |
| --- | ---: | ---: |
| Ejercicio 1 — `diff_backward` y `diff_central` | 20 | 19 |
| Ejercicio 2 — Derivadas exactas y tabla | 20 | 20 |
| Ejercicio 3 — Barrido de h | 30 | 29 |
| Ejercicio 4 — h óptimo | 25 | 15 |
| Calidad | 5 | 5 |
| Penalizaciones | | 0 |
| Crédito adicional (Ejercicio 5) | (+5) | 0 |
| **Total** | **100** | **88** |

## Comentarios generales y sugerencias

- Tu código funciona bien.
- Lo que te costó puntos fue la respuesta del Ejercicio 4, que no está.

## Nota

La suma base es 100 pts; el Ejercicio 5 suma crédito adicional hasta 5 pts. Si algo de esta revisión no te queda claro, coméntamelo.

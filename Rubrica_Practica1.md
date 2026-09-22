# Rúbrica — Práctica 1 (Tipos de datos, control de flujo y funciones)

- **Alumno:** Angel Damián Martínez Vera
- **Repositorio:** Practica1-Fisica_Computacional
- **Fecha de revisión:** 21 de septiembre de 2026

Revisión de la Práctica 1

## Resultado de las pruebas automáticas

Resultado: `OK`, `FALLÓ`, `OMITIDA` (la prueba no encontró el archivo o la función con el nombre que espera) o `TIEMPO` (no terminó dentro del límite de tiempo).

| Prueba | Ejercicio | Resultado | Detalle |
| --- | --- | --- | --- |
| `test_factorial` | Base (no se califica) | OK |  |
| `test_seno` | Base (no se califica) | OK |  |
| `test_coseno` | 3 | OK |  |
| `test_exponencial` | 3 | OK |  |
| `test_ln` | 3 | OK |  |
| `test_pi_guardado` | 2 | FALLÓ | SyntaxError: Non-UTF-8 code starting with '\xe1' on line 1, but no encoding declared; see  |
| `test_corre_sin_errores_y_genera_el_reporte` | 1 | OMITIDA | No encontré `recoleccion_datos.py`; tu script se llama `Practica1.py`. Lo revisé a mano (el reporte que subiste tiene datos reales) y corre completo. |
| `test_reporte_existe` | 4 | OK |  |

## Ejercicio 1 — Carga del electrón (experimento de Millikan) — 35 pts

### Parte A — Recolección de datos — 12 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| El script de recolección corre de principio a fin y captura los datos con `input()`, convirtiendo a `int`/`float` lo que regresa como `str` | 3 | 3 |
| `str`: nombre del experimento y del responsable | 1 | 1 |
| `float`/`int`: condiciones del experimento y mediciones | 1 | 1 |
| `bool`: alguna condición con criterio razonable (p. ej., si la gota es válida) | 1 | 1 |
| `tuple`: condiciones que no cambian entre gotas (voltaje, distancia entre placas, viscosidad) | 1 | 1 |
| `list`: carga medida de cada gota, en Coulombs (al menos 3 o 4 gotas) | 1 | 1 |
| `set`: valores únicos medidos | 1 | 1 |
| `dict`: resumen final del experimento, completado en la Parte B | 1 | 1 |
| Datos coherentes: unidades en Coulombs, orden de magnitud cercano a 1e-19, experimento (real o inventado) con sentido | 2 | 2 |
| **Subtotal Parte A** | **12** | **12** |

**Observaciones**
- Tu `Practica1.py` corre completo y tu reporte tiene datos reales (500 V, 0.005 m, cargas ≈ múltiplos de 1.6e-19 C, error relativo de 0.006%). Usas `str`, `float`/`int`, `bool` (`gotas_validas`), `tuple` (`condiciones`), `list`, `set` (`cargas_unicas`) y `dict` (`resumen`). Muy completo.

### Parte B — Estimación de la carga del electrón — 15 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Función que estima la carga del electrón (`estimar_carga_electron` u otro nombre claro) en el mismo script; regresa la estimación de `e` y su desviación estándar | 3 | 3 |
| Primera aproximación con el mínimo de las cargas medidas | 2 | 2 |
| `n = round(carga / e_aproximada)` para cada gota | 2 | 2 |
| Estimación por gota `carga / n`; el promedio de esas estimaciones es la estimación final | 2 | 2 |
| Desviación estándar calculada correctamente sobre las estimaciones por gota (fórmula explícita; población o muestra, pero consistente) | 3 | 3 |
| Error relativo contra `e = 1.602176634e-19 C` (con `error_relativo()` del curso o una versión propia), agregado al `dict` del resumen | 3 | 3 |
| **Subtotal Parte B** | **15** | **15** |

**Observaciones**
- Tu `estimar_carga_electron` está completa y es correcta: `min`, `round` por gota, promedio de las estimaciones individuales y desviación estándar calculada con la suma de las diferencias al cuadrado (evitas el problema de precisión de la fórmula `E[x^2] - media^2`). Regresa `(promedio, desviación, detalles_gotas)`.
- Agregas el error relativo (con `error_relativo` de `fiscomp.precision_numerica` y el valor aceptado 1.602176634e-19) al dict `resumen`.

### Reporte — 8 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Genera un archivo de reporte (por ejemplo `reporte_recoleccion.txt`) con `open()` y `write()` (o `print(file=...)`), en la carpeta del script o en una ruta que funcione en cualquier computadora | 3 | 3 |
| Incluye el resumen del `dict`: carga estimada, desviación estándar y error relativo | 3 | 3 |
| Incluye el detalle de cada gota: carga medida, `n` y estimación individual | 2 | 2 |
| **Subtotal Reporte** | **8** | **8** |

**Observaciones**
- Tu reporte incluye el resumen, las condiciones y el detalle por gota (carga, `n`, estimación individual), con `open()`/`write()`.
- Al escribir el archivo no indicas `encoding="utf-8"`, así que los acentos se ven mal (`Desviaci�n`, `n�mero`); no te descuento por esto, pero es fácil de arreglar agregando `encoding="utf-8"` al `open()`.

## Ejercicio 2 — π con el método de Leibniz — 15 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Suma correctamente la serie de Leibniz (`1 − 1/3 + 1/5 − …`, multiplicada por 4) con muchos términos; no vale copiar `math.pi` ni escribir el valor a mano | 5 | 5 |
| `PI` queda guardado como constante en un archivo que otros programas puedan importar (por ejemplo `fiscomp/constantes.py`), con un valor cercano al real (error relativo menor que 1e-4) y sin volver a correr la suma en cada import | 4 | 1 |
| Comentario que indica qué tan cerca quedaste, comparando contra `math.pi` | 3 | 2 |
| Explicación de por qué no se puede llegar más lejos en un tiempo razonable (convergencia lenta, error del orden de 1/N) | 3 | 3 |
| **Subtotal Ejercicio 2** | **15** | **11** |

**Observaciones**
- Tu `Practica2.py` suma la serie de Leibniz (el número de términos lo pides con `input`) y guarda el resultado en `fiscomp/constantes.py`, con `PI = 3.141591653589774` (un valor correcto, coherente con ~1,000,000 de términos).
- Aquí hay un problema real: guardas ese archivo con `open("fiscomp/constantes.py", "w")` sin `encoding="utf-8"`, así que los acentos de tus comentarios quedaron en otra codificación y Python ya no puede ni importar el archivo (`SyntaxError: Non-UTF-8 code... no encoding declared`). Lo probé directamente: `from fiscomp.constantes import PI` truena. Agrega `encoding="utf-8"` al `open()` y tu módulo va a quedar bien.
- Imprimes en pantalla la comparación contra `math.pi` y el error relativo, pero no lo dejas escrito como comentario junto al valor guardado; agrégalo para que quede documentado sin tener que volver a correr el script.
- El comentario que escribes en `constantes.py` sobre por qué no se puede llegar más lejos (la serie converge como 1/N, tomaría una cantidad de términos poco práctica) es correcto y completo.

## Ejercicio 3 — El resto de las funciones especiales — 35 pts

### `coseno(x)` — 10 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Da resultados correctos en los valores de prueba (`test_coseno`; crédito parcial por valor de `x`) | 6 | 6 |
| Serie de Taylor con `EPS` como criterio de corte, siguiendo el patrón de `seno()` | 2 | 2 |
| Reutiliza `factorial()`, no usa `math`, código claro y con docstring o comentarios | 2 | 1.5 |
| **Subtotal `coseno`** | **10** | **9.5** |

### `exponencial(x)` — 10 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Da resultados correctos en los valores de prueba (`test_exponencial`; crédito parcial por valor de `x`, incluidos los negativos) | 6 | 6 |
| Serie de Taylor con `EPS` como criterio de corte, siguiendo el patrón de `seno()` | 2 | 2 |
| Reutiliza `factorial()`, no usa `math`, código claro y con docstring o comentarios | 2 | 1.5 |
| **Subtotal `exponencial`** | **10** | **9.5** |

### `ln(x)` — 15 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Da resultados correctos en los valores de prueba (`test_ln`; crédito parcial por valor de `x`; 2.0, 5.0 y 10.0 requieren una serie que converja rápido fuera del entorno de `x = 1`) | 8 | 8 |
| Serie con `EPS` como criterio de corte (no un número fijo de términos) y sin `math` | 4 | 4 |
| Funciona para cualquier `x > 0` (serie de `ln((1+y)/(1-y))`, reducción de rango u otra) y lo documentas: qué serie usaste, para qué rango es válida y por qué | 3 | 1.5 |
| **Subtotal `ln`** | **15** | **13.5** |

**Observaciones del Ejercicio 3**
- `coseno`, `exponencial` y `ln` pasan todas las pruebas (8/8, 7/7, 6/6), usan `EPS` como criterio de corte y no usan `math`; `coseno` y `exponencial` reutilizan `factorial()`.
- Ninguna de las cuatro funciones tiene docstring (solo comentarios de sección tipo `# ===== COSENO =====`); agrégaselos.
- Tu `ln` funciona para cualquier `x > 0` (la serie con `y = (x-1)/(x+1)` converge para cualquier valor positivo, aunque lento para `x` grande), pero no hay ningún comentario que explique qué serie usaste ni para qué rango es válida. Documéntalo.

## Ejercicio 4 — Error de sus funciones especiales — 15 pts

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Comparas `seno`, `coseno`, `exponencial` y `ln` contra `math.sin`, `math.cos`, `math.exp` y `math.log` con `error_relativo()`, para varios valores de `x` que permitan ver dónde crece el error | 5 | 4 |
| Reporte con los resultados escrito con `open()` en modo escritura (`w`) y `write()` (unidad 04), legible: `x`, valor aproximado, valor real y error | 3 | 3 |
| Identificas al menos un valor de `x` donde el error es sorprendentemente alto | 3 | 1 |
| Explicas por qué: el valor "real" queda muy cerca de cero y el error *relativo* se dispara aunque el error absoluto sea chico | 4 | 4 |
| **Subtotal Ejercicio 4** | **15** | **12** |

**Observaciones**
- Tu `Practica4.py` compara las cuatro funciones contra `math` en varios valores de `x` y el reporte (`open()`/`write()`) incluye `x`, tu valor, el de `math` y el error relativo. Bien estructurado.
- Los valores que eliges (0 a 2 para seno/coseno, −2 a 2 para exponencial, 0.1 a 2 para ln) nunca se acercan a un punto donde el error se dispare (como `pi` o `pi/2`); agrega esos valores para que puedas verlo con tus propios datos.
- Tu análisis explica correctamente por qué el error relativo se dispara cuando el valor real está cerca de cero (divide entre un número chico), pero como tu tabla no llega a mostrar ningún caso así, no señalas ningún valor concreto de tu propia corrida. Con los valores que te sugerí en el punto anterior lo vas a poder mostrar.

## Reto opcional — crédito adicional (hasta 5 pts)

| Criterio | Máx | Obt. |
| --- | ---: | ---: |
| Reducción de rango en `seno`/`coseno` (llevar `x` a un intervalo chico con identidades trigonométricas) y evidencia de que mejora la precisión para `x` grande | 5 | 0 |

**Observaciones**
- Este reto era opcional y no lo entregaste.

## Penalizaciones (criterios transversales)

| Concepto | Rango | Aplicado |
| --- | --- | ---: |
| Uso de `math` (u otra librería) dentro de las funciones para calcular `sin`, `cos`, `exp`, `log` o `factorial`: la idea es reimplementarlas | −2 a −5 | 0 |
| Código sin comentarios ni docstrings mínimos, nombres de variables poco claros o funciones monolíticas | −1 a −3 | 0 |
| Entrega difícil de seguir: hay versiones distintas del mismo archivo y no se distingue cuál es la final | −1 a −2 | −1 |

No descuento por los nombres de tus archivos, de tus funciones ni por las carpetas que elegiste, mientras se entienda dónde está cada cosa y funcione.

**Observaciones**
- `Practica3.py` es una copia anterior de `fiscomp/funciones_especiales.py` que ya no usas (tiene un import relativo roto, `from .precision_numerica import EPS`, que no funciona fuera de un paquete) y que nada más importa. Te aplico −1 porque puede confundir cuál es la versión final; bórrala o muévela a otra carpeta si la quieres conservar como referencia.

## Calificación final

| Concepto | Máx | Obtenido |
| --- | ---: | ---: |
| Ejercicio 1 — Carga del electrón | 35 | 35 |
| Ejercicio 2 — π con Leibniz | 15 | 11 |
| Ejercicio 3 — Funciones especiales | 35 | 32.5 |
| Ejercicio 4 — Error de las funciones | 15 | 12 |
| Penalizaciones | | −1 |
| Crédito adicional | (+5) | 0 |
| **Total** | **100** | **89.5** |

## Comentarios generales y sugerencias

- Tu Ejercicio 1 es de lo más completo que he revisto: corre bien, usa todos los tipos de datos pedidos y tu reporte tiene datos reales con un error relativo muy chico.
- El problema más importante que corrijas es el de `fiscomp/constantes.py`: al guardarlo sin `encoding="utf-8"` quedó con una codificación que ni siquiera se puede importar. Es un cambio de una línea (`open("fiscomp/constantes.py", "w", encoding="utf-8")`) y resuelve el problema.
- Para el Ejercicio 4, agrega valores como `pi` y `pi/2` a tus listas para que puedas ver con tus propios datos el caso de error alto que ya explicas correctamente en tu análisis.

## Nota

La suma base es 100 pts. El reto opcional suma crédito adicional hasta 5 pts y no sustituye ningún criterio obligatorio de los ejercicios 1–4. Cuando tu trabajo muestra verificación numérica sólida aunque falte algún detalle menor, te doy crédito parcial proporcional. Si algo de esta revisión no te queda claro, coméntamelo y lo revisamos.

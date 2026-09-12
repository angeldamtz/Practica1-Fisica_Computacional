import math

from fiscomp.funciones_especiales import (
    seno,
    coseno,
    exponencial,
    ln
)


print("===== SENO =====")

x = 1.0

print("Mi seno:  ", seno(x))
print("math.sin: ", math.sin(x))


print()
print("===== COSENO =====")

x = 1.0

print("Mi coseno:  ", coseno(x))
print("math.cos:   ", math.cos(x))


print()
print("===== EXPONENCIAL =====")

x = 1.0

print("Mi exponencial: ", exponencial(x))
print("math.exp:       ", math.exp(x))


print()
print("===== LOGARITMO NATURAL =====")

x = 2.0

print("Mi ln:       ", ln(x))
print("math.log:    ", math.log(x))
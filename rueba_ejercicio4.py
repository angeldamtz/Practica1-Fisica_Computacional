
from fiscomp.matrices import Matrix
from fiscomp.algebra_lineal import (
    EliminacionGaussiana,
    SistemaLineal,
    FactorizacionLU,
)

A = Matrix([[2, 1, 1], [1, 1, -2], [5, 10, 5]])
b = [8, -2, 10]

e = EliminacionGaussiana(A, b, coeficientes=True)
print("U:", e.U.data)
print("b transformado:", e.b_nuevo)
print("L:", e.L.data)

sistema = SistemaLineal(A, b)
print("Solución Gauss:", sistema.resolver_gauss())
print("Solución LU:", sistema.resolver_lu())

lu = FactorizacionLU(A)
print("Determinante:", lu.determinante())
print("Inversa:", lu.inversa().data)

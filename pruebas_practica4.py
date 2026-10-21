
from fiscomp.matrices import Matrix, LowerTriangularMatrix, UpperTriangularMatrix
from fiscomp.algebra_lineal import (
    SistemaTriangular,
    EliminacionGaussiana,
    SistemaLineal,
    FactorizacionLU,
)

print("=== PRUEBA 1: MATRICES TRIANGULARES ===")

L = LowerTriangularMatrix([[2, 0, 0], [1, 3, 0], [4, 5, 6]])
U = UpperTriangularMatrix([[2, 1, 4], [0, 3, 5], [0, 0, 6]])

print("Diagonal de L:", L.diagonal())
print("Determinante de L:", L.determinant())
print("Transpuesta de L:", type(L.transpose()).__name__)

print("\n=== PRUEBA 2: SISTEMA TRIANGULAR ===")

sistema = SistemaTriangular(L, [2, 7, 26])
print("Solución:", sistema.resolver())
print("Residuo:", sistema.residuo(sistema.resolver()))

print("\n=== PRUEBA 3: ELIMINACIÓN GAUSSIANA ===")

A = Matrix([[2, 1, 1], [1, 3, -2], [5, 10, 5]])
b = [-8, -2, 10]

eliminacion = EliminacionGaussiana(A, b, coeficientes=True)
print("U:", eliminacion.U.data)
print("L:", eliminacion.L.data)
print("b transformado:", eliminacion.b_nuevo)

print("\n=== PRUEBA 4: GAUSS Y LU ===")

sistema = SistemaLineal(A, b)
print("Solución por Gauss:", sistema.resolver_gauss())

lu = FactorizacionLU(A)
print("Solución por LU:", lu.resolver(b))
print("Determinante:", lu.determinante())
print("Inversa:", lu.inversa().data)

print("\n=== FIN DE LAS PRUEBAS ===")


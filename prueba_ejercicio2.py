
from fiscomp.matrices import LowerTriangularMatrix
from fiscomp.algebra_lineal import SistemaTriangular, MatrizSingularError



L = LowerTriangularMatrix([
    [2, 0, 0],
    [1, 3, 0],
    [4, 5, 6]
])

b = [2, 7, 26]

sistema = SistemaTriangular(L, b)
x = sistema.resolver()

print("Solución:", x)
print("Residuo:", sistema.residuo(x))
print("Flops:", sistema.flops)
print("Vector original b:", b)

# Prueba 1: una matriz que NO es triangular
from fiscomp.matrices import Matrix

try:
    SistemaTriangular(Matrix([[1, 0], [0, 1]]), [1, 1])
except TypeError as error:
    print("Prueba de tipo incorrecto: OK")

# Prueba 2: una matriz singular
try:
    L_singular = LowerTriangularMatrix([
        [1, 0],
        [1, 0]
    ])
    SistemaTriangular(L_singular, [1, 1]).resolver()
except MatrizSingularError:
    print("Prueba de matriz singular: OK")

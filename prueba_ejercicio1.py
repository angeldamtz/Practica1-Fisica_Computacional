
from fiscomp.matrices import (
    Matrix,
    LowerTriangularMatrix,
    UpperTriangularMatrix
)

L = LowerTriangularMatrix([
    [2, 0, 0],
    [1, 3, 0],
    [4, 5, 6]
])

print("Matriz L:")
print(L)

print("Dimensiones:", L.shape())
print("Diagonal:", L.diagonal())
print("Determinante:", L.determinant())
print("Es singular:", L.is_singular())
print("¿Es una Matrix?:", isinstance(L, Matrix))

print("\nTranspuesta de L:")
print(L.transpose())

print(
    "¿La transpuesta es triangular superior?:",
    isinstance(L.transpose(), UpperTriangularMatrix)
)

print("\nPrueba de validación:")

try:
    LowerTriangularMatrix([
        [1, 2],
        [0, 1]
    ])
except ValueError as error:
    print("Error detectado correctamente:", error)



# ============================================================
# PRUEBAS DE MATRIZ TRIANGULAR SUPERIOR
# ============================================================

print("\n===== MATRIZ TRIANGULAR SUPERIOR =====")

U = UpperTriangularMatrix([
    [2, 1, 4],
    [0, 3, 5],
    [0, 0, 6]
])

print("Matriz U:")
print(U)
print("Dimensiones:", U.shape())
print("Diagonal:", U.diagonal())
print("Determinante:", U.determinant())
print("Es singular:", U.is_singular())

print("\nTranspuesta de U:")
UT = U.transpose()
print(UT)

print(
    "¿La transpuesta es triangular inferior?:",
    isinstance(UT, LowerTriangularMatrix)
)


# ============================================================
# VALIDACIONES
# ============================================================

print("\n===== PRUEBAS DE VALIDACION =====")

print("\nMatriz inferior incorrecta:")

try:
    LowerTriangularMatrix([[1, 2], [0, 1]])
except ValueError as error:
    print("Error detectado correctamente:", error)

print("\nMatriz superior incorrecta:")

try:
    UpperTriangularMatrix([[1, 0], [3, 1]])
except ValueError as error:
    print("Error detectado correctamente:", error)

print("\nMatriz no cuadrada:")

try:
    LowerTriangularMatrix([[1, 0, 0], [2, 3, 0]])
except ValueError as error:
    print("Error detectado correctamente:", error)


# ============================================================
# MATRIZ SINGULAR
# ============================================================

print("\n===== MATRIZ SINGULAR =====")

S = LowerTriangularMatrix([
    [2, 0],
    [1, 0]
])

print("Matriz S:")
print(S)
print("Diagonal:", S.diagonal())
print("Determinante:", S.determinant())
print("Es singular:", S.is_singular())

print("\n===== FIN DE LAS PRUEBAS =====")

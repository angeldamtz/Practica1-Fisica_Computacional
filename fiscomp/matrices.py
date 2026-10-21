#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class Matrix:
   
    def __init__(self, data):
        
        if not data:
            raise ValueError("una Matrix necesita al menos un renglón.")

        if not all(len(data[0]) == len(row) for row in data):
            raise ValueError("Todas las filas deben tener la misma longitud.")

        self.data = [list(row) for row in data]
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def __str__(self):
        return "\n".join(
            ["\t".join(map(str, row)) for row in self.data]
        )

    def shape(self):
    
        return (self.rows, self.cols)

    def get_row(self, i):
        
        if not -self.rows <= i < self.rows:
            raise ValueError("Índice de fila fuera de rango.")

        return self.data[i]

    def get_col(self, j):
        
        if not -self.cols <= j < self.cols:
            raise ValueError("Índice de columna fuera de rango.")

        return [row[j] for row in self.data]

    def copy(self):
        
        return Matrix([row[:] for row in self.data])

    def transpose(self):
        
        result = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]

        return Matrix(result)

    def __add__(self, other):
        

        # Verificar que tengan las mismas dimensiones
        if self.shape() != other.shape():
            raise ValueError(
                "Las matrices deben tener las mismas dimensiones."
            )

        resultado = []

        # Recorrer filas
        for i in range(self.rows):
            fila = []

            # Recorrer columnas
            for j in range(self.cols):
                valor = self.data[i][j] + other.data[i][j]
                fila.append(valor)

            resultado.append(fila)

        return Matrix(resultado)

    def __sub__(self, other):
        

        # A - B = A + (-B)
        if self.shape() != other.shape():
            raise ValueError(
                "Las matrices deben tener las mismas dimensiones."
            )

        return self + (other * -1)

    def __mul__(self, other):
        

        # Caso 1: multiplicación por escalar
        if isinstance(other, (int, float)):

            resultado = []

            for i in range(self.rows):
                fila = []

                for j in range(self.cols):
                    valor = self.data[i][j] * other
                    fila.append(valor)

                resultado.append(fila)

            return Matrix(resultado)

        # Caso 2: multiplicación matricial
        elif isinstance(other, Matrix):

            # Las columnas de la primera deben coincidir
            # con las filas de la segunda
            if self.cols != other.rows:
                raise ValueError(
                    "Las dimensiones de las matrices no son compatibles."
                )

            resultado = []

            # Recorrer filas de self
            for i in range(self.rows):

                fila = []

                # Recorrer columnas de other
                for j in range(other.cols):

                    suma = 0

                    # Producto punto de fila por columna
                    for k in range(self.cols):
                        suma += (
                            self.data[i][k]
                            * other.data[k][j]
                        )

                    fila.append(suma)

                resultado.append(fila)

            return Matrix(resultado)

        # Caso 3: tipo no soportado
        else:
            raise TypeError(
                "Solo se puede multiplicar por un número o por otra Matrix."
            )

    # Permite hacer también: escalar * matriz
    __rmul__ = __mul__


if __name__ == "__main__":

    A = Matrix([[1, 2, 3], [4, 5, 6]])

    print(f"Las componentes de la matriz A son {A.data}")
    print(f"La matriz A tiene {A.rows} renglones")
    print(f"La matriz A tiene {A.cols} columnas")

    B = Matrix([[7, 8, 9], [10, 11, 12]])

    print("Matriz A:")
    print(A)

    print(f"La forma de la matriz A es {A.shape()}")
    print(f"El primer renglón de la matriz A es {A.get_row(0)}")
    print(f"El segundo renglón de la matriz A es {A.get_row(1)}")
    print(f"La segunda columna de la matriz A es {A.get_col(1)}")

    print("\nMatriz B:")
    print(B)

    print("\nA + B:")
    print(A + B)

    print("\nA - B:")
    print(A - B)

    print("\nA * 2 (escalar):")
    print(A * 2)

    print("\n2 * A (escalar, del otro lado):")
    print(2 * A)

    C = Matrix([[1, 2], [3, 4], [5, 6]])

    print("\nC:")
    print(C)

    print("\nA * C (matricial):")
    print(A * C)

    print("\nTranspuesta de A:")
    print(A.transpose())

    
class LowerTriangularMatrix(Matrix):
    """
    Representa una matriz triangular inferior.

    Parameters
    ----------
    data : list of list of numbers
        Datos de la matriz.

    Raises
    ------
    ValueError
        Si la matriz no es cuadrada o tiene elementos no nulos
        por encima de la diagonal principal.
    """

    def __init__(self, data):
        
        super().__init__(data)

        if self.rows != self.cols:
            raise ValueError("La matriz debe ser cuadrada.")

        
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != 0:
                    raise ValueError(
                        f"Elemento no nulo en la posición ({i}, {j}). "
                        "La matriz no es triangular inferior."
                    )

                
    def diagonal(self):
        """
        Regresa los elementos de la diagonal principal.

        Returns
        -------
        list
            Elementos de la diagonal.
        """
        return [self.data[i][i] for i in range(self.rows)]

    def determinant(self):
        """
        Calcula el determinante como producto de la diagonal.

        Returns
        -------
        number
            Determinante de la matriz.
        """
        resultado = 1
        for elemento in self.diagonal():
            resultado *= elemento
        return resultado

    def is_singular(self):
        """
        Indica si la matriz es singular.

        Returns
        -------
        bool
            True si algún elemento diagonal es cero.
        """
        return any(elemento == 0 for elemento in self.diagonal())

    def transpose(self):
        """
        Regresa la transpuesta como matriz triangular superior.

        Returns
        -------
        UpperTriangularMatrix
            Transpuesta de la matriz.
        """
        transpuesta = super().transpose()
        return UpperTriangularMatrix(transpuesta.data)


class UpperTriangularMatrix(Matrix):
    """
    Representa una matriz triangular superior.

    Parameters
    ----------
    data : list of list of numbers
        Datos de la matriz.

    Raises
    ------
    ValueError
        Si la matriz no es cuadrada o tiene elementos no nulos
        por debajo de la diagonal principal.
    """

    def __init__(self, data):
        """Inicializa y valida una matriz triangular superior."""
        super().__init__(data)

        if self.rows != self.cols:
            raise ValueError("La matriz triangular superior debe ser cuadrada.")

        for i in range(self.rows):
            for j in range(i):
                if self.data[i][j] != 0:
                    raise ValueError(
                        f"Elemento no nulo en la posición ({i}, {j}). "
                        "Debe ser cero por debajo de la diagonal."
                    )

    def diagonal(self):
        """
        Regresa los elementos de la diagonal principal.

        Returns
        -------
        list
            Elementos de la diagonal.
        """
        return [self.data[i][i] for i in range(self.rows)]

    def determinant(self):
        """
        Calcula el determinante como producto de la diagonal.

        Returns
        -------
        number
            Determinante de la matriz.
        """
        resultado = 1
        for elemento in self.diagonal():
            resultado *= elemento
        return resultado

    def is_singular(self):
        """
        Indica si la matriz es singular.

        Returns
        -------
        bool
            True si algún elemento diagonal es cero.
        """
        return any(elemento == 0 for elemento in self.diagonal())

    def transpose(self):
        """
        Regresa la transpuesta como matriz triangular inferior.

        Returns
        -------
        LowerTriangularMatrix
            Transpuesta de la matriz.
        """
        transpuesta = super().transpose()
        return LowerTriangularMatrix(transpuesta.data)

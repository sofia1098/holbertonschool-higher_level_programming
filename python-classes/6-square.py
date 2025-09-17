#!/usr/bin/python3
"""Este módulo contiene la definición de la clase Square
con sus métodos size, position, area y my_print.
"""


class Square:
    """Define un cuadrado"""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un nuevo cuadrado"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño"""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño con validaciones"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posición"""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición con validaciones"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado"""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado con el carácter # y respetando position"""
        if self.__size == 0:
            print("")
            return

        # Desplazamiento vertical
        for _ in range(self.__position[1]):
            print("")

        # Dibujo con desplazamiento horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

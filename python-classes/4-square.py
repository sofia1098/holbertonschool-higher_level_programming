#!/usr/bin/python3
class Square:
    """Define un cuadrado"""
    

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado con tamaño opcional"""
        self.size = size

    @property
    def size(self):
        """Devuelve el valor de size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el valor de size con validaciones"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado"""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado con el carácter #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)

"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
Repaso examen
Belén María León Fernández
"""


class Vehículo:
    """
    Superclase Vehículo
    """
    @property
    def num_serie(self):
        """
        Metodo get de nun_serie
        :return:
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        Metodo setter de num_serie
        :param value:
        :return:
        """
        self.__num_serie = value

    @property
    def fabricante(self):
        """
        Metodo get de frabricante
        :return:
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        Metodo setter de fabricante
        :param value:
        :return:
        """
        self.__fabricante = value

    @property
    def color(self):
        """
        Metodo get de color
        :return:
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """
        Metodo setter de color
        :param value:
        :return:
        """
        self.__color = value


class Coche(Vehículo):

    """
    Clase Coche
    """
    num_serie = 1;
    cilindrada = 1000;
    fabricante = 'seat';
    color = 'rojo';

    def __init__(self):
        """
        Constructor vacio
        """
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """
        Constructor de la clase
        :param num_serie:
        :param cilindrada:
        :param fabricante:
        :param color:
        """
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def cilindrada(self):
        """
        Metodo get de cilindrada
        :return:
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        Metodo setter de cilindrada
        :param value:
        :return:
        """
        self.__cilindrada = value


"""
Clase Perro.
Autor: Jaime Rabasco Ronda.
Repaso examen
Belén María León Fernández
"""
class Perro:

    def ladrar(self):
        """
        Metodo que ladrar que contiene ladra
        :return:
        """
        print(self.ladra());

    def ladra(self):
        """
        Metodo ladra, devuelve Guau
        :return:
        """
        return 'Guau'


p = Perro();
p.ladrar();
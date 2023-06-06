"""
Clase Perro.
Autor: Jaime Rabasco Ronda.
Repaso examen
Belén María León Fernández
"""
class Perro:

    def ladrar(self):
        print(self.ladra());

    def ladra(self):
        return 'Guau'


p = Perro();
p.ladrar();
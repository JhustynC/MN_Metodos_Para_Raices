from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices

class GaussSeidel(MetodoHallarRaiz, IEncontrarRaices):

    def hallarRaices(self):
        print("gauss")
from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices

class NewtonRaphson(MetodoHallarRaiz, IEncontrarRaices):

    def hallarRaices(self, tolerancia, iteraciones, opc):
        return super().hallarRaices(tolerancia, iteraciones, opc)
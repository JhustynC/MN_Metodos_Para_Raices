from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices

class Muller(MetodoHallarRaiz, IEncontrarRaices):

   def hallarRaices(self, tolerancia, iteraciones):
      return super().hallarRaices(tolerancia, iteraciones)
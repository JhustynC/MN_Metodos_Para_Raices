from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt


class Muller(MetodoHallarRaiz, IEncontrarRaices):

   def hallarRaices(self, tolerancia, iteraciones, opc):
      return super().hallarRaices(tolerancia, iteraciones, opc)
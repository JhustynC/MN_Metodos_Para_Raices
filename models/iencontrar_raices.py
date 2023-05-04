#interfaz EncontrarRaices

from abc import ABCMeta
from abc import abstractmethod

class IEncontrarRaices(metaclass=ABCMeta):
    
    @abstractmethod
    def hallarRaices(self, opc,tolerancia, iteraciones,cifras):...

    
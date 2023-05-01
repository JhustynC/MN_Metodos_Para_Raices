#interfaz EncontrarRaices

from abc import ABCMeta
from abc import abstractmethod

class IEncontrarRaices(metaclass=ABCMeta):
    
    @abstractmethod
    def hallerRaices(self):
        pass

    
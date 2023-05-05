from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 

class Secante(MetodoHallarRaiz, IEncontrarRaices):

   def error_aproximado(self,aproxAct:int, aproxAnt:int):
        return abs((aproxAct - aproxAnt)/aproxAct) * 100

   def secante(self,opc,tole,ite,cif):

      

      #Criterios de finalizacion
      if ite != 0 and i>0 and i == ite:
            #print(f"Iteraciones activa {ite}")
            print("\nSe alcanzo el numero de iteraciones")
      elif tole != 0 and ea < tole:
            print("El error alcanzo el umbral, se termina de iterar")
            return xn

   def hallarRaices(self, opc, tolerancia, iteraciones, cifras):
      
      #Segun criterio de finalizacion
      match opc:
         case 2:#Umbral
               cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
         case 3:#Cifras Significativas
               tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral
      
      #Ingreso de la Función
      f = self.obtenerFuncion()

      #Calculamos valor de la raiz
      #valorRaiz = self.secante(f,x0,tolerancia,iteraciones,cifras)
      self.graficarFuncion(f,self.lapoxr)
      
      
      
      
from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt
from numpy import sign
from numpy. lib.scimath import sqrt


class Muller(MetodoHallarRaiz, IEncontrarRaices):

   def muller(self,f, x0, x1, x2, tole, ite, cif):
      ea = float('inf')
      x3 = 0
      i = 0
      print("{:^3} {:^10} {:^10} {:^10} {:^10} {:^10} ".format("i","x0","x1","x2","x3","ea(%)"))
      while True: 
         
         #Metodo
         c = f(x2)
         b = ((x0-x2)**2* (f(x1)-f(x2))-(x1-x2)**2*(f(x0)-f(x2)))/ ((x0-x2)*(x1-x2)*(x0-x1))
         a = ((x1-x2)*(f(x0)-f(x2))-(x0-x2)*(f(x1)-f(x2)))/((x0-x2)*(x1-x2)*( (x0-x1)))
         x3 = x2-(2*c)/(b+sign(b)*sqrt(b**2-4*a*c))
         ea =  self.error_aproximado(x3,x2) #abs(x3-x2)
         self.lapoxr.append(x3)
         self.lea.append(ea)

         #Tabla de valores
         print("{:^3.0f} {:<10.{}g}{:<10.{}g} {:<10.{}g} {:<10.{}g} {:^2.2f}".format( i+1,x0,cif,x1,cif,x2,cif,x3,cif, ea))
         x0 = x1 
         x1 = x2
         x2 = x3
         i+=1
      
       #Criterios de finalizacion
         if ite != 0 and i>0 and i == ite:
               #print(f"Iteraciones activa {ite}")
               print("\nSe alcanzo el numero de iteraciones")
               return x3
         elif tole != 0 and ea < tole:
               print("El error alcanzo el umbral, se termina de iterar")
               return x3


   def hallarRaices(self, opc, tolerancia, iteraciones, cifras):
       #Segun criterio de finalizacion
        match opc:
            case 2:#Umbral
                cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
            case 3:#Cifras Significativas
                tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral
        
        #Ingreso de la Función
        f = self.obtenerFuncion()
        x0  = float(input("ingrese el X0:")) #Ingreso del limite inferior
        x1  = float(input("ingrese el X1:")) #Ingreso del limite inferior
        x2  = float(input("ingrese el X2:")) #Ingreso del limite inferior

        #Calculamos valor de la raiz
        valorRaiz = self.muller(f,x0,x1,x2,tolerancia,iteraciones,cifras)
        print("\nLa aproximacion de la raiz con una toleracion de {} es: {:<20.{}g}".format(tolerancia,valorRaiz,cifras))
        print(self.lapoxr)
        self.graficarFuncionImag(f,self.lapoxr)
        self.lapoxr.clear()
        self.lea.clear()
        _ = input("Presione cualquier tecla para continuar")
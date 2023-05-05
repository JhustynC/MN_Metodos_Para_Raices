from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 

class Secante(MetodoHallarRaiz, IEncontrarRaices):

   def secante(self,f,x0,x1,tole,ite,cif):

      xs = 0
      eap = float("inf")
      i = 0
      print("{:^3} {:^10} {:^10} ".format("i","xs","ea(%)"))

      while True:

         #Metodo
         try:
            xs = x1 - ((f(x1))*(x0-x1) / (f(x0)-(f(x1)))) #Formula del método de la secante.
            ea = self.error_aproximado(x1,x0)
         except:
            print("Division para cero generada, se para las iteraciones")
            return xs
         
         self.lapoxr.append(xs)
         self.lea.append(ea)
         x0 = x1
         x1 = xs

         #Tabla de valores
         print("{:^3.0f}  {:<10.{}g} {:^2.2f}".format( i+1,xs,cif, ea))
         i+=1

         #Criterios de finalizacion
         if ite != 0 and i>0 and i == ite:
               #print(f"Iteraciones activa {ite}")
               print("\nSe alcanzo el numero de iteraciones")
               return xs
         elif tole != 0 and ea < tole:
               print("El error alcanzo el umbral, se termina de iterar")
               return xs


   def hallarRaices(self, opc, tolerancia, iteraciones, cifras):
      
      #Segun criterio de finalizacion
      match opc:
         case 2:#Umbral
               cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
         case 3:#Cifras Significativas
               tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral
      
      #Ingreso de la Función
      f = self.obtenerFuncion()
      x0  = float(input("ingrese el X0:"))
      x1  = float(input("ingrese el X0:")) 

      #Calculamos valor de la raiz
      valorRaiz = self.secante(f,x0,x1,tolerancia,iteraciones,cifras)
      self.graficarFuncion(f,self.lapoxr)
      self.lapoxr.clear()
      self.lea.clear()
      print("\nLa aproximacion de la raiz con una toleracion de {} es: {:<20.{}g}".format(tolerancia,valorRaiz,cifras))
      _ = input("Presione cualquier tecla para continuar")

      
      
      
      
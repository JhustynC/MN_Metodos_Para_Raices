from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

class PuntoFijo(MetodoHallarRaiz, IEncontrarRaices):

    def error_aproximado(self,aproxAct:int, aproxAnt:int):
        return abs((aproxAct - aproxAnt)/aproxAct) * 100


    #TODO: Funcion para trabjar la expresion (f(x)) algebraicamente

    def punto_fijo(self,f,x0,tole,ite,cif):
        xn = 0
        ea = float('inf')
        i = 0
        print("{:^3} {:^10} {:^10} ".format("i","xn","ea(%)"))
        
        while True:
            
            #Metodo
            xn = f(x0)
            self.lapoxr.append(xn)# listas raiz
            ea = self.error_aproximado(xn,x0)
            self.lea.append(ea)# listas eaprox
            
            #Tabla de valores 
            print("{:^3.0f} {:<10.{}g} {:^2.2f}".format( i+1,xn,cif, ea))
            x0 = xn 
            i += 1

            #Criterios de finalizacion
            if ite != 0 and i>0 and i == ite:
                print(f"Iteraciones activa {ite}")
                print("\nSe alcanzo el numero de iteraciones")
                self.graficarFuncion(f,self.lapoxr)  #Grafica de la funcion y puntos
                return xn
            elif tole != 0 and ea < tole:
                print("El error alcanzo el umbral, se termina de iterar")
                self.graficarFuncion(f,self.lapoxr)  #Grafica de la funcion y puntos
                return xn
            

    def hallarRaices(self, opc,tolerancia, iteraciones,cifras):

        #Segun criterio de finalizacion
        match opc:
            case 2:#Umbral
                cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
            case 3:#Cifras Significativas
                tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral
        
        #Ingreso de la Función
        f = self.obtenerFuncion()
        x0  = float(input("ingrese el X0:")) #Ingreso del limite inferior

        #Calculamos valor de la raiz
        valorRaiz = self.punto_fijo(f,x0,tolerancia,iteraciones,cifras)
        print("\nEl valor de la raiz con una toleracion de {} es: {:<20.{}g}".format(tolerancia,valorRaiz,cifras))
        terminar = input() 



        
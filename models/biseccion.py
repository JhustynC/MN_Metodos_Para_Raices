from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

class Biseccion(MetodoHallarRaiz, IEncontrarRaices):

    punto_medio = lambda self ,a, b: (a+b)/2

    def error_aproximado(self, aproxAct:int, aproxAnt:int):
        return abs((aproxAct - aproxAnt)/aproxAct) * 100

    #Se aplica a la funcion de Biseccion
    def validaSignoDiferente(self,f,a,b):
        if(f(a) >  0 and f(b) < 0 or f(b) >  0 and f(a) < 0):
            return True
        else:
            return False
    
    def biseccion(self,f,a,b,ea,tole,ite,cif):

        i = 0
        c = 0

        print("")
        print("{:^60}".format("Metodo de Bisección"))
        print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i","a","b","c","ea(%)"))

        #if tole != 0 and ea < tole : return self.punto_medio(a,b)

        while True:
            
            #Metodo
            i += 1
            c = self.punto_medio(a,b)
            ea = self.error_aproximado(a,b)
            self.lea.append(ea)
            evalua = f(a)*f(c)

            self.lapoxr.append(c)
            if evalua < 0:
                b = c
            elif evalua > 0:
                a = c    
            else:
                print("Se econtro la raiz")
                return c
            
            #Tabla de valores 
            print("{:^10} {:^10f} {:^10f} {:<20.{}g} {:^1}".format(i,a,b,c,cif,round(ea,9)))

            #Criterios de finalizacion
            if ite != 0 and i == ite:
                #print(f"Iteraciones activa {ite}")
                print("\nSe alcanzo el numero de iteraciones")
                return c 
            elif tole != 0 and ea < tole:
                #print(f"Tolerancia activa {tole}")
                print("El error alcanzo el umbral, se termina de iterar")
                return c

    def hallarRaices(self,opc,tolerancia:float , iteraciones:int = 0 ,cifras:int = 3):
        
        #Segun criterio de finalizacion
        match opc:
            case 2:#Umbral
                cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
            case 3:#Cifras Significativas
                tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral


        #Ingreso de la Función
        f = self.obtenerFuncion()
        a = float(input("ingrese el X0:")) #Ingreso del limite inferior
        b = float(input("ingrese el X1:")) #Ingreso del limite superior
        ea = 1 #Error aproximado inicializado en 1

        #if(self.validaSignoDiferente(f,a,b)):
                
        if(f(a) * f(b) < 0): # Verificamos si en el intervalo hay una raiz 
        
            valorRaiz = self.biseccion(f,a,b,ea,tolerancia,iteraciones,cifras)#Calculamos el aproximado de la raiz con Bisección
            #Grafica de la funcion y punto
            self.graficarFuncion(f,self.lapoxr)
            self.lapoxr.clear()
            print("\nLa aproximacion de la raiz con una toleracion de {} es: {:<20.{}g}".format(tolerancia,valorRaiz,cifras))
            _ = input("Presione cualquier tecla para continuar")

            #-----------------------------
        else: # En caso de que la raiz no esta en el intervalo dado
        
            print("No existe una raiz en este intervalo. revise la grafica")

            #Grafica de la funcion y punto
            self.graficarFuncion(f,[self.punto_medio(a,b)])
            #-----------------------------x

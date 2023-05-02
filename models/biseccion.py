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
    
    def biseccion(self,f,a,b,t,ea):

        print("")
        print("{:^60}".format("Metodo de Bisección"))
        print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i" ,"a","b","c","ea(%)"))
        
        i = 0
        c = 0

        if ea < t: return self.punto_medio(a,b)

        while ea > t:

            i += 1
            c = self.punto_medio(a,b)
            ea = self.error_aproximado(a,b)
            evalua = f(a)*f(c)

            if evalua < 0:
                b = c
            elif evalua > 0:
                a = c
            else:
                return c

            #Valores de la Tabla 
            print("{:^10} {:^10f} {:^10f} {:^10f} {:^10}".format(i,a,b,c,round(ea,9)))
        return c      

    def hallarRaices(self,tolerancia, iteraciones, opc):
        #Ingreso de la Función
        f = self.obtenerFuncion()
        
        a = float(input("ingrese el X0:")) #Ingreso del limite inferior
        b = float(input("ingrese el X1:")) #Ingreso del limite superior
        ea = 1 #Error aproximado inicializado en 1
        t = tolerancia #Tolerancia del error

        #if(self.validaSignoDiferente(f,a,b)):
                
        if(f(a) * f(b) < 0): # Verificamos si en el intervalo esta la raiz 
        
            point = self.biseccion(f,a,b,t,ea)#Calculamos el aproximado de la reis con Bisección

            #Grafica de la funcion y punto
            plt.figure("Biseccion")#----------
            xpts = np.linspace(-10,10) #Array de valores, para la grafica
            plt.plot(xpts, f(xpts))
            plt.title("Grafica de la Funcion")
            plt.grid(True, which='both')
            plt.scatter(point,0,c="red")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.axvline(color="black")
            plt.axhline(color="black")
            plt.ylim([-5,5])
            plt.title(label="Metodo Biseccion")
            plt.show()
            #-----------------------------

        else: # En caso de que la raiz no esta en el intervalo dado
        
            print("Ingrese un nuevo intervalo")

            #Grafica de la funcion y punto
            xpts = np.linspace(-10,10, num=100) #Array de valores, para la grafica
            plt.plot(xpts, f(xpts))
            plt.title("Sugerencia desde la Grafica de la Funcion")
            plt.grid(True, which='both')
            plt.axvline(color="black")
            plt.axhline(color="black")
            plt.scatter(self.punto_medio(a,b),0,c="red")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.ylim([-5,5])
            plt.show()
            #-----------------------------x

    
    def hallarRaicesIteraciones(self):
        ...
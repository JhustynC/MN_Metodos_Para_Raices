from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

class PuntoFijo(MetodoHallarRaiz, IEncontrarRaices):

    def error_aproximado(self,aproxAct:int, aproxAnt:int):
        return abs((aproxAct - aproxAnt)/aproxAct) * 100

    def punto_fijo(self,f,x0,t,ite):
        xn = 0
        ea = 0
        print("{:^3} {:^10} {:^10} {:^5}".format("i","xn","ea(%)"))
        for i in range(0,ite):
            xn = f(x0)
            ea = self.error_aproximado(xn,x0)
            if i > 0:
                if(ea < t):    
                    print("{:^3.0f} {:^11f} {:^2.2f} {:^11.2f}".format(i+1,xn,ea)) #Se imprime para saber en que iteracion se cumple la tolerancia
                    
                    #Grafica de la funcion y punto
                    print("")
                    xpts = np.linspace(-5,5) #Array de valores, para la grafica
                    plt.plot(xpts, lambdify(x,sympify("exp(-x) - x"))(xpts))
                    plt.title("Grafica de la Funcion")
                    plt.grid(True, which='both')
                    plt.scatter(xn,0,c="red")
                    plt.xlabel("x")
                    plt.ylabel("f(x)")
                    plt.axvline(color="black")
                    plt.axhline(color="black")
                    plt.ylim([-3,3])
                    plt.show()
                    #-----------------------------
                    
                    return xn
        print("{:^3.0f} {:^11f} {:^2.2f}".format(i+1,xn,ea))
        x0 = xn 

        #Grafica de la funcion y punto
        print("")
        xpts = np.linspace(-5,5) #Array de valores, para la grafica
        plt.plot(xpts, lambdify(self.x,sympify("exp(-x) - x"))(xpts))
        plt.title("Grafica de la Funcion")
        plt.grid(True, which='both')
        plt.scatter(xn,0,c="red")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axvline(color="black")
        plt.axhline(color="black")
        plt.ylim([-3,3])
        plt.show()
        #-----------------------------

    def hallarRaices(self, tolerancia, iteraciones, opc):
        
        f = self.obtenerFuncion()
        x0  = float(input("ingrese el X0:")) #Ingreso del limite inferior
        ea = 0 #Error aproximado inicializado en 1
        t = tolerancia #Tolerancia del error

        valorRaiz = self.punto_fijo(f,x0,tolerancia,iteraciones)
        print("\nEl valor de la raiz con una toleracion de {} es: {:^11f}".format(tolerancia,valorRaiz)) 



        
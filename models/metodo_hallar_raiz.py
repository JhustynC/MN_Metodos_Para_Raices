from sympy import * 
import numpy as np
import matplotlib.pyplot as plt
import math

class MetodoHallarRaiz():
    
    x, y = symbols('x y')
    

    def obtenerFuncion(self):
        fs = sympify(input("ingrese la funcion en terminos de x:"))#Ingreso de la Función
        return lambdify(self.x, fs) #Transfarmamos a una expresion simbolica y que podamos evaluar


    CalcularUmbral = lambda self, cifras: (0.5 * pow(10, 2 - cifras))
    CalcularCifras = lambda self, umbral: int(2 - (math.log(2 * umbral) / math.log(10))) # Calcula el número de cifras significativas para el umbral dado


    def graficarFuncion(self,f,lp:list):
        print("<--Grafica de la funcion en pantalla-->")
        xpts = np.linspace(-5,5) #Array de valores, para la grafica
        plt.plot(xpts,f(xpts))
        plt.title("Grafica de la Funcion")
        plt.grid(True, which='both')
        if(len(lp) != 0): 
            for i in range(len(lp)): 
                plt.scatter(lp[i],0, cmap='Set2' ,label=f'iter {i+1}')
            plt.legend(loc='lower right', ncol = 3,fontsize="small")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axvline(color="black")
        plt.axhline(color="black")
        plt.ylim([-3,3])
        plt.show()

    
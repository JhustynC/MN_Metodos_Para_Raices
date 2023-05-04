from sympy import * 
import numpy as np
import matplotlib.pyplot as plt
import itertools

class MetodoHallarRaiz():
    
    x, y = symbols('x y')
    
    f = 0
    n = 0
    t = 0

    def obtenerFuncion(self):
        fs = sympify(input("ingrese la funcion en terminos de x:"))#Ingreso de la Función
        return lambdify(self.x, fs) #Transfarmamos a una expresion simbolica y que podamos evaluar

    #Grafica de la funcion y punto
    def graficarFuncion(self,f,lp:list):
        print("<--Grafica de la funcion-->")
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
    #-----------------------------
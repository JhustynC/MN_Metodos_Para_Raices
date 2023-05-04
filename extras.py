from sympy import * 
import models.metodo_hallar_raiz as m
from models.agrupacion_metodos import *

x, y = symbols('x y') 
'''

#Se aplica a la funcion de Biseccion
def validaSignoDiferente(f,a,b):
    if(f(a) >  0 and f(b) < 0 or f(b) >  0 and f(a) < 0):
          return True
    else:
        return False


x0 = float(input())
x1 = float(input())
print(validaSignoDiferente(f,x0,x1))
'''
def obtenerFuncion():
        fs = sympify(input("ingrese la funcion en terminos de x:"))#Ingreso de la Función
        return lambdify(x, fs) #Transfarmamos a una expresion simbolica y que podamos evaluar

def metodo(ite = 0, umbral = 0, cif = 4):
        cont = 0
        ea = 1
        while True:
                if ite != 0 and cont == ite:
                        print("Se finalizo por iteraciones")
                        break 
                elif umbral != 0 and ea > umbral:
                        print("Se finalizo por umbral")
                        break 
                
                #metodo asignado
                cont += 1
                ea += 1
                print(f"iteracion {cont}, cifras significativas {cif}")

metodo(umbral=10)

#f = obtenerFuncion()

#mhr = m.MetodoHallarRaiz()

#mhr.graficarFuncion(f=f,lp=[i for i in range(20)])


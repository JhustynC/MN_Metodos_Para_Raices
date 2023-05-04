from sympy import * 
import models.metodo_hallar_raiz as m


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

f = obtenerFuncion()

mhr = m.MetodoHallarRaiz()

mhr.graficarFuncion(f=f,lp=[i for i in range(20)])

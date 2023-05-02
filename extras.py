from sympy import * 
    
x, y = symbols('x y')
def obtenerFuncion():
        fs = sympify(input("ingrese la funcion en terminos de x:"))#Ingreso de la Función
        return lambdify(x, fs) #Transfarmamos a una expresion simbolica y que podamos evaluar

#Se aplica a la funcion de Biseccion
def validaSignoDiferente(f,a,b):
    if(f(a) >  0 and f(b) < 0 or f(b) >  0 and f(a) < 0):
          return True
    else:
        return False

f = obtenerFuncion()
x0 = float(input())
x1 = float(input())

print(validaSignoDiferente(f,x0,x1))

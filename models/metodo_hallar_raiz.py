from sympy import * 

class MetodoHallarRaiz():
    
    x, y = symbols('x y')
    
    f = 0
    n = 0
    t = 0

    def obtenerFuncion(self):
        fs = sympify(input("ingrese la funcion en terminos de x:"))#Ingreso de la Función
        return lambdify(self.x, fs) #Transfarmamos a una expresion simbolica y que podamos evaluar


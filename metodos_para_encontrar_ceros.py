"""Metodos para encontrar ceros.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DqwPVrO61gst0RvaU7aq8Ib90zdo_I4u

# Trabajo 1 - Metodo Biseccion 

## Integrantes: Patricia Cajas & Jhustyn Carvajal
"""

from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols('x y')

punto_medio = lambda a,b: (a+b)/2

def error_aproximado2(aproxAct:int, aproxAnt:int):
  return abs((aproxAct - aproxAnt)/aproxAct) * 100

def biseccion(f,a,b,t,ea):
  
  print("")
  print("{:^60}".format("Metodo de Bisección"))
  print("{:^10} {:^10} {:^10} {:^10} {:^10}".format ("i" ,"a","b","c","ea(%)"))
  
  i = 0
  c = 0

  if ea < t: return punto_medio(a,b)

  while ea > t:

    i += 1
    c = punto_medio(a,b)
    ea = error_aproximado(a,b)
    evalua = f(a)*f(c)

    if evalua < 0:
      b = c
    elif evalua > 0:
      a = c
    else:
      return c

    #Valores de la Tabla 
    print("{:^10} {:^10f} {:^10f} {:^10f} {:^10}".format (i,a,b,c,round(ea,9)))
  return c

#Ingreso de la Función
fs = sympify(input("ingrese la funcion en terminos de x:"))
f = lambdify(x, fs) #Transfarmamos a una expresion simbolica y que podamos evaluar

a = int(input("ingrese el X0:")) #Ingreso del limite inferior
b = int(input("ingrese el X1:")) #Ingreso del limite superior
ea = 1 #Error aproximado inicializado en 1
t = 0.1 #Tolerancia del error

if(f(a) * f(b) < 0): # Verificamos si en el intervalo esta la raiz 
  
  point = biseccion(f,a,b,t,ea)#Calculamos el aproximado de la reis con Bisección

  #Grafica de la funcion y punto
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
  plt.legend()
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
  plt.scatter(punto_medio(a,b),0,c="red")
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.ylim([-5,5])
  plt.show()
  #-----------------------------x

"""# Trabajo 2 - Punto Fijo

## Integrantes: Patricia Cajas & Jhustyn Carvajal
"""

from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols('x y')

def error_aproximado(aproxAct:int, aproxAnt:int):
  return abs((aproxAct - aproxAnt)/aproxAct) * 100

#Ingreso de la Función
fs = sympify(input("ingrese la funcion en terminos de x:"))
f = lambdify(x, fs) #Transfarmamos a una expresion simbolica y que podamos evaluar

solve(exp(-x) - x) #Encontrano los ceros de la funcion

#Valor real de la raiz (Lo usaremos para calcular el Error Relativo Porcentual Verdadero = et)
vr = LambertW(1).evalf()
vr

x0 = 0
tolerancia = 0.1
iteraciones = 100
f = lambdify(x,sympify("exp(-x)")) #trabajo la funcion algebraicamente 

def punto_fijo(f,x0,t,ite):
  xn = 0
  ea = 0
  erpv = 0
  print("{:^3} {:^10} {:^10} {:^5}".format("i","xn","ea(%)","et(%)"))
  for i in range(0,ite):
    xn = f(x0)
    ea = error_aproximado(xn,x0)
    if i > 0:
      if(ea < t):    
        print("{:^3.0f} {:^11f} {:^2.2f} {:^11.2f}".format(i+1,xn,ea,erpv)) #Se imprime para daber en que iteracion se cumple la tolerancia
        
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
    print("{:^3.0f} {:^11f} {:^2.2f} {:^11.2f}".format(i+1,xn,ea,erpv))
    x0 = xn
    erpv = abs(round(vr - xn,10)*100)

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

valorRaiz = punto_fijo(f,x0,tolerancia,100)
print("\nEl valor de la raiz con una toleracion de {} es: {:^11f}".format(tolerancia,valorRaiz))

"""# Trabajo 3 - Newton-Raphson

## Integrantes: Patricia Cajas & Jhustyn Carvajal
"""

from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols('x y')

fs = sympify("e^-x - x")
f = lambdify(x, fs) #Transfarmamos

c = solve(f(x))

f = sympify("x^3 - x - 1")
df = sympify(diff(f,x))
f = lambdify(x,f)
df = lambdify(x,df)
f(x)

iteraciones = 30
x0 = 0
xs = x0 - (f(x0)/df(x0))
xs

for i in range(0,iteraciones):
  xs = x0 - (f(x0)/df(x0))
  print(xs)
  x0 = xs
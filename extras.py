from sympy import * 
from models.agrupacion_metodos import *
import matplotlib.pyplot as plt 
import numpy as np
from models.metodo_hallar_raiz import MetodoHallarRaiz as m
import re

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

#--------------------------------------------------------------------
'''
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
'''
#-----------------------------------------------------------------------

#metodo(umbral=10)

g = m()



def graficarFuncion2(f,lp:list):
	print("")
	ax = plt.figure().add_subplot(projection='3d')
	print("\033[1;31m"+"<--Grafica de la funcion en pantalla-->")
	print("\033[4;35m"+""+'\033[0;m')
	xpts = np.linspace(-5,5,100) #Array de valores, para la grafica
	#ax.title("Grafica de la Funcion")
	ax.grid(True, which='both')
	if(len(lp) != 0): 
		ax.plot(xpts,f(xpts))
		for i in range(len(lp)): 
			ax.scatter(lp[i],0, cmap='Set2' ,label=f'iter {i+1}')
			ax.legend(loc='lower right', ncol = 3,fontsize="small")
	plt.xlabel("x")
	plt.ylabel("f(x)")
	plt.axvline(color="black")
	plt.axhline(color="black")
	#plt.ylim([-15,15])  # adjust the top leaving bottom unchanged
	#ax.view_init(elev=20., azim=-35, roll=0)
	plt.show()

#f = obtenerFuncion()
#g.graficarFuncion(f,[i for i in range(10)])
#graficarFuncion2(f=f,lp=[i for i in range(20)])

#f = input(f"Ingrese la  ecuacion en funcion de x: ")
#Pasar coeficientes a lista
'''
ecuacion = "1x1 + 2x2 + 34x3 - 56x4 =   123"
pcoeficientes = re.compile('[1-9]*x[1-9]')
presultado = re.compile(f'=\s*[1-9][0-9]*')


lista = re.split(r" \s* | = | \+ | - | x[0-9]+",ecuacion)
print(lista)

res_ecu = presultado.findall(ecuacion)[0].replace("=","").replace(" ","")

print((list_coe,res_ecu))
'''
def pedir_ecuaciones(cant_ecu:int):

	list_coe = []
	list_res = []
	matriz_coe = []
	for _ in range(cant_ecu):
		
		list_coe.clear()
		coe = input("Cantidad de coeficientes a ingresar: ")

		for i in range(int(coe)):
			c = float(input(f"x{i+1}:"))
			list_coe.append(c)
			print(list_coe)
		
		matriz_coe.append(list_coe)

		res = float(input("igual a: "))
		list_res.append(res)

		ecua = ""
		for i in range(len(list_coe)):
			if i >= 0 and list_coe[i] < 0:
				ecua += " " + str(list_coe[i]) + f"x{i+1}"
			elif list_coe[i] > 0 and i > 0:
				ecua += " + " + str(list_coe[i]) + f"x{i+1}"
			else:
				ecua += str(list_coe[i]) + f"x{i+1}"
		ecua += f" = {res}"
		print(ecua)
	return (matriz_coe,list_res)

print(pedir_ecuaciones(3))

x = np.linspace(-5, -1, 1000)  # Rango de valores para x

plt.plot()
plt.show()





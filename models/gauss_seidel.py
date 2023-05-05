from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 
import numpy as np

class GaussSeidel(MetodoHallarRaiz, IEncontrarRaices):

	def pedir_ecuaciones(self,cant_ecu:int):

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

	def gaussSeidel(self,A,b,tole,ite,cif):
		
		
		A = np.array([[10, -1 ,2, 0],
					  [-1, 11, -1, 3],
					  [2, -1, 10, -1],
					  [0, 3, -1, 8]])
		
		b = np.array([6,25,-11,15.]) #tiene que ser flotantes

		x = np.zeros_like(b) 
		ea = float("inf")
		it = 0
		print("{:^3} {:^10} {:^10} ".format("i","x","ea(%)"))
		
		while True:
			
			#Metodo
			for i in range (len(b)):
				x[i] = (b[i] - np.sum(A[i][:i]*x[:i]) - np.sum(A[i][i+1:]*x[i+1:]))/A[i][i]

			ea = np.linalg.norm(A@x - b)

			#Tabla de valores
			print("{:^3.0f} {} {:^3.0f}".format(it+1,x,ea))
			it+=1
			
			#Criterios de finalizacion
			if ite != 0 and it == ite:
				#print(f"Iteraciones activa {ite}")
				print("\nSe alcanzo el numero de iteraciones")
				return x
			elif tole != 0 and ea < tole:
				print("El error alcanzo el umbral, se termina de iterar")
				return x


	def hallarRaices(self, opc, tolerancia, iteraciones,cifras ):
		#Segun criterio de finalizacion
		match opc:
			case 2:#Umbral
				cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
			case 3:#Cifras Significativas
				tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral

		#Ingreso de la Función
		'''c = int(input("Cuantas ecuaciones va a ingresar: "))
		t = self.pedir_ecuaciones(c)
		
		A = np.array(t[0])
		b = np.array(t[1])'''

		#Calculamos valor de la raiz
		valorRaiz = self.gaussSeidel(0,0,tolerancia,iteraciones,cifras)
		print("\nLa aproximacion de la raiz con una toleracion de {} es: {}".format(tolerancia,valorRaiz))
		
		_ = input("Presione cualquier tecla para continuar")
		
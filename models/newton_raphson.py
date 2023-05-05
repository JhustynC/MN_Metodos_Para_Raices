from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 

class NewtonRaphson(MetodoHallarRaiz, IEncontrarRaices):

    
    def error_aproximado(self, aproxAct:int, aproxAnt:int):
        return abs((aproxAct - aproxAnt)/aproxAct) * 100

    def newtonRaphson(self,f,df,x0,tole, ite, cif):
        
        ea = float("inf")
        i = 0
        print("{:^3} {:^10} {:^10} ".format("i","xn","ea(%)"))

        while True:
            
            #Metodo
            try:
                if i > 0:
                    xsant = xs
                xs = x0 - (f(x0)/df(x0))
                ea = self.error_aproximado(xs,x0)
            except Exception:
                print("Se genero una division para cero, se termina las iteraciones")
                return xs
            
            if(i > 0 and self.verificarOscilacionDivergencia(xs,xsant) == True): break

            #Calculo de pendiente por punto
            try:
                m = df(x0)
                self.lrt.append(str(m)+"*x-"+str(m*x0)+"+"+str(f(x0)))
            except Exception:
                print(Exception)
                print("Problema al calcular pendiente")

            self.lea.append(ea)
            x0 = xs

            #Tabla de valores
            print("{:^3.0f} {:^3.0f} {:<10.{}g} {:^2.2f}".format( i+1,xs,x0,cif, ea))
            i += 1

            #Criterios de finalizacion
            if ite != 0 and i == ite:
                print(f"Iteraciones activa {ite}")
                print("\nSe alcanzo el numero de iteraciones")
                return xs 
            elif tole != 0 and ea < tole:
                #print(f"Tolerancia activa {tole}")
                print("El error alcanzo el umbral, se termina de iterar")
                return xs 

    
    def hallarRaices(self, opc, tolerancia, iteraciones, cifras):
        #Segun criterio de finalizacion
        match opc:
            case 2:#Umbral
                cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
            case 3:#Cifras Significativas
                tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral
        
        #Ingreso de la Función
        #f = self.obtenerFuncion()
        try:
            fs = sympify(input("ingrese la funcion en terminos de x:"))
            dfs = sympify(diff(fs,self.x))
            f = lambdify(self.x,fs)
            df = lambdify(self.x,dfs)
        except Exception:
            ...

        x0  = float(input("ingrese el X0:")) #Ingreso del limite inferior

        #Calculamos valor de la raiz
        valorRaiz = self.newtonRaphson(f,df,x0,tolerancia,iteraciones,cifras)
        self.graficarRectas(f,self.lrt)
        print("\nLa aproximacion de la raiz con una toleracion de {} es: {:<20.{}g}".format(tolerancia,valorRaiz,cifras))
        self.lapoxr.clear()
        self.lea.clear()
        _ = input("Presione cualquier tecla para continuar") 
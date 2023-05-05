from models.metodo_hallar_raiz import MetodoHallarRaiz
from models.iencontrar_raices import IEncontrarRaices
from sympy import * 

class PuntoFijo(MetodoHallarRaiz, IEncontrarRaices):

    #* TODO: Funcion para trabjar la expresion (f(x)) algebraicamente

    def funcionAlgebraicamente(self,func:str):
        funcion = sympify(func)
        funPredictora = funcion + symbols('x')
        return lambdify(symbols('x'), funPredictora)

    def punto_fijo(self,f,x0,tole,ite,cif):
        xn = 0
        ea = float('inf')
        i = 0
        print("{:^3} {:^10} {:^10} ".format("i","xn","ea(%)"))
        
        while True:
            
            #Metodo
            try:
                xnant = xn
                xn = f(x0)
                self.lapoxr.append(xn)# listas raiz
                ea = self.error_aproximado(xn,x0)
                self.lea.append(ea)# listas eaprox
            except:
                print("Se genero una Excepcion, no se pudo seguir calculando aproximaciones")
                return xn
            
            if(i > 0 and self.verificarOscilacionDivergencia(xn,xnant) == True): break

            #Tabla de valores 
            print("{:^3.0f} {:<10.{}g} {:^2.2f}".format( i+1,xn,cif, ea))
            x0 = xn 
            i += 1


            #Criterios de finalizacion
            if ite != 0 and i>0 and i == ite:
                #print(f"Iteraciones activa {ite}")
                print("\nSe alcanzo el numero de iteraciones")
                return xn
            elif tole != 0 and ea < tole:
                print("El error alcanzo el umbral, se termina de iterar")
                return xn
            

    def hallarRaices(self, opc,tolerancia, iteraciones,cifras):

        #Segun criterio de finalizacion
        match opc:
            case 2:#Umbral
                cifras = self.CalcularCifras(tolerancia)#Calculo de cifras sig
            case 3:#Cifras Significativas
                tolerancia = self.CalcularUmbral(cifras)#Calculo de umbral
        
        #Ingreso de la Función
        #f = self.obtenerFuncion()
        fs = input("ingrese la funcion en terminos de x:")
        fta = input("Ingrese la funcion trabajada algebraicamente(opcional): ")
        if(len(fta) != 0): 
            f = simplify(fta)
            f = lambdify(self.x,f)
        else:
            f = self.funcionAlgebraicamente(fs)
        x0  = float(input("ingrese el X0:")) #Ingreso del limite inferior

        #Calculamos valor de la raiz
        valorRaiz = self.punto_fijo(f,x0,tolerancia,iteraciones,cifras)
        print("\nLa aproximacion de la raiz con una toleracion de {} es: {:<20.{}g}".format(tolerancia,valorRaiz,cifras))
        self.graficarFuncion(f,self.lapoxr)
        self.lapoxr.clear()
        self.lea.clear()
        _ = input("Presione cualquier tecla para continuar")



        
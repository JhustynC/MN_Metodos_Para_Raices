
#from agrupacion_metodos import *
from models.agrupacion_metodos2 import *

def validarNumero(string,i,vi=None,vf=None):
    match i:
        case 1: 
            try: # Validamos que la opcion sea un entero 
                num = int(string)
                if(vi != None and vf != None):
                    if(num >= vi and num <= vf): 
                        return num
                    else: return False
                return num
            except Exception:
                print("Dato Incorrecto (No es entero)")
        case 2:
            try: # Validamos que la opcion sea un flotante 
                num = float(string)
                if(vi != None and vf != None): 
                    if(num >= vi and num <= vf): 
                        return num
                    else: return False
                return num
            except Exception:
                print("Dato Incorrecto (No es flotante)")
    return False


def seleccionar_opcion_metodo():
    op = 0

    while True:    
        print( "\n"+"\033[1;4;32m"+"  Metodos para encontrar la raices  "+'\033[0;m') 
        print("\033[1;36m"+"1.Biseccion")
        print("\033[1;36m"+"2.Punto Fijo")
        print("\033[1;36m"+"3.Newton-Raphson")
        print("\033[1;36m"+"4.Secante")
        print("\033[1;36m"+"5.Muller")
        print("\033[1;36m"+"6.Gauss-Seidel")
        print("\033[1;36m"+"7.Modificar Iteraciones - Tolerancia/Umbral (por Default)")
        print("\033[1;36m"+"8.Salir")
        print("\033[4;35m"+""+'\033[0;m')
        op =  validarNumero(input("Ingrese una opcion: "),1,1,8)
        if(op != False): return op
        print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
        print("\nOpcion Incorrecta, vuelva a intentar")


def menu():
    #-------------------------------
    tolerancia = 0.01
    n = 0
    cifras = 4
    #-------------------------------
    biseccion = Biseccion()
    punto_fijo = PuntoFijo()
    newton_raphson = NewtonRaphson()
    secante = Secante()
    muller = Muller()
    gauss_seidel = GaussSeidel()
    #-------------------------------
    while True:
        print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
        opm = seleccionar_opcion_metodo()#opcion para seleccionar metodo
        opc = 0 #opcion para seleccionar criterio de finalizacion
        if opm != 7 and opm != 8:
            print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
            while True:
                print( "\n"+"\033[1;4;32m"+"   Criterio de Finalización "+'\033[0;m') 
                print("\033[1;36m"+"1.Iteraciones")
                print("\033[1;36m"+"2.Tolerancia/Umbral")
                print("\033[1;36m"+"3.Cifras Significativas")
                print("\033[1;36m"+"4.Regresar")
                print("\033[4;35m"+""+'\033[0;m')
                opc = validarNumero(input("Ingrese una opcion:"),1,1,4)
                if( opc != False): 
                     match opc:
                        case 1:#Iteraciones
                            n = validarNumero(input("Ingrese un numero de iteraciones:"),1)
                            cifras = validarNumero(input("Ingrese un numero de cifras significativas:"),1)
                            if cifras != False and n != False: break
                        case 2:#Umbral
                            tolerancia = validarNumero(input("Ingrese un numero de tolerancia/umbral:"),2)
                            if tolerancia != False: break
                        case 3:#Cifras Significativas
                            cifras = validarNumero(input("Ingrese un numero de cifras significativas:"),1)
                            if cifras != False: break
                        case 4: 
                            print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
                            break
                print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
                print("\nOpcion Incorrecta, vuelva a intentar")
        #--------------------------------------------------------------------
        if opc != 4:
            print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
            match opm:
                case 1:
                    biseccion.hallarRaices(tolerancia, n,cifras, opc)
                case 2:
                    punto_fijo.hallarRaices(tolerancia, n, opc)
                case 3:
                    newton_raphson.hallarRaices(tolerancia, n, opc)
                case 4:
                    secante.hallarRaices(tolerancia, n, opc)
                case 5:
                    muller.hallarRaices(tolerancia, n, opc)
                case 6:
                    gauss_seidel.hallarRaices(tolerancia, n, opc)
                case 7:
                    print("\n"+"\033[1;36m"+f"El valor de las iteraciones es: {n}")
                    print("\033[1;36m"+f"El valor de la tolerancia es: {tolerancia}")
                    print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
                    while True:
                        print( "\n"+"\033[1;4;32m"+"   Modificar Valores Default  "+'\033[0;m') 
                        print("\033[1;36m"+"1.Iteraciones")
                        print("\033[1;36m"+"2.Tolerancia/Umbral")
                        print("\033[1;36m"+"3.Regresar")
                        print("\033[4;35m"+""+'\033[0;m')
                        opc = validarNumero(input("Ingrese una opcion:"),1,1,3)
                        if( opc != False): 
                            match opc:
                                case 1:
                                    n = validarNumero(input("Ingrese un numero de iteraciones:"),1)
                                    if n != False: break
                                case 2:
                                    tolerancia = validarNumero(input("Ingrese un numero de tolerancia/umbral:"),2)
                                    if tolerancia != False: break
                                case 3:
                                    break
                        print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
                        print("\nOpcion Incorrecta, vuelva a intentar")
                    
                case 8:
                    print("\033[1;31m"+"Gracias por usar el programa")
                    print("\033[4;35m"+""+'\033[0;m')
                    break           
        

def main():
    menu()
    

if __name__ == "__main__":
    main()

#TODO: Graficar todas las iteraciones Newton-Secante-Muller

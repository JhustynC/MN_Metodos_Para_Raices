from agrupacion_metodos import *


def seleccionar_opcion_menu():
    op = 0

    while True:  
       
        print( "\n"+"\033[1;4;32m"+"  Metodos para encontrar la raices  "+'\033[0;m') 
        print("\033[1;36m"+"1.Biseccion")
        print("\033[1;36m"+"2.Punto Fijo")
        print("\033[1;36m"+"3.Newton-Raphson")
        print("\033[1;36m"+"4.Secante")
        print("\033[1;36m"+"5.Muller")
        print("\033[1;36m"+"6.Gauss-Seidel")
        print("\033[1;36m"+"7.Salir")
        print("\033[4;35m"+""+'\033[0;m')
      
        try: # Validamos que la opcion sea un entero y esete en el rango
            op = int(input("Ingrese una opcion:"))
            if(op > 0 or op <= 7): 
                return op
        except Exception:
            print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
            print("\nOpcion Incorrecta, vuelva a intentar")


def menu():
    biseccion = Biseccion()
    punto_fijo = PuntoFijo()
    newton_raphson = NewtonRaphson()
    secante = Secante()
    muller = Muller()
    gauss_seidel = GaussSeidel()

    while True:
        op = seleccionar_opcion_menu()
        
        #TODO: Pedir datos aqui, iteraciones, umbral/tolerancia y funcion a evaluar

        match op:
            case 1:
                biseccion.hallarRaices()
            case 2:
                punto_fijo.hallarRaices()
            case 3:
                newton_raphson.hallarRaices()
            case 4:
                secante.hallarRaices()
            case 5:
                muller.hallarRaices()
            case 6:
                gauss_seidel.hallarRaices()
            case 7:
                print("Gracias por usar el programa")
                break           
    

def main():
    menu()
    

if __name__ == "__main__":
    main()

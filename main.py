from agrupacion_metodos import *


def seleccionar_opcion_menu():
    op = 0
    while True:    
        print("\n\033[2J\033[1;1f") # Borrar pantalla y situar cursor
        print("\033[1;4;32m"+"  Metodos para encontrar la raices  "+'\033[0;m') 
        print("\033[1;36m"+"1.Biseccion")
        print("\033[1;36m"+"2.Punto Fijo")
        print("\033[1;36m"+"3.Newton-Raphson")
        print("\033[1;36m"+"4.Secante")
        print("\033[1;36m"+"5.Muller")
        print("\033[1;36m"+"6.Gauss-Seidel")
        print("\033[1;36m"+"7.Salir")
        print("\033[4;35m"+""+'\033[0;m')
        op = int(input("Ingrese una opcion:"))
        if(isinstance(op, int) and (op > 0 and op <= 7)): #validamos que la opcion sea un entero y esete en el rango
            return op
        
def menu():
    biseccion = Biseccion()
    punto_fijo = PuntoFijo()
    

    op = 0
    while True:
        op = seleccionar_opcion_menu()
        
        #TODO: Pedir datos aqui, iteraciones, umbral/tolerancia y funcion a evaluar

        match op:
            case 1:
                biseccion.hallerRaices()
            case 2:
                punto_fijo.hallerRaices()
            case 3:
                punto_fijo.hallerRaices()
            case 4:
                ...
            case 5:
                ...
            case 6:
                ...
            case 7:
                print("Gracais por usar el programa")
                break           
    

def main():
    menu()
    

if __name__ == "__main__":
    main()

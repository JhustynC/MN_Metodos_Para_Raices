from agrupacion_metodos import *

def imprimir_menu():
    op = -1
    while True:    
        print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
        print("\033[1;4;32m"+"  Metodos para encontrar la raices  "+'\033[0;m') 
        print("\033[1;36m"+"1.Biseccion")
        print("\033[1;36m"+"2.Punto Fijo")
        print("\033[1;36m"+"3.Newton-Raphson")
        print("\033[1;36m"+"4.Secante")
        print("\033[1;36m"+"5.Muller")
        print("\033[4;35m"+""+'\033[0;m')
        op = int(input("Ingrese una opcion:"))
        if(isinstance(op, int) and (op > 0 and op <= 5)): #validamos que la opcion sea un entero y esete en el rango
            return op
            

def menu(op):
    match op:
        case 1:
            #Esto es un cambio para git
            saludar()
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case _:
            ...            
    

def main():
    op = imprimir_menu()
    menu(op)

if __name__ == "__main__":
    main()
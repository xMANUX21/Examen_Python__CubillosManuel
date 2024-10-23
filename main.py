from data import *
from jason import *

usuarios,bonos,totales= cargarDatos()

def menu():
    while True:
        print("======BIENVENIDOS=====")
        print("1. Registro de usuarios")
        print("2. Registro de inasistencias")
        print("3. Registro de bonos")
        print("4. Calcular nomina")
        print("5. Guardar datos")
        print("0. Salir")
        OP=input("\n Digite la opcion que desea realizar joven: ")

        if OP=="1":
            registro(usuarios)

        elif OP=="2":
            inasistencias(usuarios)

        elif OP=="3":
            bonos(usuarios,bonos)
        
        elif OP=="4":
            nomina(usuarios,bonos,totales)
        elif OP=="5":
            guardar(usuarios,bonos,totales)
        elif OP=="0":
            guardar(usuarios,bonos,totales)
            print("Saliendo...")
            break
        else:
            print("opcion invalida")

menu()



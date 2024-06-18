#Ejercicio de contactos
from Funciones import *
while True:
    os.system('cls')
    print('LISTA DE CONTACTOS.\n1: Agregar contacto\n2: Mostrar contactos\n3: Guardar contactos en csv\n 4: Salir:  ')
    time.sleep(3)
    os.system('cls')
    opc=int(input('Ingrese una opcion: '))
    if opc==1:
        Opcion1()
    elif opc==2:
        Opcion2(contactos)
    elif opc==3:
        Opcion3(contactos)
    else:
        print('Adiooos..')
        break
    time.sleep(2)
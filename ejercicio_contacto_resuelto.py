#Ejercicio contacto
import os, time
from funcion_contacto import *

while True:
    os.system('cls')
    print('Menu\n1: Agregar contacto\n2: Ver contactos\n3: Exportar archivo csv\n4: Salir')
    opc=int(input('Ingrese opcion: '))
    
    os.system('cls')
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opcion3()
    else:
        opcion4()
    time.sleep(2)    
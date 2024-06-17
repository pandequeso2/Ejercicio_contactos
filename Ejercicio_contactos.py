#Ejercicio de contactos
import os, time
import csv

contactos= []
while True:
    os.system('cls')
    print('LISTA DE CONTACTOS.\n1: Agregar contacto\n2: Mostrar contactos\n3: Guardar contactos en csv\n 4: Salir:  ')
    os.system('cls')
    opc=int(input('Ingrese una opcion: '))
    if opc==1:
        print('Agregar contactos: ')
        nombre=input('Ingresa tu nombre: ')
        numero_telefonico=int(input('Ingresa tu numero telefonico (sin el +): '))
        correo=input('Ingrese su correo electronico: ')
        contacto= [nombre,numero_telefonico,correo]
        contactos.append(contacto)
        time.sleep(3)
        print('Contacto agregado con exito...')
    elif opc==2:
        print('Mostrar contactos: ')
        if len(contactos) == 0:
            print('No tienes contactos en tu lista, prueba ir a la opción 1.')
        else:
            for c in contactos:
                print(f'Nombre: {c[0]}\nNumero telefonico: {c[1]}\nCorreo: {c[2]} ')
    elif opc==3:
        pass
    else:
        print('Adiooos..')
        break
    time.sleep(3)
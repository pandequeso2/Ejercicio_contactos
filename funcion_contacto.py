#Funciones contacto
import time,os
contactos=[]
def opcion1():
    print('Agregar opciones: ')
        
    nombre=validacion_nombre()
    numero_telefonico=validacion_telefono()
    correo=validacion_correo()
    contacto= {'nombre':nombre,
               'telefono':numero_telefonico,
               'correo':correo}
    contactos.append(contacto)
    time.sleep(2)
    print('Contacto agregado con exito...')        
def opcion2():
    print('Mostrar contactos: ')
    if not contactos:
        print('No tienes contactos en tu lista, prueba ir a la opción 1.')
    else:
        for c in contactos:
            print(f"Nombre: {c['nombre']}\nNumero telefonico: {c['telefono']}\nCorreo: {c['correo']}\n ")      
def opcion3():
    print('Mostrar el formato csv: ')   
    if len(contactos)==0:
        print('No tienes contactos agregados, ve a la opcion 1 primero.')
    else:
        nombre_archivo=input('Ingrese el nombre de el archivo: ')
        try:
            import csv
            with open(f"{nombre_archivo}.csv",'x',newline='') as archivo:
                escritor=csv.DictWriter(archivo,['nombre','telefono','correo'])
                escritor.writerows(contactos)
        except:
            print('ERROR, el nombre de el achivo existente')                                     
def opcion4():
    print('Adioooos..')
    exit()
def validacion_nombre():
    while True:
        nom=(input('Ingresa el nombre: ')).capitalize()
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print('Ingrese almenos de 3 caracteres y solo letras...')
def validacion_telefono():
    while True:
        try:
            tel=int(input('Ingrese su numero telefonico(sin el +56): '))
            if len(str(tel)) == 9 and str(tel)[0]==9:
                return tel
            else:
                print('Error, debe comenzar con 9 y tener 9 digitos.')
        except:
            print('Ingrese un número.')                   
def validacion_correo():
    while True:
        #paterns
        cor=input('Ingrese su correo(sólo @gmail.com): ')
        if cor.strip().lower().endswith("@gmail.com") and len(cor.strip()) >=13:
            return cor
        else:
            print('ERROR, solo se aceptan gmail..')


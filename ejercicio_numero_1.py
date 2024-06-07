#ejercicio 1
import csv,os
from funciones import *
os.system('cls')
lista_nombres= []
for x in range (1,4):
    while True:
        nombre=input('Ingrese El nombre. ')
        if len(nombre) >=3 and nombre.isalpha():
            break
        else:
            print('ERROR, debes ingresar un nombre con mas de 3 caracteres, y sin espacios. ')
    lista_nombres.append(nombre)       
print(lista_nombres)
buscar_nombre_largo(lista_nombres)
crear_csv_nombres(lista_nombres)
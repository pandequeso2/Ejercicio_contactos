#Ejercicio 1
import os
os.system('cls')

notas =[]
lista_asignaturas =['Matematicas','Física','Quimica','Historia','Lenguaje']
print(lista_asignaturas)

#ejercicio 2
for x in range(len(lista_asignaturas)):
    print('Yo estudio ',lista_asignaturas[x])
#ejercicio 3
for x in range(len(lista_asignaturas)):
    nota=float(input(f'Ingrese la nota que te sacaste en {lista_asignaturas[x]} '))
    notas.append(nota)
for x in range(len(lista_asignaturas)):
    print(f'En {lista_asignaturas[x]} te has sacado un :{notas}')
#ejercicio 4
lista_numeros=[]
for x in range(1,6):
    numero=int(input('Ingrese sus 6 numeros ganadores de la loteria ( Desde el 0 hasta el 49 ) :'))
    lista_numeros.append(numero)
    lista_numeros.sort()
print('Los numeros ganadores son :',lista_numeros) 
#ejercicio 5

lista_vector_1 =[1,2,3] 
lista_vector_2 =[-1,0,2]
producto = 0

for x in range(len(lista_vector_1)):
    producto = lista_vector_1 * lista_vector_2
    
    print('El producto de las listas de vectores es :',producto)
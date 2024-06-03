#Pokedex
import os, time
os.system('cls')

pokemones =[]
while True:
        print('''Pokedex.
        1. Añadir pokémon. 
        2. Ver pokémones. 
        3. Eliminar pokémones. 
        3. Experiencia. 
        5. Salir. ''')
        while True:
            try:
                opc= int(input('Ingrese una de las 5 opciónes. '))
                if opc in(1,2,3,4,5):
                    break
                else:
                    print('ERROR, esa opción no esta en la lista') 
            except:
                print('Error Ingrese un numero entero. ')
        if opc==1:
            print('Agregar pokemon. ')
            nombre=input('Ingresa el nombre de el pokemon. ')
            while True:
                try:
                    tipo=int(input('Ingrese el tipo de el pokemon (1. Agua, 2. Fuego, 3. Tierra, 4. Lucha)'))
                    if tipo > 0:
                        break
                    else:
                        print('Ingrese un numero mayor que 0 ')
                except:
                    print('ERROR, ingresa un numero') 
            while True:
                try:
                    exp=int(input('Ingrese el nivel de experiencia'))               
                    if exp > 0:
                        break
                    else:
                        print('Ingrese un numero mayor que 0. ')
                except:
                    print('ERROR, ingrese un numero entero') 
            pokemon={'nombre': nombre,
                     'tipo' : tipo,
                     'exp': exp,
                     'nro': len(pokemones)}  
            pokemones.append(pokemon) 
            time.sleep(2)
            print('Pokemon Agregado con exito... ')
        elif opc ==2:
            print('Ver pokémon. ') 
            for pokemon in pokemones:
                print(pokemon['nombre'],pokemon[tipo],pokemon ['exp'],pokemon ['nro'])
                break       
        elif opc ==3:
            print('Eliminar pokémon. ')
            while True:
                try:
                    nro_eliminar=int(input('Ingrese el numero de el pokemon a eliminar.'))
                    if nro_eliminar > 0:
                        break
                    else:
                        print('ERROR, el numero debe ser mayor que 0. ')
                except:
                    print('ERROR, debe ser un numero entero. ')
            for pokemon in pokemones:
                if nro_eliminar == pokemon('nro'):
                    pokemones.remove(pokemon)
                    time.sleep(2)
                    print('Pokémon eliminado con éxito... ')
                    break
                else:
                    print('ERROR, ese numero no está') 
                       
                                            
        elif opc ==4:
            print('Experiencía. ')
            while True:
                try:
                    nro_a_buscar=int(input('Ingrese el número de el pokémon a buscar. '))
                    if nro_a_buscar >0:
                        break
                    else:
                        print('ERROR, el numero debe ser positivo')
                except:
                    print('ERROR, debe ser un númer entero. ')
            for pokemon in pokemones:
                expe=int(input('Ingrese el nuevo nivél de experiencia. '))
                pokemon['exp'] = expe 
                time.sleep(2)
                print('Experiencia modificada con éxito...')               
        else:
            print('Adiooos. ')
            break        
                       
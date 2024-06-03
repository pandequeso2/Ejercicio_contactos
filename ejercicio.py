#Ejercicio pokemones 
import os,time
os.system('cls')

pokemones=[]
tipos= ('agua','fuego','planta','tierra','lucha')
while True:
    print('''Pokemones
          1. Agregar pokemones 
          2. Ver pokemones.
          3. Actualizar pokemon
          4. Eliminar pokemon
          5. Salir,''')
    
    opc =int(input('Ingrese la opción.'))

    if opc ==1:
        print('Agregar pokemon.')
        nombre=input('Ingrese nombre de el pokemon. ')
        while True:
            try:
                tipo=int(input('Ingrese tipo (1: agua, 2:fuego, 3: planta, 4: tierra, 5:Lucha). '))
                if tipo in (1,2,3,4,5):
                    break
                else:
                    print('No esta en las opciónes')
            except:
                print('Debes ingresar un numero entero')        
        experiencia=int(input('Ingrese la experiencia de un pokemon '))
        pokemon = {
            'nro': len(pokemones) + 1 ,
            'nombre':nombre,
            'tipo':tipos[tipo - 1],
            'experiencia':experiencia
        }
        pokemones.append(pokemon)
        time.sleep(2)
        print('POKEMON AGREGADO...')
    elif opc ==2:
        print('Ver pokémon. ')
        for pokemon  in pokemones:
            print(pokemon['nombre'],pokemon['tipo'],pokemon['experiencia'])
    elif opc==3:
        print('Actualizar la expeiencia')
        numero_buscar=int(input('Ingrese numero pokemon a buscar. '))
        for pokemon in pokemones :
            if numero_buscar == pokemon['nro']:
                exp=int(input('Ingrese la nueva experiencia. '))
                pokemon['experiencia'] = exp
                #pokemon.update({'experiencia': exp})
                time.sleep(1)
                print('Pokemon Actualizado.')
                break
    elif opc==4:
        print('Eliminar pokemon')
        numero_eliminar=int(input('Ingrese el numero de el pokemon a eliminar.'))
        for pokemon in pokemones:
            if numero_eliminar == pokemon['nro']:
                pokemones.remove(pokemon)
                time.sleep(1)
                print('Pokemon eliminado')    
                break
    else:
        print('Adios..')
        break
    time.sleep(3)
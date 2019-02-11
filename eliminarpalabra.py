cantidad = input('\nDigite cuántas palabras tiene la lista: ')
lista = []
posicion = 0
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa lista creada es:', lista)

    palabra = input('\nDigite la palabra a eliminar en la lista: ')

    while posicion < len(lista):
        if lista[posicion] == palabra:
            lista.pop(posicion)
        else:
            posicion += 1

    print('\nLa nueva lista ahora es: ', lista)

else:
    print('\n¡Imposible crear la lista!')
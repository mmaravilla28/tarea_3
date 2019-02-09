cantidad = input('\nDigite cuántas palabras tiene la lista: ')
lista = []
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa lista creada es:', lista)

    palabra = input('\nDigite la palabra a buscar en la lista: ')

    print('\nLa palabra {} aparece {} veces en la lista.'.format(palabra, lista.count(palabra)))

else:
    print('\n¡Imposible crear la lista!')
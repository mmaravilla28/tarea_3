cantidad = input('\nDigite cuántas palabras tiene la lista: ')
lista = []
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa lista creada es:', lista)

    palabra = input('\nDigite la palabra a cambiar en la lista: ')
    nuevapalabra = input('\nDigite la nueva palabra para agregar en la lista: ')

    for x in lista:
        if palabra == x:
            lista[lista.index(x)] = nuevapalabra

    print('\nLa nueva lista ahora es: ', lista)

else:
    print('\n¡Imposible crear la lista!')
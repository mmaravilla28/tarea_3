cantidad = input('\nDigite cuántas palabras tiene la lista: ')
lista = []
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa lista creada es:', lista)
else:
    print('\n¡Imposible crear la lista!')


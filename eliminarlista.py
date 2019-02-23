cantidad = input('\nDigite cuántas palabras tiene la lista: ')
lista1 = []
lista2 = []
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista1.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa lista creada es:', lista1)
else:
    print('\n¡Imposible crear la lista!')

cantidad = input('\nDigite cuántas palabras tiene la lista de palabras a eliminar: ')
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista2.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa lista de palabras a eliminar es:', lista2)
else:
    print('\n¡Imposible crear la lista!')

posicion1 = 0
posicion2 = 0

while posicion1 < len(lista1):

    while posicion2 < len(lista2):

        if lista1[posicion1] == lista2[posicion2]:
            lista1.remove(lista1[posicion1])
        else:
            posicion2 += 1

    posicion1 += 1
    posicion2 = 0

print('\nLa lista ahora es: ', lista1)

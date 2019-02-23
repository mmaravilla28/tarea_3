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

repetidos = 0

for i in lista:
    repetidos = lista.count(i)
    if repetidos > 1:
        lista.remove(i)
    else:
        repstidos = 0

print('\nLa lista sin repeticiones es: ', lista)
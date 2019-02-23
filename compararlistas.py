cantidad = input('\nDigite cuántas palabras tiene la primera lista: ')
lista1 = [] #primera lista
lista2 = [] #segunda lista
lista3 = [] #lista de palabras que aparecen en ambas listas
lista4 = [] #lista de palaabras que aparecen solo en la lista1
lista5 = [] #lista de palabras que aparecen solo en la lista2
palabras = [] #lista de todas las palabras
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista1.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa primera lista es:', lista1)
else:
    print('\n¡Imposible crear la lista!')

#eliminar repetidos en la primera lista
repetidos = 0
for i in lista1:
    repetidos = lista1.count(i)
    if repetidos > 1:
        lista1.remove(i)
    else:
        repetidos = 0

cantidad = input('\nDigite cuántas palabras tiene la segunda lista: ')
cont = 0

if int(cantidad) > 0:
    while cont < int(cantidad):
        cont += 1
        lista2.append(input('Digite la palabra {}: '.format(cont)))

    print('\nLa segunda lista es:', lista2)
else:
    print('\n¡Imposible crear la lista!')

#eliminar repetidos en la segunda lista
repetidos = 0
for i in lista2:
    repetidos = lista2.count(i)
    if repetidos > 1:
        lista2.remove(i)
    else:
        repetidos = 0

#palabras que aparecen en ambas listas
posicion1 = 0
posicion2 = 0

while posicion1 < len(lista1):

    while posicion2 < len(lista2):

        if lista1[posicion1] == lista2[posicion2]:
            lista3.append(lista1[posicion1])
            posicion2 += 1
        else:
            posicion2 += 1

    posicion1 += 1
    posicion2 = 0

lista3.sort()
print('\nPalabras que aparecen en las dos listas: ', lista3)

#palabras que aparecen solo en la primera lista
posicion1 = 0
posicion2 = 0
existe = False

while posicion1 < len(lista1):

    while posicion2 < len(lista2):

        if lista1[posicion1] == lista2[posicion2]:
            posicion2 += 1
            existe = True
        else:
            posicion2 += 1

    if existe == False:
        lista4.append(lista1[posicion1])

    posicion1 += 1
    posicion2 = 0
    existe = False

print('\nPalabras que aparecen solo en la primera lista: ', lista4)

# palabras que aparecen solo en la segunda lista
posicion1 = 0
posicion2 = 0
existe = False

while posicion2 < len(lista2):

    while posicion1 < len(lista1):

        if lista2[posicion2] == lista1[posicion1]:
            posicion1 += 1
            existe = True
        else:
            posicion1 += 1

    if existe == False:
        lista5.append(lista2[posicion2])

    posicion1 = 0
    posicion2 += 1
    existe = False

print('\nPalabras que aparecen solo en la segunda lista: ', lista5)

#se agregan todas las palabras de las listas sin repetidos
for i in lista3:
    palabras.append(i)

for j in lista4:
    palabras.append(j)

for k in lista5:
    palabras.append(k)

palabras.sort()
print('\nTodas las palabras: ', palabras)
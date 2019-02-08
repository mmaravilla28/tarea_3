#definir clase CalculadoraBasica
class CalculadoraBasica:
        #Menu de opciones
        def Menu(self):
                print('\n1)SUMAR 2)RESTAR 3)MULTIPLICAR 4)DIVIDIR 5)SALIR')

        #constructor de la clase
        def iniciar(self, num1, num2):
                self.num1 = num1
                self.num2 = num2

        #función para sumar los números
        def sumar(self):
                print('La suma de {} + {} es = {}'.format(operacion.num1, operacion.num2, int(self.num1) + int(self.num2)))

        #función para restar los números
        def restar(self):
                print('La resta de {} - {} es = {}'.format(operacion.num1, operacion.num2, int(self.num1) - int(self.num2)))

        #función para multiplicar los números
        def multiplicar(self):
                print('La multiplicación de {} * {} es = {}'.format(operacion.num1, operacion.num2, int(self.num1) * int(self.num2)))

        #función para dividir los números
        def dividir(self):
                if int(num2) == 0:
                        print('No se puede dividir por cero')
                else:
                        print('La división de {} / {} es = {}'.format(operacion.num1, operacion.num2, int(self.num1) / int(self.num2)))

#se instancia el objeto operación con la clase CalculadoraBasica
operacion = CalculadoraBasica()
operacion.Menu()
opcion = input('\nSeleccione un operación para iniciar: ')

#mientras la opción selecciona este dentro del rango se ejecuta la operación
while (int(opcion) > 0 and int(opcion) < 5):

        #se solicitan los dos núemros para realizar la operación seleccionada
        num1 = input('\nDigite el primer número: ')
        num2 = input('Digite el segundo número: ')

        #se inicializan los valores de los dos numeros digitados
        operacion.iniciar(num1, num2)

        #se verifica la opción para realizar la operación respectiva
        if int(opcion) == 1:
                operacion.sumar()
                operacion.Menu()
                opcion = input('\nSeleccione un operación para iniciar: ')
        elif int(opcion) == 2:
                operacion.restar()
                operacion.Menu()
                opcion = input('\nSeleccione un operación para iniciar: ')
        elif int(opcion) == 3:
                operacion.multiplicar()
                operacion.Menu()
                opcion = input('\nSeleccione un operación para iniciar: ')
        elif int(opcion) == 4:
                operacion.dividir()
                operacion.Menu()
                opcion = input('\nSeleccione un operación para iniciar: ')





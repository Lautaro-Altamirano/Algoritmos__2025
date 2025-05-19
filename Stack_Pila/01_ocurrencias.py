
#1. Determinar el número de ocurrencias de un determinado elemento en una pila.
from random import randint
from stack import Stack

pila_principal = Stack()
ocurencia = 10
numero_de_ocurencia = 0
for i in range(10):
    numero_random = randint(1,10)
    pila_principal.push(numero_random)
    if numero_random == ocurencia : numero_de_ocurencia += 1

pila_principal.show()
if numero_de_ocurencia > 0:
    print(f"El numero {ocurencia} se repite {numero_de_ocurencia}")
else:
    print(f"No se encontro el numero {ocurencia} en la pila.")
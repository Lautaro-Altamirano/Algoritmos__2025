# 4. Invertir el contenido de una pila, solo puede utilizar 
# una pila auxiliar como estructura extra.
from random import randint
from stack import Stack

pila_pricipal = Stack()
pila_aux = Stack()

for i in range(5):# cargamos pila (stack)
    numero_random = randint(1,20)
    print(numero_random)
    pila_pricipal.push(numero_random)
    
print("Pila original :")
pila_principal.show()

while pila_pricipal.size() > 0 :
    eliminado = pila_pricipal.pop()
    pila_aux.push(eliminado)
    
print("Pila invertida :")
pila_aux.show()

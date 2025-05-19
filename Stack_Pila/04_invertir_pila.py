# 4. Invertir el contenido de una pila, solo puede utilizar 
# una pila auxiliar como estructura extra.
from random import randint
from stack import Stack

pila_pricipal = Stack()
pila_aux = Stack()
print("Pila original :")
for i in range(5):# cargamos pila (stack)
    numero_random = randint(1,20)
    print(numero_random)
    pila_pricipal.push(numero_random)

while pila_pricipal.size() > 0 :
    eliminado = pila_pricipal.pop()
    pila_aux.push(eliminado)
while pila_aux.size() > 0 :
    pila_pricipal.push(pila_aux.pop())
    
print("Pila invertida :")
pila_pricipal.show()

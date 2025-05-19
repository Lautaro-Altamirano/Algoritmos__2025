#11. Dada una pila de letras determinar cuántas vocales contiene.

from stack import Stack
import string
from random import choice

pila_principal = Stack()
#pila_aux = Stack()
vocales = ["A","E","I","O","U"]
contador = 0

for i in range(15):
    letras_random = choice(string.ascii_uppercase)
    pila_principal.push(letras_random) 
pila_principal.show()
while pila_principal.size() > 0:
    value = pila_principal.pop()
    #pila_aux.push(value)
    contador += vocales.count(value) 
#while pila_aux.size() > 0:
    #pila_principal.push(pila_aux.pop())
    
print(f"La pila contiene {contador} vocal/es.")

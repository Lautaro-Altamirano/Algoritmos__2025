#2. Eliminar de una pila todos los elementos impares, es decir que en la misma 
# solo queden números pares.
from random import randint

from stack import Stack

number_stack = Stack()
par_stack = Stack()

# cargar pila con numeros random  
for i in range(5):
    numero_random = randint(1,10)
    print(numero_random)
    number_stack.push(numero_random) #agregamos numeros random a la pila
    
# eliminar los numero inpares 
while number_stack.size() > 0 :
    numero = number_stack.pop()# agrego a number el ultimo de la pila hasta el final 
    if numero % 2 == 0 :# si numero es par lo agrego a la pila par
        par_stack.push(numero) # agrego a par_pila los numeros par    
            
print ("Pila sin numeros inpares")
par_stack.show()

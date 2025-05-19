#5. Determinar si una cadena de caracteres es un palíndromo.
from stack import Stack

pila_principal = Stack()
palabra = input("ingresar una palabra: ")
for letra in palabra:
    if letra != " ":
        pila_principal.push(letra) 
          
palabra_inversa = "" 
for i in range(pila_principal.size()):
    palabra_inversa += pila_principal.pop()
    
if palabra == palabra_inversa:
    print(f"--{palabra} es un políndromo")
else:print(f"--{palabra} no es un políndromo")

# otra forma comparando pila con pila_inversa-
# while pila_principal.size() > 0:
#     eliminada = pila_principal.pop()
#     pila_aux.push(eliminada)
#     pila_palindromo.push(eliminada) 
# while pila_aux.size() > 0: pila_principal.push(pila_aux.pop())

# while pila_principal.size() > 0 and salida == False:
#     if pila_principal.pop() == pila_palindromo.pop():
#         salida = False
#     else:
#         salida = True
#         print(f"La palabra ({palabra}) no es un palíndromo")
# if salida == False:
#     print(f"La palabra ({palabra}) es un palíndromo")

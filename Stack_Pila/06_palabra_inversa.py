# 6. Leer una palabra y visualizarla en forma inversa.
from stack import Stack

pila_principal = Stack()
palabra = input("Ingresar palbra : ")
palabra_inversa = ""
for letra in palabra:
    pila_principal.push(letra)
for i in range(pila_principal.size()):
    palabra_inversa += pila_principal.pop()
print(f"Palabra original : {palabra}")
print(f"Palabra inversa : {palabra_inversa}")

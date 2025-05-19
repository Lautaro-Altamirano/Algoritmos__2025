# 12. Dada una pila con nombres de los personajes de la saga de Star Wars,
# implemente una función 
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos
from stack import Stack

pila_principal = Stack()
pila_aux = Stack()
nombres_star_wars = ["LEÍLA ORGANA","BOBA FETT","DARTH VADER","LUKE SKYWALKER","HAN SOLO","YODA"]
encontrado = False
buscado = "HAN SOLO"


for nombre in nombres_star_wars:
    pila_principal.push(nombre)

while pila_principal.size() > 0:
    value = pila_principal.pop()
    pila_aux.push(value)
    if value == buscado:
        encontrado = True
while pila_aux.size() > 0:
    pila_principal.push(pila_aux.pop())      
      
if encontrado == True:
    print(f"{buscado} fue encontrado en la pila ")
else:
    print(f"{buscado} no fue encontrado en la pila ")
print("---PILA----")
pila_principal.show()
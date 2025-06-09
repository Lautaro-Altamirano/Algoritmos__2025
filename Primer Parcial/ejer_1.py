
# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:

# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

def buscar(superheroe:list, pos=0):
    if pos > len(superheroe):
        return False, pos
    
    if superheroe[pos].upper() == "CAPITAN AMERICA":
        return True, pos
    else:
        return buscar(superheroe, pos + 1)

def listar(superheroe:list, pos=0):
    
    if pos > len(superheroe):
        return None
    
    if pos < len(superheroe):
        print(f"{pos} - {superheroe[pos]}")
        return listar(superheroe, pos + 1)
    
lista_superheroe = list()

lista_superheroe= ["Kang","Hulk","Black Widow","Iron Man","Magneto","Capitan America","Venom","Abomination",
                   "Black Panther","Bullseye","Cable","Cyclops-X-Men97","Deadpool","Dr Doom","Dr Strange","Electro"]

print("- Lista de Superheroes:")
listar(lista_superheroe)
encontrado, posicion = buscar(lista_superheroe)
if encontrado:
    print()
    print(f"- Capitan America se encuentra en la posicion ({posicion})")
    print()


# Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:

from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes

class Superheroes:
    def __init__(self,nombre,real_nombre,aparicion,is_villain,biografia):
        self.nombre = nombre
        self.real_nombre = real_nombre
        self.aparicion = aparicion
        self.is_villain = is_villain
        self.biografia = biografia

    def __str__(self):
        return f"{self.nombre} - {self.real_nombre} - {self.aparicion}"

def order_by_name(item):
    return item.nombre

def order_by_real_nombre(item):
    return item.real_nombre

def order_by_aparicion(item):
    return item.aparicion

lista_supeheroes = List()
Queue_villanos = Queue()
lista_supeheroes.add_criterion("nombre", order_by_name)
lista_supeheroes.add_criterion("real_nombre", order_by_real_nombre)
lista_supeheroes.add_criterion("aparicion", order_by_aparicion)

for superhero in superheroes:
    hero = Superheroes(
        nombre = superhero["name"],
        real_nombre = superhero["real_name"],
        aparicion = superhero["first_appearance"],
        is_villain = superhero["is_villain"],
        biografia = superhero["short_bio"],
    )
    lista_supeheroes.append(hero)

def listado(personajes:List,opc):
    for i in personajes:
        if opc:
            print(f"- {i.nombre}-{i.aparicion}")
        else:
            print(f"- {i.nombre}-{i.real_nombre}")
    return None

def buscar_nombre(personaje:List,nombre):
    pos = personaje.search(nombre,"nombre")
    if pos:
        print()
        print(f"{personaje[pos].nombre}, se encuentra en la posicion: {pos}")
    return None

def listado_villano(personajes):
    villanos = Queue()
    for superheroe in personajes:
        if superheroe.is_villain == True:
            villanos.arrive(superheroe)
            print(f"- {superheroe.nombre}")
    return villanos

def aparicion_antes_1980(cola:Queue):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje.aparicion < 1980:
            cola.move_to_end()
        else:
            cola.attention()
    print()
    print("- Villanos que aparecieron antes de 1980 :")
    cola.show()


# Listado ordenado de manera ascendente por nombre de los personajes.
print("- Listado ordenado de manera ascendente por nombre de los personajes :")
lista_supeheroes.sort_by_criterion("nombre")
listado(lista_supeheroes,False)

# Determinar en que posicion esta The Thing y Rocket Raccoon.
buscar_nombre(lista_supeheroes,"The Thing")
buscar_nombre(lista_supeheroes,"Rocket Raccoon")

#Listar todos los villanos de la lista.
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
print()
print("- Listado de todos los villanos de la lista")
Queue_villanos = listado_villano(lista_supeheroes)
aparicion_antes_1980(Queue_villanos)

# Listar los superheores que comienzan con  Bl, G, My, y W.
print()
print("- Superheores que comienzan con  Bl, G, My, y W :")
for superhero in lista_supeheroes:
    nom = superhero.nombre.upper()
    if nom.startswith(("BL","G","MY","W")):
        print(f"- {superhero.nombre}")


# Listado de superheroes ordenados por fecha de aparación.
print()
print("- Listado de superheroes ordenados por fecha de aparación :")
lista_supeheroes.sort_by_criterion("aparicion")
listado(lista_supeheroes,True)

# Modificar el nombre real de Ant Man a Scott Lang.
index = lista_supeheroes.search("Ant Man","nombre")
if index:
    print()
    print(f"Nombre real :{lista_supeheroes[index].real_nombre}")
    lista_supeheroes[index].real_nombre = "Scott Lang"
    print(f"Nombre real :{lista_supeheroes[index].real_nombre}")

# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print()
print("-Personajes que en su biografia incluyan la palabra time-traveling o suit.")
for supehero in lista_supeheroes:
    if "TIME" in supehero.biografia.upper() or "TRAVELING" in supehero.biografia.upper() or "SUIT" in supehero.biografia.upper():
        print(f"- {supehero.nombre}")

# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
lista_supeheroes.delete_value("Electro","nombre")
lista_supeheroes.delete_value("Baron Zemo","nombre")

 # Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# lista_supeheroes.sort_by_criterion(str("real_nombre"))
# listado(lista_supeheroes,False)

# 6. Dada  una  lista  de  superhéroes  de  comics,  de  los  cuales  se  conoce  su  nombre,  año  aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

from list_ import List
from super_heroes_data import superheroes

class SuperHero:
    """ . """
    def __init__(self,nombre,real_nombre,aparicion,villano,biografia,comics):
        self.nombre = nombre
        self.real_nombre = real_nombre
        self.aparicion = aparicion
        self.villano = villano
        self.biografia = biografia
        self.comics = comics
    def __str__(self):
        return f" - {self.nombre} - {self.real_nombre} - {self.aparicion} - {self.comics} "

def order_by_name(item):
    """ . """
    return item.nombre

def order_by_year(item):
    """ ."""
    return item.aparicion

def cargar_personajes(hero,lista:List):
    """ . """
    for superhero in superheroes:
        personaje = hero(
            nombre = superhero["name"],
            real_nombre = superhero["real_name"],
            aparicion = superhero["first_appearance"],
            villano = superhero["is_villain"],
            biografia = superhero["short_bio"],
            comics = superhero["comics"])

        lista.append(personaje)


lista_de_superheroes = List()
lista_de_superheroes.add_criterion("nombre" , order_by_name)
lista_de_superheroes.add_criterion("aparicion" , order_by_year)
lista_de_superheroes.sort_by_criterion("nombre")

cargar_personajes(SuperHero,lista_de_superheroes)

# A) Eliminar el nodo que contiene la información de Linterna Verde;
lista_de_superheroes.delete_value("Linterna Verde","nombre")

# B) Mostrar el año de aparición de Wolverine;
index = lista_de_superheroes.search("Wolverine","nombre")
if index:
    print(f" - Año de aparición de Wolverine : {lista_de_superheroes[index].aparicion}")
    print()
# C) Cambiar la casa de Dr. Strange a Marvel;
index = lista_de_superheroes.search("Dr Strange","nombre")
if index:

    print(f" - {lista_de_superheroes[index].nombre} - {lista_de_superheroes[index].comics}")
    lista_de_superheroes[index].comics = "dc"
    print(f" - {lista_de_superheroes[index].nombre} - {lista_de_superheroes[index].comics}")
print()

# D) Mostrar  el  nombre  de  aquellos  superhéroes  que  en  su  biografía  menciona  la  palabra
# “traje” o “armadura”;
print(" - Superhéroes que en su biografía menciona la palabra “traje” o “armadura :")
for pers in lista_de_superheroes:
    if "ARMOR" in pers.biografia.upper() or "SUIT" in pers.biografia.upper() or "ARMADURA" in pers.biografia.upper() or "TRAJE" in pers.biografia.upper():
        print(f" - {pers.nombre}")

# E) Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print()
print(" - Superhéroes cuya fecha de aparición sea anterior a 1963 :")
lista_de_superheroes.sort_by_criterion("aparicion")
for pers in lista_de_superheroes:
    if pers.aparicion < 1963:
        print(f" - {pers.nombre} : {pers.aparicion}")

# F) Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print()
lista_de_superheroes.sort_by_criterion("nombre")
index ,index_2 = lista_de_superheroes.search("Captain Marvel","nombre") , lista_de_superheroes.search("Marvel Girl","nombre")
if index:
    print(f" - {lista_de_superheroes[index].nombre} : {lista_de_superheroes[index].comics}")
if index_2:
    print(f" - {lista_de_superheroes[index_2].nombre} : {lista_de_superheroes[index_2].comics}")

# G) Mostrar toda la información de Flash y Star-Lord;
print()
index , index_2 = lista_de_superheroes.search("The Flash","nombre") , lista_de_superheroes.search("Star-Lord","nombre")
if index:
    print(lista_de_superheroes[index]) 
if index_2:
    print(lista_de_superheroes[index_2])

#H) Listar los superhéroes que comienzan con la letra B, M y S;
# I) Determinar cuántos superhéroes hay de cada casa de comic
print()
print(" - Superhéroes que comienzan con la letra B, M y S :")
marvel = 0
dc = 0
for pers in lista_de_superheroes:
    if pers.comics == "marvel":
        marvel += 1
    else:
        dc += 1
        
    if pers.nombre.startswith(("B","M","S")):
        print(f" - {pers.nombre}")

print()
print(" - Cantidad de personajes en cada casa de comics (Marvel,Dc)")
print(f" - Marvel :{marvel}")
print(f" - Dc : {dc}")
print()

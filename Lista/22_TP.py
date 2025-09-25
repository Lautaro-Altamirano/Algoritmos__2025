#22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:


# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron

from jedis_data import jedis
from list_ import List

class Jedi:
    """ . """
    def __init__(self,nombre,maestro,sables_luz,especie):
        self.nombre = nombre
        self.maestro = maestro
        self.sables_luz = sables_luz
        self.especie = especie

    def __str__(self):
        return f" - Nombre: {self.nombre} - Maestro/s: {self.maestro} - Especie: {self.especie}"

def order_by_name(item):
    """ . """
    return item.nombre

def order_by_especie(item):
    """ . """
    return item.especie

def cargar_lista(personaje,lista:List):
    """ . """
    for jedi in jedis:
        pers = personaje (
            nombre = jedi["nombre"],
            maestro = jedi["maestro"],
            sables_luz = jedi["sables_luz"],
            especie = jedi["especie"]
        )
        lista.append(pers)

def aprendices(lista:List):
    """ . """
    print()
    print(" - Todos los padawan de Yoda y Luke Skywalker:")
    for jedi in lista:
        if "Yoda" in  jedi.maestro or "Luke Skywalker" in jedi.maestro :
            print(f" - {jedi.nombre} - Maestro/s: {jedi.maestro}")

lista_de_jedis = List()
lista_de_jedis.add_criterion("nombre" , order_by_name)
lista_de_jedis.add_criterion("especie" , order_by_especie)
cargar_lista(Jedi,lista_de_jedis)


# A)
#print(" - Listado ordenado por nombre:")
lista_de_jedis.sort_by_criterion("nombre")
# print(" - Listado ordenado por especie")
# lista_de_jedis.sort_by_criterion("especie")
# lista_de_jedis.show()

# # B)
# print("")
# print(" - Información de Ahsoka Tano y Kit Fisto:")
# index = lista_de_jedis.search("Ahsoka Tano" , "nombre")
# if index:
#     print(lista_de_jedis[index])
# index = lista_de_jedis.search("Kit Fisto" , "nombre")
# if index:
#     print(lista_de_jedis[index])

# # C)
# aprendices(lista_de_jedis)

# # D)
# print()
# print(" - Jedis de especie humana y twi'lek:")
# for jedi_ in lista_de_jedis:
#     if jedi_.especie in  ("Twi'lek","humano"):
#         print(f" - {jedi_.nombre} - {jedi_.especie}")

# # E)
# print()
# print(" - Todos los Jedi que comienzan con A :")
# for jedi_ in lista_de_jedis:
#     if jedi_.nombre[0] == "A":
#         print(f" - {jedi_.nombre}")

# # F)
# print()
# print(" - Jedis que usaron sable de luz de más de un color :")
# for jedi_ in lista_de_jedis:
#     if len(jedi_.sables_luz) > 1:
#         print(f" - {jedi_.nombre} - {jedi_.sables_luz}")

# # g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# print(" - Jedis que utilizaron sable de luz amarillo o violeta")
# for jedi_ in lista_de_jedis:
#     for i in jedi_.sables_luz:
#         if i in ("amarillo" , "violeta"):
#             print(f" - {jedi_.nombre} - {jedi_.sables_luz}")
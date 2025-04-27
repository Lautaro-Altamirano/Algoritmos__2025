
# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, 
# el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos.
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” 
# realizar las siguientes actividades:


# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no 
# queden más objetos en la mochila;
def usar_la_fuerza(mochila:list, lugar=0):
    if lugar >= len(mochila):
        return False ,lugar
    
    if mochila[lugar].upper() == "SABLE DE LUZ":
        return True ,lugar + 1
    else:
        return usar_la_fuerza(mochila ,lugar + 1) 
   
# c. Utilizar un vector para representar la mochila.
mochila_luk = ["pistola","piedra","lanza","libros","sable de luz","armadura","escudo"]
encontardo , lugar = usar_la_fuerza(mochila_luk)

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
if encontardo:
    print("Se encontró [sable de luz] en la mochila.")  
    print(f"Fue necesario sacar [{lugar}] objetos para encontrarlo.")
else:
    print("No se encontró [sable de luz] en la mochila.")
    
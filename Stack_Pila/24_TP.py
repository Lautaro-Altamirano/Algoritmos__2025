# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad 
# de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
from stack import Stack
pila_principal = Stack()

def cragar_personajes(pila:Stack):
    personajes = [
        {   
            "Nombre" : "Rocket Raccoon",
            "Peliculas" : 6,
        },
        {   
            "Nombre" : "Black Widow",
            "Peliculas" : 7,
        },
        {   
            "Nombre" : "Groot",
            "Peliculas" : 6,   
        },
        {  
            "Nombre" : "Iron Man",
            "Peliculas" : 10,
        },
        {  
            "Nombre" : "Capitán América",
            "Peliculas" : 10,
        },
        {  
            "Nombre" : "Deadpool",
            "Peliculas" : 3,
        },
        {
            "Nombre" : "Doctor Strange",
            "Peliculas" : 6,
        },
    ]
    for personaje in personajes:
        pila.push(personaje)

def posicion_Rocket_Groot(pila:Stack,bus_1:str,bus_2:str):
    aux = Stack()
    pos = 0
    posicion = {}
    
    while pila.size() > 0:
        eliminado = pila.pop()
        
        if (eliminado["Nombre"].upper() == bus_1) or (eliminado["Nombre"].upper() == bus_2):
            posicion[eliminado["Nombre"]] = pos           
        pos += 1
        aux.push(eliminado)  
    while aux.size() > 0:
        pila.push(aux.pop())
        
    return posicion

def mas_5_peliculas(pila:Stack):
    aux = Stack()
    pers = {}
    
    while pila.size() > 0:
        eliminado = pila.pop()
        
        if eliminado["Peliculas"] > 5:
            pers[eliminado["Nombre"]] = eliminado["Peliculas"]
            
        aux.push(eliminado)
        
    while aux.size() > 0:
        pila.push(aux.pop())
        
    return pers 

def buscar(pila:Stack):
    aux = Stack()
    participaciones = 0
    
    while pila.size() > 0:
        eliminado = pila.pop()
        
        if eliminado["Nombre"].upper() == "BLACK WIDOW":
            participaciones = eliminado["Peliculas"]
            
        aux.push(eliminado)
        
    while aux.size() > 0:
        pila.push(aux.pop())
        
    if participaciones:   
        print(f"Black Widow participo en ({participaciones}) películas")   

def nombres_C_D_G(pila:Stack):
    pers = []
    comparacion = ["C","D","G"]
    while pila.size() > 0:
        eliminado = pila.pop()
        nombre = eliminado["Nombre"]
        
        if nombre[0].upper() in comparacion:
            pers.append(nombre)
            
    if pers:
        print(f"Personajes cuyos nombres empiezan con (C , D y G) : {pers}")
        
cragar_personajes(pila_principal)
posiciones = posicion_Rocket_Groot(pila_principal,"ROCKET RACCOON","GROOT")
buscar(pila_principal)
if posiciones:
    print()
    print("Posiciónes en la que se encuentran en la pila:")
    print(posiciones)
personajes_mas_5 = mas_5_peliculas(pila_principal)
if personajes_mas_5:
    print()
    print("Personajes que participaron en más de (5) películas y la cantidad :")
    print(personajes_mas_5)
else:
    print("No se encontró personajes con mas de (5) películas")
print()
nombres_C_D_G(pila_principal)
print()
        
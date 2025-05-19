# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se 
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver 
# las siguientes actividades:

# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, 
# además mostrar el nombre de dichas películas;

# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.

# c. eliminar los modelos de los trajes destruidos mostrando su nombre;

# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar 
# más de un modelo de traje, estos deben cargarse por separado;

# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos 
# repetidos en una misma película;

# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y 
# “Capitan America: Civil War”.

from stack import Stack

def cargar(pila:Stack):
   
    
    trajes_iron_man = [
        {
            "Pelicula": "Spider Man: Homecoming",
            "Modelo" : "Mark XLVII",
            "Estado" : "destruido",
         },
         {
            "Pelicula": "Capitan America: Civil War",
            "Modelo" : "Mark XLIV",
            "Estado" : "dañado",
        },
        {
            "Pelicula": "Avengers: Age of Ultron",
            "Modelo" : "Mark XLIV",
            "Estado" : "destruido",
        },
        {
            "Pelicula": "Capitan America",
            "Modelo" : "Mark XLIV",
            "Estado" : "dañado",
        },
        {
            "Pelicula": "Avengers: Infinity War",
            "Modelo" : "Mark L",
            "Estado" : "destruido",
        },
    ]
    for traje in trajes_iron_man:
        pila.push(traje)
def hulkbuster_y_trajes_dannados(pila:Stack):
    peliculas = []
    dannados = []
    aux = Stack()
    
    while pila.size() > 0:
        eliminado = pila.pop()
        
        if eliminado["Modelo"].upper() == "MARK XLIV":
            peliculas.append(eliminado["Pelicula"])
            
        if eliminado["Estado"].upper() == "DAÑADO":
            dannados.append(eliminado["Modelo"])
            
        aux.push(eliminado)
        
    while aux.size() > 0:
        pila.push(aux.pop())
        
    return peliculas,dannados

def agregar_otro_modelo(pila:Stack,pelicula:str,modelo:str,estado:str):
    aux = Stack()
    nuevo = True
    
    while pila.size() > 0:
        eliminado = pila.pop()
        if eliminado["Pelicula"].upper() == pelicula.upper() and eliminado["Modelo"].upper() == modelo.upper():
            nuevo = False
        aux.push(eliminado)
        
    while aux.size() > 0:
        pila.push(aux.pop())
        
    if nuevo is True:
        pila.push({
            "Pelicula": pelicula,
            "Modelo" : modelo,
            "Estado" : estado,
        })
    else:
        print("No se pueden cargar modelos repetidos")

def trajes_Homecoming_Civil_War(pila:Stack):
    trajes_utilizados = []
    aux = Stack()
    while pila.size() > 0:
        eliminado = pila.pop()
        if (eliminado["Pelicula"].upper() == "SPIDER MAN: HOMECOMING") or (eliminado["Pelicula"].upper() == "CAPITAN AMERICA: CIVIL WAR"):
            trajes_utilizados.append(eliminado["Modelo"])
        aux.push(eliminado)
    while aux.size() > 0:
        pila.push(aux.pop())
    
    print(f"Trajes utilizados en las peliculas : (Spider-Man: Homecoming) y (Capitan America: Civil War) : {trajes_utilizados}")

def eliminar_trajes_destruidos(pila:Stack):
    aux = Stack()
    while pila.size() > 0:
        eliminado = pila.pop()
        if eliminado["Estado"].upper() == "DESTRUIDO":
            print("Traje eliminado : ")
            print(eliminado["Modelo"])
        else:
            aux.push(eliminado)
    while aux.size() > 0:
        pila.push(aux.pop())
        
pila_principal = Stack()
peliculas_hulkbuster = []
trajes_dannados =[]

cargar(pila_principal)
agregar_otro_modelo(pila_principal,"Avengers: Endgame","Mark LXXXV","dañado")
peliculas_hulkbuster, trajes_dannados = hulkbuster_y_trajes_dannados(pila_principal)
trajes_Homecoming_Civil_War(pila_principal)
print(f"Peliculas en la que aparece Mark XLIV (Hulkbuster) : {peliculas_hulkbuster}")
print()
print(f"Trajes que quedaron dañados : {trajes_dannados}")
print()
eliminar_trajes_destruidos(pila_principal)
pila_principal.show()
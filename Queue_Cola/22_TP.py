# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino 
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

from queue_ import Queue
from stack import Stack

cola_principal = Queue()

def carga(cola:Queue):
    personajes = [
        {
        "Nombre_real" : "Tony Stark",
        "Superheroe": "Iron Man",
        "Genero" : "M",    
        },       
        {
        "Nombre_real" : "Steve Rogers",
        "Superheroe": "Capitán América",
        "Genero" : "M",    
        },        
        {
        "Nombre_real" : "Carol Danvers",
        "Superheroe": "Capitana Marvel",
        "Genero" : "F",    
        },        
        {
        "Nombre_real" : "Natasha Romanoff",
        "Superheroe": "Black Widow",
        "Genero" : "F",    
        },       
        {
        "Nombre_real" : "Scott Lang",
        "Superheroe": "Ant Man",
        "Genero" : "M",    
        },        
    ]
    for personaje in personajes:
        cola.arrive(personaje)
        
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
def capitana_marvel(cola:Queue):
    
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje["Superheroe"].upper() == "CAPITANA MARVEL":
            print()
            print("El nombre real del personaje Capitana Marvel es :")
            print(personaje["Nombre_real"])
            break
        cola.move_to_end()
        
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
def superheroes_femeninos_Masculino(cola:Queue):
    femeninos = Stack()
    masculino = Stack()
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje["Genero"].upper() == "F":
            femeninos.push(personaje["Superheroe"])
        elif personaje["Genero"].upper() == "M":
            masculino.push(personaje["Superheroe"])
        cola.move_to_end()
    if femeninos:
        print()
        print("Superhéroes Femeninos:")
        femeninos.show()
    if masculino:
        print()
        print("Superhéroes Masculino:")
        masculino.show()
        
# d. determinar el nombre del superhéroe del personaje Scott Lang;
def scott_lang(cola:Queue):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje["Nombre_real"].upper() == "SCOTT LANG":
            print()
            print("Scott Lang es el Superhéroe :")
            print(personaje["Superheroe"])
            break
        cola.move_to_end()

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan 
# con la letra S;
def nombre_comienzan_s(cola:Queue):
    nombres_s = Stack()
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje["Nombre_real"][0].upper() == "S" or personaje["Superheroe"][0].upper() == "S":
            nombres_s.push(personaje)
        cola.move_to_end()
    if nombres_s:
        print()
        print("Personajes o Superheroés cuyos nombres comienzan con la letra (S) ")
        nombres_s.show()

# f. determinar  si  el  personaje  Carol  Danvers  se  encuentra  en  la  cola  e  indicar  su  nombre 
# de superhéroes.
def carol_danvers(cola:Queue):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje["Nombre_real"].upper() == "CAROL DANVERS":
            print()
            print("El personaje Carol Danvers se encuentra en la cola y su nombre de superhéroe es: ")
            print(personaje["Superheroe"])
            break
        cola.move_to_end()
    
carga(cola_principal)
capitana_marvel(cola_principal)
scott_lang(cola_principal)
nombre_comienzan_s(cola_principal)
carol_danvers(cola_principal)
superheroes_femeninos_Masculino(cola_principal)
# cola_principal.show()
            
# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, 
# de  las  cual  se  cuenta  con  la  hora  de  la  notificación,  la  aplicación  que  la  emitió  y  el  mensaje,  
# resolver las siguientes actividades:

from queue_ import Queue
from stack import Stack

def cargar(cola:Queue):
    smartphones = [
        {
            "Aplicacion" : "Twitter",
            "Mensaje" : "Python 3.11.2 xxxxx",
            "Hora" : 14.45,
        },
        {
            "Aplicacion" : "WhatsApp",
            "Mensaje" : "Nuevo mensaje de xxxxxxx",
            "Hora" : 12.55,
        },
        {
            "Aplicacion" : "Twitter",
            "Mensaje" : "Ultimas noticias de python",
            "Hora" : 12.14,
        },
        {
            "Aplicacion" : "Facebook",
            "Mensaje" : "Solicitud de amistad de xxxxxx",
            "Hora" : 17.55,
        },
        {
            "Aplicacion" : "Instagram",
            "Mensaje" : "Nuevo seguidor",
            "Hora" : 11.15,
        },
    ]
    for smartphon in smartphones:
        cola.arrive(smartphon)
        
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
def facebook(cola:Queue):
    
    for i in range(cola.size()):
        notificacion = cola.on_front()
        if notificacion["Aplicacion"].upper() == "FACEBOOK":
            cola.attention()
        else:
            cola.move_to_end()

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya 
# la palabra ‘Python’, si perder datos en la cola;

def twitter(cola:Queue):
    mensaje = Stack()
    
    for i in range(cola.size()):
        notificacion = cola.on_front()

        if notificacion["Aplicacion"].upper() == "TWITTER":
            if "PYTHON" in notificacion["Mensaje"].upper():
                mensaje.push(notificacion)
        cola.move_to_end()
    if mensaje:
        print()
        print("Notificaciónes de Twitter, cuyo mensaje incluya la palabra (Python) :")
        mensaje.show()
        

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 
# 11:43 y las 15:57, y determinar cuántas son.
def notif_entre_un_rango(cola:Queue):
    pila = Stack()
    cont = 0
    for i in range(cola.size()):
        notificacion = cola.on_front()
        
        if (notificacion["Hora"] > 11.43) and (notificacion["Hora"] < 15.57):
            pila.push(notificacion)
            cont += 1
        cola.move_to_end()
    if pila:
        print()
        print(f"Notificaciónes producidas entre las 11:43 y las 15:57 : ({cont})")
        pila.show()

notificaciones = Queue()

cargar(notificaciones)
facebook(notificaciones)
twitter(notificaciones)
notif_entre_un_rango(notificaciones)

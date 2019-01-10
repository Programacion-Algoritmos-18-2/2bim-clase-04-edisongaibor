from paquete_archivos.miarchivo import MiArchivo
from modelado.modelo import *
# Esta libreria pasa de cadena a json
import json

m = MiArchivo() # objeto para leer el archivo


lista = m.obtener_informacion()
lista_jugadores = []
#Esta identificando la cabecera 
#lista = lista[1:]
for d in lista:
   	datos = json.loads(d)
   	#print(datos["Height"]) #Selecciono la parte del diccionario que quiero que se imprima
   	jugador = Equipo(datos['ShirtName'], datos['Goals'], datos['Height'], datos['Contry'])
   	lista_jugadores.append(jugador)
   	#print (jugador)
    #print(d)
    #print(d.__class__)
    #print(d[0])
    #print("--------------")

operaciones = OperacionesEquipo(lista_jugadores)
print(operaciones.get_promedio_goles())


m.cerrar_archivo()
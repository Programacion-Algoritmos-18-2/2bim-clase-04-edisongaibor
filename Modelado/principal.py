from paquete_archivos.miarchivo import MiArchivo , MiArchivoEscribir
from modelado.mimodelo import *

m = MiArchivo()
m2= MiArchivoEscribir()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
lista_equipos = []
for d in lista:
    # print(d)
    p = Equipo(d[0], d[1], d[2], d[3])
    lista_equipos.append(p)

operacion = Operaciones(lista_equipos)

op = int(input("Para ordenar por nombre digite n, digite cualquier otra letra para ordenar por campeonato"))
if (op== 1):
	lista_equipos2 = operacion.ordenar_nombres()
if(op == 2):
	lista_equipos2 = operacion.ordenar_campeonatos()

for i in lista_equipos2:
	m2.agregar_informacion(i)
	print(i)
m.cerrar_archivo
m2.cerrar_archivo


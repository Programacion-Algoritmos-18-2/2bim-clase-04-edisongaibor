from paquete_archivos.miarchivo import MiArchivo , MiArchivoEscribir
from modelado.mimodelo import Equipo

m = MiArchivo()
m2= MiArchivoEscribir()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

for d in lista:
    # print(d)
    p = Equipo(d[0], d[1], d[2], d[3])
    print(p)
    m2.agregar_informacion(p)

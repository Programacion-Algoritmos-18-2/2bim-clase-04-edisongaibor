import codecs
import sys


class MiArchivo:
    """
    """
    #Abre el archivo
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/datos.txt", "r")

    #Lee linea por linea
    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self):
        self.archivo.close()

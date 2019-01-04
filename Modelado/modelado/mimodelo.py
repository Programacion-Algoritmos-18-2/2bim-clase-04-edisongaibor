class Equipo():
    def __init__(self, nom, ci, camp, juga ):
        self.nombre = nom
        self.ciudad = ci
        self.campeonatos = camp
        self.numJugadores = juga


    def agregar_nombre(self,nom):
        self.nombre = nom
    def obtener_nombre(self):
        return self.nombre
    def agregar_ciudad(self,ci):
        self.ciudad = ci
    def obtener_ciudad(self):
        return self.ciudad
    def agregar_campeonatos(self,camp):
        self.campeonatos =camp
    def obtener_campeonatos(self):
        return self.campeonatos
    def agregar_numJugadores(self,juga):
        self.numJugadores = juga
    def obtener_numJugadores(self):
        return self.numJugadores


    def __str__(self):
            """
            """
            return "%s - %s - %s - %s" % (self.obtener_nombre() ,self.obtener_ciudad () ,self.obtener_campeonatos (),self.obtener_numJugadores())
    def __repr__(self):
        return "%s - %s - %s - %s" % (self.obtener_nombre() ,self.obtener_ciudad () ,self.obtener_campeonatos (),self.obtener_numJugadores())
        

class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipos = listado

    def ordenar_nombres(self):
        return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_nombre())
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
    def ordenar_campeonatos(self):    
        return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_campeonatos())

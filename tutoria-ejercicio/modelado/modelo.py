class Equipo():
	
	def __init__(self, con, shirt, go, hei):
		self.contry = con
		self.shirtname = shirt
		self.goals = go
		self.height = hei

	def set_contry(self):
		self.contry = con
	def get_contry(self):
		return self.contry
	def set_shirtname(self):
		self.shirtname = shirt
	def get_shirtname(self):
		return self.shirtname
	def set_goals(self):
		self.goals = go
	def get_goals(self):
		return self.goals
	def set_height(self):
		self.height = hei
	def get_height(self):
		return self.heigth

def __str__(self):    
    return "%s - %s - %d - %d" % (self.contry ,self.goals ,self.height,self.shirtName)
def __repr__(self):
   	return "%s - %s - %d - %d" % (self.contry ,self.goals ,self.height,self.shirtName)

class OperacionesEquipo(object):
	def __init__(self, listado):
		self.listado_jugadores = listado
	def get_promedio_goles(self):
		val = 0
		for i in self.listado_jugadores:
			val = val + i.goals 

		prom = val / len(self.listado_jugadores)
		return prom


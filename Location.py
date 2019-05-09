class Location():
	id = -1
	name = ""
	connections = []
	def __init__(self, id, name, connections):
		self.id = id
		self.name = name
		self.connections = connections
	def addCon(self, con):
		if not(con in self.connections):
			self.connections.append(con)
	def cons(self):
		cons = ""
		for con in self.connections:
			cons = cons + str(con) + ", "
		return cons
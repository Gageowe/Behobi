from Location import Location
class Map():
	locations = []
	def __init__(self, locations=[]):
		self.locations = []
	def whereIs(self, name):
		x = -1
		name = name
		for loc in self.locations:
			if name == loc.name:
				x = loc.id
		return x
	def locName(self, num):
		return self.locations[num]
	def newLoc(self, name, location, connections=[]):
		self.locations.append(Location(len(self.locations), name, location))
	def getIds(self, names):
		ids = []
		for name in names:
			if self.whereIs(name):
				ids.append(self.whereIs(name))
	def addCon(self, loc, ids):
		for id in ids:
			self.locations[loc].addCon(id)
			self.locations[id].addCon(loc)
		return ids
	def printLocs(self):
		names = ""
		for loc in self.locations:
			names = names + loc.name + ":" + " " +str(loc.id) + ", "
		print (names)
	def printCons(self, loca = -1):
		if loca == -1:
			for loc in self.locations:
				print(loc.name + ": " + loc.cons())
		else:
			print(self.locations[loca].name + ": " + self.locations[loca].cons())
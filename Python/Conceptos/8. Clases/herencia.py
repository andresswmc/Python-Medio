class Animal:
	def comer(self):
		print("Comiendo")

	def dormir(self):
		print("Durmiendo")

	def comun(self):
		print("Este es un metodo de Animal")

class Mascota:
	def fecha_adopcion(self, fecha):
		self.fecha_de_adopcion = fecha

	def comun(self):
		print("Este es un metodo de Mascota")

class Perro(Animal, Mascota):
	def __init__(self, nombre):
		self.nombre = nombre

	def ladrar(self):
		print("Ladrando")

	def dormir(self):
		print(self.nombre, "esta durmiendo")
		Animal.dormir(self)
		print("No molestar")

class Gato(Animal, Mascota):
	def ronroneo(self):
		print("ronroneo")

firulais = Perro("Firulais")
firulais.dormir()

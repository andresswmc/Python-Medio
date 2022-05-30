class Circulo:
	
	pi = 3.14159265
	def __init__(self, radio):
		self.radio = radio

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(Circulo.pi)

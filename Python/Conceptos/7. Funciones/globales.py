animal = 'León' #Variable global

def mostrar_animal()
	global animal
	animal = 'Ballena' #Variables locales
	print(animal)

mostrar_animal()
print(animal)
def crear_usuario(nombre='', apellido='', edad):
	return{
	'nombre' : nombre,
	'apellido' : apellido,
	'nombre_completo' : "{} {}".format(nombre, apellido),
	'edad' : edad
	}

codi = crear_usuario("nombre", "apellido", 30)

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])
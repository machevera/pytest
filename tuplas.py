
def p(mensaje):
	print("\n--"+mensaje+"--")

p("** TUPLAS desde Sublime 3 **")
p("Para compilar presionar Ctrl-B y Python debe estar en PATH")
#este es un comentario 

p('Genero la tupla')
mitupla=("primero","segundo","cuarto")
print(mitupla)

p('Acceso al primer')
print(mitupla[0])

p('Acceso al ultimo')
print(mitupla[-1])

p("Nueva Tupla Marcos 26.4.74")
mitupla=("Marcos",26,4,1974)
print(mitupla)

p("Convierto en lista")
milista=list(mitupla)
print(milista)

p("Validar si MArcos existe valor en tupla")
existe=False
existe="MArcos" in mitupla
if existe:
	print("Existe MArcos")
else:
	print("No existe MArcos")

p("Longitud de la tupla")
print(len(mitupla))

p("Error al definir tupla de un solo valor")
mitupla2=("Jenny")
print(mitupla2)
print(type(mitupla2))

p("Corrección al definir tupla de un solo valor")
mitupla2=("Jenny",)
print(mitupla2)
print(type(mitupla2))

p("Desempaquetado de tuplas ")
print(mitupla)
nombre,dia,mes,anio=mitupla
print("nombre "+ nombre)
print("dia "+ str(dia)) 
print("mes "+ str(mes))
print("año "+ str(anio))
#f{"Nombre: {1} Nacimiento:{2}"}

p("Impresion formateada del Desempaquetado")
print(f"Nombre : {nombre}\nNacimiento: {str(dia)}/{str(mes)}/{str(anio)}")

p("***FIN***")
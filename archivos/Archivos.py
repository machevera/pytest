#Uso de archivos
def p(mensaje):
	print("\n--"+mensaje+"--")

p("**Gestion de Archivos**")
p('apertura de archivo')
archivo=open("prueba.txt")
p('lectura de contenido en una variable string')
contenido=archivo.read()
p('Impresion de la variable string')
print(contenido)

p('lectura de contenido en lista')
archivo.seek(0)
lineas=archivo.readlines()
p('impresion de contenido en la variable lista')
print(lineas)
p('impresion de contenido en la variable lista por renglones')
n=0
for linea in lineas:
	n+=1
	print(f"linea {n} --> {linea}")

p('Impresion de contenido en la variable lista por renglones en archivo')
archivo_out=open("prueba.salida.txt",mode="w")
n=0
for linea in lineas:
	n+=1
	archivo_out.write(f"linea {n} --> {linea}")


p('Cerrando Archivos')
archivo.close()
archivo_out.close()
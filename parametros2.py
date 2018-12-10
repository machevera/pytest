#sys.argv is the list of command-line arguments.
#sys.argv ES UNA LISTA
#uso de la libreria getopt (get options)
#python parametros2.py -i archivo1.xls -o archivo1.sql
#python parametros2.py --ifile=archivo1.xls --ofile=archivo1.sql

#imports
import sys 
import getopt

#funciones
def p(mensaje):
	print("\n--"+mensaje+"--")

p('** PARAMETROS DE LA LINEA DE COMANDOS (con gestion de opciones) **')

p('cantidad de parametros')
print(str(len(sys.argv)))


p("carga de opciones (lista)")
#python parametros2.py -i archivo1.xls -o archivo1.sql
#python parametros2.py --ifile=archivo1.xls --ofile=archivo1.sql
try:
	#sys.argv[1:] es la lista de opciones 
	opciones,argumentos=getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
	print ("parametros2.py -i <archivo entrada> -o <archivo salida>")
	sys.exit(0)

p('lista de opciones')
print(opciones)	
p('lista de argumentos')
print(argumentos)

p('gestion de opciones y argumentos')
for opcion,argumento in opciones:
	print(f"el valor de la opcion {opcion} es {argumento}")
	if opcion in ("-i","--ifile"):
		print(f"el archivo de entrada es {argumento}")
	elif opcion in ("-o","--ofile"):
		print(f"el archivo de salida es {argumento}")

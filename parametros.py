#sys.argv is the list of command-line arguments.
#sys.argv ES UNA LISTA

# queda pendiente la definicion
#import milib


#imports
import sys 

#funciones
def p(mensaje):
	print("\n--"+mensaje+"--")

p('** PARAMETROS DE LA LINEA DE COMANDOS (sin gestion de opciones) **')

p('cantidad de parametros')
print(str(len(sys.argv)))

p('relacion de parametros')
for i in sys.argv:
	print(i)

p('fin')
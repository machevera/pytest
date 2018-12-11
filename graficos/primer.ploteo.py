'''
Primero Ploteo de Graficos
Usando las bibliotecas:
matplotlib
'''
#importacion 
#import pandas as pd 
from matplotlib import pyplot as plt 

#definicion de funciones
def p(mensaje):
	print("\n--"+mensaje+"--")

p("** GRAFICO CON LISTAS **")

p("ejemplo 1: listas ")
x=[1,2,3,4,5,6]
y=[1,4,9,16,25,36]

plt.plot(x,y)
plt.title("Ejemplo y=x2 con 6 muestras")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


p("ejemplo 2: con mas precision ")
x=[]
y=[]
for i in range(1,201):
	xi=i/20
	yi=pow(xi,2)
	x.append(xi)
	y.append(yi)

plt.plot(x,y)
plt.title("Ejemplo y=x2 con 200 muestras")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

p("ejemplo 3: varias series (>=2) ")
x=[]
y=[]
z=[]
for i in range(1,201):
	xi=i/20
	yi=pow(xi,2)
	zi=yi-xi
	x.append(xi)
	y.append(yi)
	z.append(zi)

plt.plot(x,y)
plt.plot(x,z)
plt.title("Mas de 2 series")
plt.xlabel('X')
plt.ylabel('Y & Z')
#debemos usar leyendas 
plt.legend(["Valores Y","Valores Z"])
plt.show()



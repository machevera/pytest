'''
Segundo Ploteo de Graficos
Usando las bibliotecas:
matplotlib
pandas
'''
#importacion 
import pandas as pd 
from matplotlib import pyplot as plt 

#definicion de funciones
def p(mensaje):
	print("\n--"+mensaje+"--")

p("** GRAFICO DESDE CSV **")

p('impresion de datos [dataframe]')
datos=pd.read_csv('sample.csv')
print(datos)
print(type(datos))#es un dataframe

p('impresion de la columna c [series]')
print(datos.column_c)
print(type(datos.column_c))

p('recorrido de la columna c')
for i in range(0 , len(datos.column_c)):
	print(datos.column_c.iloc[i])

plt.plot(datos.column_a,datos.column_b)	
plt.plot(datos.column_a,datos.column_c)
plt.xlabel("A")	
plt.ylabel("B y C")
plt.legend(["B","C"])
plt.show()


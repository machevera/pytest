'''
Cuarto Ploteo de Graficos
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

p("** GRAFICO DESDE CSV [nivel 3]**")

p('carga de dataframe')
datos=pd.read_csv('countries.csv') #es un dataframe

p('datos de us')
datos_us=datos[datos.country=="United States"] #es otro dataframe

p('datos de china')
datos_china=datos[datos.country=="China"] #es otro dataframe

#el ratio de crecimiento (en %) como serie 
plt.plot(datos_us.year,datos_us.population/datos_us.population.iloc[0]*100)
plt.plot(datos_china.year,datos_china.population/datos_china.population.iloc[0]*100)
plt.xlabel("Año")
plt.ylabel("Poblacion (% Crecimiento)")
plt.legend(["USA","CHINA"])
plt.show()

plt.show()
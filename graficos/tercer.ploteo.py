'''
Tercer Ploteo de Graficos
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

p("** GRAFICO DESDE CSV [nivel 2]**")

p('carga de dataframe')
datos=pd.read_csv('countries.csv') #es un dataframe

p('datos de us')
datos_us=datos[datos.country=="United States"] #es otro dataframe

p('datos de china')
datos_china=datos[datos.country=="China"] #es otro dataframe


plt.plot(datos_us.year,datos_us.population/pow(10,6)) #en millones
plt.plot(datos_china.year,datos_china.population/pow(10,6))
plt.xlabel("Año")
plt.ylabel("Poblacion (mllns)")
plt.legend(["USA","CHINA"])
plt.show()


def p(mensaje):
	print("\n--"+mensaje+"--")

p("** DICCIONARIOS desde Sublime 3 **")
#DICT[key] --> value
# {key1:value1,key2:value2,key3:value3,....}
p("Para compilar presionar Ctrl-B y Python debe estar en PATH")

p("Diccionario de Capitales del Mundo")
midict={"Peru":"Lima","Colombia":"Bogota","Francia":"Paris","USA":"Washington","España":"Madrid"}
print(midict)

p("Tamaño de Diccionario")
print(len(midict))

p("Agregando nuevas entradas al Diccionario")
midict["Italia"]="Roma"
midict["Loreto"]="Iquitos"
print(midict)

p("Modificando una entrada del Diccionario")
midict["USA"]="Washington D.C"
print(midict)

p("Eliminando una entrada del Diccionario")
del(midict["Loreto"])
print(midict)

p("Estructuras Complejas en Memoria sin necesidad de definición")
midict2= \
 {"Vargas Llosa":["La Casa Verde","La Ciudad y Los Perros","Conversación en la Catedral"],
  "Garcia Marquez":["100 años de Soledad","El Coronel No Tiene Quien Le Escriba"],
  "Cesar Vallejo":["Trilce","Los Heraldos Negros","La Piedra Cansada"]       }
print("Autores y su Bibliografia")
print(midict2)


midict3 = {
	"Queen":[1971,1991],
	"The Beatles":[1962,1970],
	"Pink Floyd":[1967,1994],
	"The Rolling Stones":[1963,"la actualidad"]
}
print("Grupos y Duracion")
print (midict3)


p("Recorridos de Estructuras Complejas")
p("solo se recorre por keys ")
p("Autores / Obras ")
for autor in midict2:
	print(f"Autor: {autor}")
	print("Bibliografia:")
	for obra in midict2[autor]:
		print(f'\t {obra}')

p("Grupos y Vigencia")
for grupo in midict3:
	inicio,fin=midict3[grupo]
	print(f'{grupo} estuvo formado desde {inicio} hasta {fin}')

p("Uso de Keys Values e Items")
print(f"KEYS   -> {midict2.keys()}")
print(f"VALUES -> {midict2.values()}")
print(f"ITEMS  -> {midict2.items()}")

print("rodrigo")
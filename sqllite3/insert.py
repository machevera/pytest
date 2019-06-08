import sqlite3

#conectarse a base de datos
con = sqlite3.connect('mibd.db') # si no esta la crea

#crear tabla
cursorObj = con.cursor()
#cursorObj.execute("CREATE TABLE stats (proceso text,inicio date, fin date)")
#con.commit()

#insertar registros
registros=["'proceso3', '25-04-2019','12-05-2019'",
	"'proceso4', '13-04-2019','30-04-2019'"]

for r in registros:
  insert="insert into stats values("+r+")"
  cursorObj.execute(insert)

con.commit()
import sqlite3

#conectarse a base de datos
con = sqlite3.connect('mibd.db') # si no esta la crea

#crear tabla
cur = con.cursor()
cur.execute("select * from stats")
rows=cur.fetchall() 
print(rows) #rows es una lista de tuplas
for row in rows:
	print(row)
#[print(row) for row in cur.fetchall()]

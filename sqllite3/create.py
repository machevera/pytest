import sqlite3

#conectarse a base de datos
con = sqlite3.connect('mibd.db') # si no esta la crea

#consultar tabla
cur=con.cursor()
cur.execute("CREATE TABLE stats (proceso TEXT,inicio  DATE,fin DATE")
con.commit()

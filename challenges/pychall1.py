import os
import sqlite3


tblValues = (("Jean-Baptiste Zorg", "Human",122),("Korben Dallas","Meat Popsicle",100),("Ak\'not","Mangalore",-5))
conn = sqlite3.connect('db_roster.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists tbl_roster(col_name TEXT, col_species TEXT, col_iq INT);")
    cur.executemany("INSERT INTO tbl_roster VALUES(?,?,?)", tblValues)
conn.close()

humans = ''
conn = sqlite3.connect('db_roster.db')
with conn:
    cur = conn.cursor()
    cur.execute("UPDATE tbl_roster SET col_species = 'Human' WHERE col_name = 'Korben Dallas';")
    cur.execute("SELECT col_name, col_iq FROM tbl_roster WHERE col_species = 'Human';")
    humans = cur.fetchall()
conn.close()
print(humans)

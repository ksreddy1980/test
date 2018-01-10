import mysql.connector

d = mysql.connector.Connect(host = "localhost", user = "srini", password = "Nari@1980", db = "Advik")

cur = d.cursor()

cur.execute("select * from artist")

print(cur.fetchmany(3))
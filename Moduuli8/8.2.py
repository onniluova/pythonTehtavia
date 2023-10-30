import mysql.connector

def haeICAOKoodi(name):
    lukumaara = 0
    sql = "SELECT name, type, COUNT(*) FROM airport"
    sql += " WHERE iso_country = '" + name + "'"
    sql += " GROUP BY type; "
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(rivi)
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentokonepeli',
         user='root',
         password="1234",
         autocommit=True
         )
name = input("Maakoodi: ")
haeICAOKoodi(name)
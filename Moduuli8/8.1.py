import mysql.connector

def haeICAOKoodi(icao):
    sql = "SELECT name FROM airport"
    sql += " WHERE iso_country = '" + icao + "'"
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
         password="grheGierhu43432-d",
         autocommit=True
         )
icao = input("Lentokentän ICAO koodi: ")
haeICAOKoodi(icao)
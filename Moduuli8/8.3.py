import mysql.connector
from geopy.distance import geodesic

def haeICAOjaEtäisyys(icao1, icao2):
    # Yhdistä tietokantaan
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='lentokonepeli',
        user='root',
        password="grheGierhu43432-d",
        autocommit=True
    )

    # Hae ICAO-koodien koordinaatit tietokannasta
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(f"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident IN ('{icao1}', '{icao2}')")
    tulos = cursor.fetchall()
    cursor.close()

    # Jos tulos on lyhyempi kuin 2 merkkiä, ohjelma keskeytyy ja palauttaa tyhjää.
    if len(tulos) != 2:
        print("ICAO-koodeja ei löydetty.")
        return

    # Asetetaan tulosten tiedot muuttujille
    icao1_tiedot = tulos[0]
    icao2_tiedot = tulos[1]

    # Lasketaan etäisyys Geopylla
    sijainti1 = (icao1_tiedot['latitude_deg'], icao1_tiedot['longitude_deg'])
    sijainti2 = (icao2_tiedot['latitude_deg'], icao2_tiedot['longitude_deg'])
    etäisyys = geodesic(sijainti1, sijainti2).kilometers

    # Printataan lentokenttien etäisyys
    print(f"Etäisyys ICAO-koodien {icao1} ja {icao2} välillä on {etäisyys} kilometriä.")

    # Suljetaan yhteys lopussa
    yhteys.close()

# Tiedoston ajaminen alkaa tästä.
# Kun tiedosto suoritetaan, "__name__" saa __main__ arvon. Jos tätä skriptiä ajettaisiin toisen skriptin osana, se saisi tiedoston nimen.
if __name__ == "__main__":
    icao1 = input("Syötä ensimmäinen ICAO-koodi: ").strip()
    icao2 = input("Syötä toinen ICAO-koodi: ").strip()
    haeICAOjaEtäisyys(icao1, icao2)
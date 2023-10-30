import requests
from flask import Flask, request
from flask.json import jsonify
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lentokonepeli',
    user='root',
    password="1234",
    autocommit=True
)
@app.route("/icao/<string:name>", methods=["GET"])
# Haetaan ICAO koodia vastaava kaupunki
def haeICAOKoodi(name):
    sql = "SELECT name FROM airport"
    sql += " WHERE ident = '" + name + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi)
    return jsonify({"ICAO": name, "Kaupunki": tulos})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
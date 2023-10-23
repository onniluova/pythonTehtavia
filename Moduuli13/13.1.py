import requests
from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route("/alkuluku/<int:luku>", methods=["GET"])
def alkuluku(luku=None):
    # Tarkistetaan, onko luku positiivinen.
    if luku is None:
        return jsonify({"Error": "Luku ei ole määritetty."}), 400
    elif luku < 1:
        return jsonify({"Error": "Luku ei ole positiivinen."}), 400

    # Testataan, onko luku alkuluku.
    alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            alkuluku = False
            break

    # Palautetaan vastaus.
    return jsonify({"Number": luku, "isPrime": alkuluku})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
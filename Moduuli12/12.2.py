import requests

loppu = 0

while loppu == 0:
    kaupunki = input("Syötä kaupunki: ")
    api_avain = "64a3c819f71b57b32d2758c31a6dcfa9"

    response = requests.get((f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}"))

    json_response = response.json()

    # Tarkistetaan onko json_responsella main avainta
    if "main" in json_response:
        # Parsataan json-data muuttujiin.
        lämpötila = json_response["main"]["temp"]
        kosteus = json_response["main"]["humidity"]
        tuulen_nopeus = json_response["wind"]["speed"]

        lämpötila = round(lämpötila, 1) - 273.15
        lämpötila = round(lämpötila, 2)

        # Printataan datat
        print(f"Lämpötila: {lämpötila}°C")
        print(f"Kosteus: {kosteus}%")
        print(f"Tuuli: {tuulen_nopeus} m/s")
    else:
        print("Virhe: Kaupunkia ei löytynyt")

    uusi = input("Haluatko syöttää uuden? y/n ")
    if uusi == "y":
        loppu = 0
    else:
        loppu = 1

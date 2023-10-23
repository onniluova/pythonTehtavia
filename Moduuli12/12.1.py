import requests

# Tehdään response muuttuja, jossa otamme request-kirjastolla vitsit sivustolta.
response = requests.get("https://api.chucknorris.io/jokes/random")

# Otetaan JSON response
json_response = response.json()

# Parsataan json response
joke = json_response["value"]

# Printataan vitsi
print(joke)
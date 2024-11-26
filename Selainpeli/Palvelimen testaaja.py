import requests
import json

icao = input("Anna ICAO-koodi: ")

pyyntö = f"http://127.0.0.1:3000/kentta/{icao}"
print(pyyntö)

vastaus_raw = requests.get(pyyntö)
print(vastaus_raw)

vastaus = vastaus_raw.json()
print(vastaus)

from flask import Flask, request
from flask_cors import CORS
import mysql.connector


### TÄMÄ EI TOIMI!!!
###############################################################################################

app = Flask(__name__)
CORS(app)
@app.route('/newgame/<name>/<difficulty>')
def server_newgame(name, difficulty):
    #Alustaa uuden pelin. game_data muuttujat laitetaan oletusarvoihin ja lisätään pelaajan nimi:



    #viesti = f"Uusi peli aloitettu nimellä {name}."
    #game_data['name'] = name
    #game_data['message'] = viesti
    #game_data['difficulty'] = difficulty #helppo, keskivaikea, vaikea
    #game_data['start_money'] = start_money #vaikeusasteen funktiona?

    return game_data


@app.route('/<flight_type>/<destination>')
def server_input(flight_type, destination):
#server_input parsii syötteen ja syöttää pelaajan valinnat game-funktioon joka pyörittää peliä

    vastaus = game(flight_type, destination)

    return vastaus

def game(flight_type, destination):

    game_data["flight_type"] = flight_type
    game_data["destination"] = destination
    game_data["message"] = f"Lennät kohteeseen {destination}"

    return game_data

#Pääohjelma
#globaalit muuttujat on testiversiota varten. game_data pitäisi olla lopullinen tietorakenne:

app.run(host='127.0.0.1', port=3000)
globaalit = {}
game_data = {
        "game_status": "gameinprogress/gameover/game won",
        "message": "default",
        "name": "default",
        "flight_type": "default",
        "destination": "default",
        # "total"-arvot on kertymä koko pelin ajalta. money_gained on viimeisimmän saapumisen lisäämä rahamäärä
        "difficulty": "hard?",
        "start_money": "1500",
        "money": "1500",
        "money_gained": "123",
        "co2": "50",
        "money_gained_total": "200",
        "money_spent_total": "100",
        "distance": "1000",
        # time, temperature, weather on reaaliaikaisia muuttujia joita ei tallenneta tietokantaan.
        "time": "12.00",
        "temperature": "20",
        "weather": "cloudy?",
        # Pelaajan sijainti, lentokentän tiedot:
        "location": {"goal": True, "visited": True, "icao": "efhk", "name": "helsinki", "country": "suomi",
                     "lat": "50.22", "lon": "20.22", "gdp": "0"},
        # lista tarjolla olevista lennoista:
        "flights": [{"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"}
                    ],
        # lista KAIKISTA lentokentistä. Vieraillut ja tavoite kentät on osoitettu booleilla: goal ja visited True/False
        "airports": [
            {"goal": True, "visited": True, "icao": "efhk", "name": "helsinki", "country": "suomi", "lat": "50.22",
             "lon": "20.22", "gdp": "0"},
            {"goal": False, "visited": False, "icao": "efhk", "name": "espoo", "country": "suomi", "lat": "50.22",
             "lon": "20.22", "gdp": "0"},
            {"goal": True, "visited": False, "icao": "efhk", "name": "vantaa", "country": "suomi", "lat": "50.22",
             "lon": "20.22", "gdp": "0"}
            ]
    }




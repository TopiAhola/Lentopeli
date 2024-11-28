

from flask import Flask, request
import mysql.connector


app = Flask(__name__)
@app.route('/newgame/<name>')
def server_newgame(name):
    #Alustaa uuden pelin...
    teksti = f"Uusi peli aloitettu nimellä {name}."
    vastaus = {"teksti": teksti}
    return vastaus


@app.route('/<input>')
def server_input(input):
#server_input parsii syötteen ja syöttää pelaajan valinnat game-funktioon joka pyörittää peliä
#kesken!
    flight
    vastaus = game(flight_type, destination)

    return vastaus

def game(input):
    data_dic = { "game_status" : "gameinprogress/gameover/game won",
"name":"Xxx",
"location_icao":"efhk",
"location_name":"helsinki",
"location_country":"Suomi",
"location_lat":"60.23",
"location_lon":"24.74",
"money":"1500",
"co2":"100",
"money_gained":"20",
"money_spent":"100",
"distance":"1000",
#time, temperature, weather on reaaliaikaisia muuttujia joita ei tallenneta tietokantaan.
"time":"12.00",
"temperature":"20",
"weather":"cloudy?",

#lista tarjolla olevista lennoista
"flights" : [   {"name":"a", "icao":"efhk", "cost":"x", "distance":"100", "co2":"50", "lat":"50.22", "lon":"20.22"},
                {"name":"a", "icao":"efhk", "cost":"x", "distance":"100", "co2":"50", "lat":"50.22", "lon":"20.22"},
                {"name":"a", "icao":"efhk", "cost":"x", "distance":"100", "co2":"50", "lat":"50.22", "lon":"20.22"},
                {"name":"a", "icao":"efhk", "cost":"x", "distance":"100", "co2":"50", "lat":"50.22", "lon":"20.22"}
                 ],

#lista KAIKISTA lentokentistä. Vieraillut ja tavoite kentät on osoitettu booleilla: goal ja visited True/False
"airports" : [  {"goal" : True , "visited":True, "name": "helsinki", "country":"suomi", "lat": "50.22", "lon": "20.22"},
                {"goal" : False , "visited":False, "name": "espoo", "country":"suomi", "lat": "50.22", "lon": "20.22"},
                {"goal" : True , "visited":False, "name": "vantaa", "country":"suomi", "lat": "50.22", "lon": "20.22"}
                ]
}
    return data_dic

app.run(use_reloader=True, host='127.0.0.1', port=3000)



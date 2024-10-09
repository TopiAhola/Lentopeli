### Eurooppalainen Turisti - Projekti

#### Importit
import mysql.connector <br>
import random <br>
from geopy import distance <br>

#### Tietokanta
Tietokantayhteyden nimi on "yhteys": <br>
yhteys = mysql.connector.connect(**parametrit) 

Kursorin nimi on "kursori": <br>
kursori = yhteys.cursor()

Tietokantaa käytetään käyttäjällä "game" <br>
parametrit = 
{"host" :'localhost', 
'database' :'flight_game', 
'user' : 'game',
'password' : '', 
"collation" : "latin1_swedish_ci"}


<img src="https://github.com/user-attachments/assets/8e5a8ea8-b712-43ff-a5bd-ad7815cd692a" width="75%" height="75%">


#### Funktiot

def load_game():
    #Näyttää edelliset pelit ja antaa pelaajan valita game_id numeron
    #Jos pelaaja antaa tyhjän syötteen aloittaa new_game funktion.


def new_game():
    #Luo pelaajan ja tavoitteet ja syöttää ne tietokantaan.
    #Palauttaa pelaajan game_id tietokannasta.


def random_location():
    #Antaa satunnaisen kentan ident-koodin


def goal_reached(game_id):
    #Hakee saavutettujen tavoitteiden totuusarvot tietokannasta.
    #Palauttaa True jos kaikki arvot != 0, palauttaa False jos yksikin arvo on 0.


def game_values(game_id):
    #Ottaa game:id ja palauttaa game taulun kaikki arvot listana.
    #Käytetään tietojen lataamiseen uudelleen jos on tehty muutoksia tietokantaan.


def show_location(game_id):
    #Tulostaa pelaajan sijainnin: Lentokenttä ja maa.


def show_goals(game_id):
    #Tulostaa pelaajan jäljellä olevat tavoitteet.


def get_destinations(game_location):
    #Ottaa sijainnin ja antaa vaihtoehdot minne lentää.


def get_nearby(game_location):
    #Ottaa pelaajan sijainnin ja palauttaa 3:n lähimmän kentän identin ja etäisyyden.


def get_jokeri(game_location, nearest1, nearest2, nearest3):
    #Ottaa pelaajan sijainnin ja antaa sattumanvaraisen matkakohteen identin.
    #Argumentit on game_location ja 3 kenttää jotka get_destinations arpoo. Ei anna samaa kenttää uudestaan.


def get_name_country(ident):
    #Ottaa identin ja palauttaa kentän nimen ja maan nimen.


def check_money(game_money, game_location, kentta1, kentta2, kentta3, kentta4):
    #Tarkistaa onko pelaajalla rahaa lentää kentille halvimmalla lipulla. Jos ei, pelaaja häviää pelin!


def dist(origin, destination):
    #Laskee kahden kentän välisen etäisyyden. Syöte on kenttien ident-koodi.
    #Antaa tuloksen kilometreinä kokonaislukuna.


def get_flights(game_location, kentta1, kentta2, kentta3, kentta4):
    #Palauttaa listan tupleja lennoista jotka ovat tarjolla.
    #tuple =(id, destination, distance, cost, co2)
    #vähäpäästöinen luokka on flights[0:3], keskipäästöinen on [4:8], suuri on [8:12]


def select_flight(flights):
    #Tulostaa tarjolla olevat lennot ja ottaa pelaajalta syötteen lennon valinta.


def fly(selected_flight, game_id):
    #Ottaa lennon tiedot. Hakee pelin tiedot ja muokkaa niitä lennon mukaisesti.
    #selected_flight =(destination, name, country, distance, cost, co2)


def get_money(game_id, game_location):
    #Antaa pelaajalle lisää rahaa. Voisi myös tulostaa jonkin selityksen mistä raha tulee.


def update_game(game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights):
    #Tallentaa muutoksia game-tauluun


def visit_destination(game_location, game_id):
    #Tarkistaa onko pelaaja käynyt kohteessa. Muokkaa tietokantaan visited ja goal taulut.


def end_game(game_id):
    #Pelaaja voittaa pelin. Tulostetaan lopputiedot.


def goal_reach_list(game_id):
    #Palauttaa pelaajan saavuttamat tavoitteet listana. end_game funktiota varten.

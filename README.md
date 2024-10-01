### Eurooppalainen Turisti - Projekti

#### Importit
import mysql.connector <br>
import random

#### Funktiot

def distance( origin, destination ):
Laskee kahden kentän välisen etäisyyden. Syöte on kenttien ident-koodit. Antaa tuloksen kilometreinä kokonaislukuna.

def random_location(): Antaa satunnaisen kentan ident-koodin

##### Valikko funktiot
def valikko(): Näyttää valikon, joka sisältää muita funktioita. Toimii numeroilla.

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


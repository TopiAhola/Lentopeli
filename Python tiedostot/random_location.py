
import mysql.connector
import random

# yhteys tietokantaan
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',
              "collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()


def random_location():
    #Antaa satunnaisen kentan ident-koodin

    #Haetaan kenttien ident.koodit listaan:
    sql = f"SELECT ident FROM kentat;"
    kursori.execute(sql)
    list = kursori.fetchall()
    kursori.close()

    #Arvotaan kenttä väliltä 0, listan pituus-1
    n = random.randint(0, len(list)-1)

    #Karsitaan erikoimerkit pois listaobjektista
    location = str(list[n])
    location = location.replace("('", "")
    location = location.replace("',)", "")

    #Palautetaan ident-koodi
    return location




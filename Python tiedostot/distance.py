
def distance( origin, destination ):
# Laskee kahden kentän välisen etäisyyden. Syöte on kenttien ident-koodi. Antaa tuloksen kilometreinä kokonaislukuna.

    import mysql.connector
    from geopy import distance

    #yhteys tietokantaan
    parametrit = {"host" :'localhost', 'database' :'flight_game', 'user' : 'game','password' : '', "collation" : "latin1_swedish_ci"}
    yhteys = mysql.connector.connect(**parametrit)
    kursori = yhteys.cursor()

    #Haetaan koordinaatit
    sql1= f"select longitude_deg, latitude_deg from kentat where ident ='{origin}'  "
    sql2= f"select longitude_deg, latitude_deg from kentat where ident ='{destination}' "

    kursori.execute(sql1)
    tulos1 = kursori.fetchall()
    kursori.execute(sql2)
    tulos2 = kursori.fetchall()
    kursori.close()

    #lasketaan etäisyys, muunnetaan kokonaisluvuksi
    dist = int(distance.distance(tulos1, tulos2).km)

    return dist






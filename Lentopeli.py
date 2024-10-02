### Ohjelman alusta ###
import mysql.connector
from geopy import distance
import random

#yhteys tietokantaan
parametrit = {"host" :'localhost', 'database' :'flight_game', 'user' : 'game','password' : '', "collation" : "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

### Peli alusta / Back-end ###

# Laskee kahden kentän välisen etäisyyden. Syöte on kenttien ident-koodi. Antaa tuloksen kilometreinä kokonaislukuna.
def distance( origin, destination ):
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


#Antaa satunnaisen kentan ident-koodin
def random_location():
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


#Arvotaan aloitus kenttä ja 4 lähintä kenttää ja yksi jokeri kenttä
def find_airports():
    # Haetaan kaikki kentät
    sql = "SELECT Ident, Country_fi FROM kentat;"
    kursori.execute(sql)
    kentat = [row[0] for row in kursori.fetchall()]  # Kenttien identit
    kursori.close()

    #arvotaan aloitus kenttä
    aloitus_kenttä = random.choice(kentat)
    print(f"Aloituskenttä: {aloitus_kenttä}")

    etaisyydet = []
    for kentta in kentat:
        if kentta != aloitus_kenttä:
            dist = distance(aloitus_kenttä, kentta)
            etaisyydet.append((kentta, dist))

    etaisyydet.sort(key=lambda x: x[1])
    lahi_kentat = etaisyydet[:4]

    print("4 lähintä lentokenttää: ")
    for kentta in lahi_kentat:
        print(f"{kentta[0]}: {kentta[1]} km")

    lahi_identit = [kentta[0] for kentta in lahi_kentat]
    jokeri = [kentta for kentta in kentat if kentta not in lahi_identit and kentta != aloitus_kenttä]

    if jokeri:  # Tarkistetaan, että listassa on mahdollisia jokerikenttiä
        jokeri_kentta = random.choice(jokeri)  # Arvotaan jokerikenttä
        jokeri_etaisyys = distance(aloitus_kenttä, jokeri_kentta)  # Lasketaan jokerikentän etäisyys
        print(f"Jokerikenttä: {jokeri_kentta}, Etäisyys: {jokeri_etaisyys} km")
    else:
        print("Ei löytynyt sopivaa jokerikenttää.")

### Valikko / Front-end ###

#Ensimmäinen funktio, joka tulostetaan pelaajalle näkyville
def alkufunktio():
    print("--- Tervetuloa Urheilijan Jalkapalloseikkailu Euroopassa! ---")
    print("\nTässä pelissä sinä olet jalkapalloilija, joka osallistuu kansainvälisiin turnauksiin viidessä eri Euroopan maassa.")
    print("Tavoitteesi on päästä kaikkiin viiteen maahan, joissa pelataan jalkapallo-otteluita.")
    print("Aloitat seikkailusi yhdestä Euroopan maasta ja saat 1500 € sponsorirahaa matkallesi.")
    print("Valitse yksi kolmesta lähimmistä lentokentästä ja tee valintoja, jotka vaikuttavat päästöihisi ja kuluihisi.")
    print("Kun saavut uuteen maahan saat palkkion kunniaosoituksena.")
    print("Kunniaosoituksen määrä riippuu kunkin valtion varallisuudesta (maan BKT).")
    
    print("\n--- Lentojen hinnat ja päästöt ---")
    print("1. Vähänpäästöinen luokka:")
    print("   - Päästöt: 100 g CO2 per kilometri")
    print("   - Hinta: 0,3 € per kilometri")
    print("2. Keskipäästöinen luokka:")
    print("   - Päästöt: 200 g CO2 per kilometri")
    print("   - Hinta: 0,2 € per kilometri")
    print("3. Suurpäästöinen luokka:")
    print("   - Päästöt: 300 g CO2 per kilometri")
    print("   - Hinta: 0,1 € per kilometri\n")
    
    print("Pelin tavoitteena on käydä kaikissa viidessä maassa mahdollisimman pienillä päästöillä.")
    print("Mikäli rahasi loppuvat, peli päättyy.")
    print("Voit voittaa pelin ja päästä kunnioitustauluun, jos onnistut saavuttamaan kaikki viisi kohdetta vähillä päästöillä!")


#Säännöt funktio
def nayta_saannot():
    print("\n--- Pelin säännöt ---")
    print("1. Tavoitteesi on käydä viidellä (5) satunnaisesti valitulla lentokentällä mahdollisimman pienillä päästöillä.")
    print("2. Saat 1500€ rahaa pelin alussa.")
    print("3. Pelissä valitset aina kolmesta lähimmästä lentokentästä minne haluat lentää.")
    print("4. Lentoluokan (vähänpäästöinen, keskipäästöinen, suurpäästöinen) valinta vaikuttaa kustannuksiin ja päästöihin.")
    print("5. Jokainen lento kuluttaa rahaa ja aiheuttaa päästöjä.")
    print("6. Voitat pelin, kun olet käynyt kaikilla viidellä tavoitelentokentällä.")
    print("7. Häviät pelin, jos rahat loppuvat ennen kuin olet saavuttanut tavoitteesi.")
    print("8. Lentoluokat vaikuttavat hintaan ja päästöihin seuraavasti:")
    print("   - Vähänpäästöinen: 0,4€/km ja 75 gCO2/km")
    print("   - Keskipäästöinen: 0,3€/km ja 150 gCO2/km")
    print("   - Suurpäästöinen: 0,2€/km ja 300 gCO2/km")
    print("9. Voit tarkistaa rahasi, päästösi ja sijaintisi milloin tahansa.")


#Lentokoneen valikko
def lentokone_valikko(etaisyys):
    print("\n--- Lentokoneen luokka ---")
    print("Valitse lentoluokka (1-3):")
    print("1. Vähänpäästöinen (100 g CO2/km, 0,3 €/km)")
    print("2. Keskipäästöinen (200 g CO2/km, 0,2 €/km)")
    print("3. Suurpäästöinen (300 g CO2/km, 0,1 €/km)")

    while True:
        valinta = input("Syötä valintasi (1-3): ")

        if valinta == "1" or valinta == "2" or valinta == "3":
            break
        else:
            print("Virheellinen syöte. Anna vain numero (1-3).")

    if valinta == "1":
        hinta_per_km = 0.3
        saastot_per_km = 100
    elif valinta == "2":
        hinta_per_km = 0.2
        saastot_per_km = 200
    else:
        hinta_per_km = 0.1
        saastot_per_km = 300

    kokonais_hinta = hinta_per_km * etaisyys
    kokonais_saastot = saastot_per_km * etaisyys

    print(f"\nValitsit luokan: {['Vähänpäästöinen', 'Keskipäästöinen', 'Suurpäästöinen'][int(valinta) - 1]}")
    print(f"Hinta matkastasi (etäisyys: {etaisyys} km): {kokonais_hinta:.2f} €")
    print(f"Matkastasi aiheutuvat päästöt: {kokonais_saastot} g CO2\n")

    return kokonais_hinta, kokonais_saastot

#Valikko funktio
def valikko():
    print("\n1. Lentokentät \n2. Tavoite lentokentät \n3. Pelin säännöt")
    valinta = input("Syötä numero: \n")

    # Lentokentät
    if valinta == "1":
        print("Lentokentät funktio")
    
    #Tavoite lentokentät
    elif valinta == "2":
        print("Tavoite lentokentät funktio")

    #Pelin säännöt
    elif valinta == "3":
        nayta_saannot()

    #Virheellinen valinta
    else:
        print("Virheellinen valinta")
        valikko()
#Valikko funktio
def valikko():
    print("\n1. Lentokentät \n2. Pelin säännöt")
    valinta = input("Syötä numero: \n")

    # Lentokentät
    if valinta == "1":
        select_flight(flights)

    #Pelin säännöt
    elif valinta == "2":
        print("Säännöt funktio")

    #Virheellinen valinta
    else:
        print("Virheellinen valinta")
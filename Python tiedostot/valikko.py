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
        print("Säännöt funktio")

    #Virheellinen valinta
    else:
        print("Virheellinen valinta")

while True:
    valikko()
#Valikko funktio
def valikko():
    print("\n1. Lentokentät \n2. Tavoite lentokentät \n3. Pelin säännöt")
    valinta = int(input("Syötä numero: "))

    # Lentokentät
    if valinta == 1:
        print("Lentokentät funktio")
    
    #Tavoite lentokentät
    elif valinta == 2:
        print("Tavoite lentokentät funktio")

    elif valinta == 3:
        print("Säännöt funktio")

while True:
    valikko()
def select_flight(flights):
    # Tulostaa tarjolla olevat kentät ja ottaa pelaajalta syötteen lentoluokan valinta.
    print("\nTarjolla on seuraavat kentät:")
    for i, flight in enumerate(flights[:4], 1):
        print(f"{i}: {flight[1]}, {flight[2]}, etäisyys {flight[3]} km")

    while True:
        try:
            selection = int(input("\nValitse lento (1-4):\n"))
            if 1 <= selection <= 4:
                selected_flight = flights[selection - 1]
                break
            else:
                print("Valitse numero välillä 1-4.")
        except ValueError:
            print("Virheellinen syöte. Anna numero väliltä 1-4.")

    # Valitaan lentoluokka
    while True:
        try:
            print("\nValitse lentoluokka:")
            print("1: Vähäpäästöiset lennot")
            print("2: Keskipäästöiset lennot")
            print("3: Suurpäästöiset lennot")
            class_selection = int(input("\nAnna numero (1-3):\n"))

            if class_selection == 1:
                selected_flight = flights[0:4][selection - 1]
            elif class_selection == 2:
                selected_flight = flights[4:8][selection - 1]
            elif class_selection == 3:
                selected_flight = flights[8:12][selectio n - 1]
            else:
                print("Valitse numero väliltä 1-3.")
                continue

            break
        except ValueError:
            print("Virheellinen syöte. Anna numero väliltä 1-3.")

    return selected_flight
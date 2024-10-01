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

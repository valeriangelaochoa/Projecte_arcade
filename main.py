import jocs
while True:
    print("---BENVINGUT/ADA AL MINI ARCADE---")
    print("1. Jugar a Pedra, Paper, Tisora ")
    print("2. Jugar a Endevinar el Número ")
    print("S. S'ha esta tancant el mini arcade adeu....")

    choice = input("Eligeix un joc: ").upper()

    match choice:
        case "1":
            jocs.janken()
        case "2":
            jocs.nana()
        case " ":
            print("Per favor posa una de les opcions que se le ofereix...")
        case "S":
            print("Moltes gracies, per jugar, s'ha esta tancat l'arcade...")
            break
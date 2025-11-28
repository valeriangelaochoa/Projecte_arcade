# Importa els jocs creats del fitxer jocs.py
import jocs
# Fa un bucle per mostrar el menú principal fins que l'usuari decideixi sortir
while True:
# Mostra el menú princial amb les opcions dels jocs i vol sortir
    print("---BENVINGUT/ADA AL MINI ARCADE---")
# Si vol jugar a pedra, paper o tisora que trii l'opció 1 
    print("1. Jugar a Pedra, Paper, Tisora ")
# Si vol jugar a endevinar el número que trii l'opció 2
    print("2. Jugar a Endevinar el Número ")
# Si vol sortir que trii l'opció S
    print("S. S'ha esta tancant el mini arcade adeu....")
# Demana a l'usuari que trii una opció
    choice = input("Eligeix un joc: ").upper()
# Utilitzem el match choice per gestionar les opcions que es poden triar
    match choice:
# Si l'usuari tria l'opció 1, es crida la funció janken del mòdul jocs
        case "1":
            jocs.janken()
# Si l'usuari tria l'opció 2, es crida la funció nana del mòdul jocs
        case "2":
            jocs.nana()
# Si l'usuari tria l'opció S, es mostra un missatge d'agraïment i es tanca el bucle
        case "S":
            print("Moltes gracies, per jugar, s'ha esta tancat l'arcade...")
            break
# Si l'usuari tria una opció no vàlida, es mostra un missatge d'error
        case _:
            print("Per favor posa una de les opcions que se le ofereix...")
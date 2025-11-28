# Importa la jugada del robot del fitxer robot.py
from robot import robot
# Funció del joc de pedra, paper o tisora
def janken():
# Opcions del joc
    opcions = ["pedra", "paper", "tisora"]
    while True:
# Tria el nombre de rondes
        rondes = input("Quantes rondes vols jugar 3 o 5? ")
# Puntuació de l'usuari i del robot
        puntuacio_usuari = 0
        puntacio_robot = 0
# Si no tria l'opció valida no comença el joc
        if rondes not in ["3", "5"]:
            print("Aquesta opcio no surt en les opcions que et donem")
# El joc comença amb elecció de 3 rondes
        if rondes == "3":
            while puntuacio_usuari < 4 and puntacio_robot < 4:
                jugada = input("Tria paper, pedra o tisora: ").strip()
                jugada_robot = robot().playing()
# Si l'elecció no està entre les opcions, et donara un missatge d'error
                if jugada not in opcions:
                    print("Aquesta elecció no esta entre les opcions per a triar")
                    continue
# Si la jugada és igual a la del robot, empaten
                if jugada == jugada_robot:
                    print("Han empatat")
# Si l'usuari tria pedra i el robot tisora, l'usuari guanya un punt
                elif (jugada == "pedra" and jugada_robot == "tisora"):
                    print("Has guanyat")
# Si l'usuari tria paper i el robot pedra, l'usuari guanya un punt
                    puntuacio_usuari += 1
                elif (jugada == "paper" and jugada_robot == "pedra"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
# Si l'usuari tria tisora i el robot paper, l'usuari guanya un punt
                elif (jugada == "tisora" and jugada_robot == "paper"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
# Ara si el robot tria paper i l'usuari pedra, el robot guanya un punt
                elif (jugada == "pedra" and jugada_robot == "paper"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
# Si el robot tria pedra i l'usuari tisora, el robot guanya un punt
                elif (jugada == "tisora" and jugada_robot == "pedra"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
# Si el robot tria tisora i l'usuari paper, el robot guanya un punt
                elif (jugada == "paper" and jugada_robot == "tisora"):
                    print("ha guanyat el robot")
                    puntacio_robot += 1
# Si en el cas que l'usuari arriba a 3 punts, guanya la partida i retorna al menú
                if puntuacio_usuari == 3:
                    print("Has guanyat la partida")
                    return
# Ara si el robot arriba a 3 punts, guanya la partida i retorna al menú
                if puntacio_robot == 3:
                    print("Ha guanyat el robot")
                    return
# El joc comença amb elecció de 5 rondes
        elif rondes == "5":
            while puntuacio_usuari < 6 and puntacio_robot < 6:
                jugada = input("Tria paper, pedra o tisora: ").strip()
                jugada_robot = robot().playing()
# Si l'elecció no està entre les opcions, et donara un missatge d'error
                if jugada not in opcions:
                    print("Aquesta elecció no esta entre les opcions per a triar")
                    continue
# Si la jugada és igual a la del robot, empaten
                if jugada == jugada_robot:
                    print("Han empatat")
# Si l'usuari tria pedra i el robot tisora, l'usuari guanya un punt
                elif (jugada == "pedra" and jugada_robot == "tisora"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
# Si l'usuari tria paper i el robot pedra, l'usuari guanya un punt
                elif (jugada == "paper" and jugada_robot == "pedra"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
# Si l'usuari tria tisora i el robot paper, l'usuari guanya un punt
                elif (jugada == "tisora" and jugada_robot == "paper"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
# Ara si el robot tria paper i l'usuari pedra, el robot guanya un punt
                elif (jugada == "pedra" and jugada_robot == "paper"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
# Si el robot tria pedra i l'usuari tisora, el robot guanya un punt
                elif (jugada == "tisora" and jugada_robot == "pedra"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
# Si el robot tria tisora i l'usuari paper, el robot guanya un punt
                elif (jugada == "paper" and jugada_robot == "tisora"):
                    print("ha guanyat el robot")
                    puntacio_robot += 1
# Si en el cas que l'usuari arriba a 5 punts, guanya la partida i retorna al menú
                if puntuacio_usuari == 5:
                    print("Has guanyat la partida")
                    return
# Ara si el robot arriba a 5 punts, guanya la partida i retorna al menú
                if puntacio_robot == 5:
                    print("Ha guanyat el robot")
                    return
# Funció del joc d'edenvinar el numero
def nana():
# Importa el mòdul random per generar un número aleatori entre 1 i 100
    import random
    numero_endevinant = random.randint(1, 100)
# El comptador d'intents que ha fet l'usuari
    intents = 0
# Bucle per demanar a l'usuari que endevini el número entre 1 i 100
    while True:
# Demana a l'usuari que introdueixi un número
        numero = int(input("Introdueix un numero: "))
# Contara els intents que fa l'usuari
        intents +=1
# Comprova si el número és massa baix i dona un avís que es massa baix
        if numero < numero_endevinant:
            print("Aquest numero es massa baix")
# Comprova si el número és massa alt i dona un avís que es massa alt
        elif numero > numero_endevinant:
            print(" Aquest numero es massa alt")
# Si l'usuari endevina el número, felicita'l i mostra els intents que ha fet i tanca el joc i torna al menú
        else: 
            print(f"Felicitats, has endevinat el numero en aquests {intents} intents. ")
            break
if __name__ == "__main__":
    janken()
    nana()
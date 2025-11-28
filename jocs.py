# Importa la jugada del robot del fitxer robot.py
from robot import robot
# Funció del joc de pedra, paper o tisora
def janken():
# Opcions del joc
    opcions = ["pedra", "paper", "tisora"]
    while True:
        rondes = input("Que vols jugar hasta 3 victories o fins a 5 rondes? ")
        victoria_usuari = 0
        victoria_robot = 0
        if rondes not in ["3", "5"]:
            print("Aquesta opcio no surt en les opcions que et donem")
        if rondes == "3":
            while victoria_usuari < 4 and victoria_robot < 4:
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
                    victoria_usuari += 1
                elif (jugada == "paper" and jugada_robot == "pedra"):
                    print("Has guanyat")
                    victoria_usuari += 1
# Si l'usuari tria tisora i el robot paper, l'usuari guanya un punt
                elif (jugada == "tisora" and jugada_robot == "paper"):
                    print("Has guanyat")
                    victoria_usuari += 1
# Ara si el robot tria paper i l'usuari pedra, el robot guanya un punt
                elif (jugada == "pedra" and jugada_robot == "paper"):
                    print("Ha guanyat el robot")
                    victoria_robot += 1
# Si el robot tria pedra i l'usuari tisora, el robot guanya un punt
                elif (jugada == "tisora" and jugada_robot == "pedra"):
                    print("Ha guanyat el robot")
                    victoria_robot += 1
# Si el robot tria tisora i l'usuari paper, el robot guanya un punt
                elif (jugada == "paper" and jugada_robot == "tisora"):
                    print("ha guanyat el robot")
                    victoria_robot += 1
# Si en el cas que l'usuari arriba a 3 punts, guanya la partida i retorna al menú
                if victoria_usuari == 3:
                    print("Has guanyat la partida")
                    return
# Ara si el robot arriba a 3 punts, guanya la partida i retorna al menú
                if victoria_robot == 3:
                    print("Ha guanyat el robot")
                    return
        elif rondes == "5":
            ronda_count = 0
            while ronda_count < 5:
                ronda_count += 1
                print(f"\nRonda {ronda_count} de 5")
                jugada = input("Tria paper, pedra o tisora: ").strip()
                jugada_robot = robot().playing()
# Si l'elecció no està entre les opcions, et donara un missatge d'error
                if jugada not in opcions:
                    print("Aquesta elecció no esta entre les opcions per a triar")
                    ronda_count -= 1
                    continue
# Si la jugada és igual a la del robot, empaten
                if jugada == jugada_robot:
                    print("Han empatat")
# Si l'usuari tria pedra i el robot tisora, l'usuari guanya un punt
                elif (jugada == "pedra" and jugada_robot == "tisora"):
                    print("Has guanyat")
                    victoria_usuari += 1
# Si l'usuari tria paper i el robot pedra, l'usuari guanya un punt
                elif (jugada == "paper" and jugada_robot == "pedra"):
                    print("Has guanyat")
                    victoria_usuari += 1
# Si l'usuari tria tisora i el robot paper, l'usuari guanya un punt
                elif (jugada == "tisora" and jugada_robot == "paper"):
                    print("Has guanyat")
                    victoria_usuari += 1
# Ara si el robot tria paper i l'usuari pedra, el robot guanya un punt
                elif (jugada == "pedra" and jugada_robot == "paper"):
                    print("Ha guanyat el robot")
                    victoria_robot += 1
# Si el robot tria pedra i l'usuari tisora, el robot guanya un punt
                elif (jugada == "tisora" and jugada_robot == "pedra"):
                    print("Ha guanyat el robot")
                    victoria_robot += 1
# Si el robot tria tisora i l'usuari paper, el robot guanya un punt
                elif (jugada == "paper" and jugada_robot == "tisora"):
                    print("ha guanyat el robot")
                    victoria_robot += 1
                print(f"Resultat: Tu {victoria_usuari} - Robot {victoria_robot}")
            print(f"Puntuació final: Tu {victoria_usuari} - Robot {victoria_robot}")
            if victoria_usuari > victoria_robot:
                print("L'usuari ha guanyat")
                return
            elif victoria_robot > victoria_usuari:
                print("El robot ha guanyat")
                return
            else:
                print("Hem empatat")
                return
            
# Funció del joc d'endevinar el número
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
# Punt d'entrada per executar els jocs
if __name__ == "__main__":
# Crida a les funcions dels jocs pedra, paper o tisora i edenvinar el número
    janken()
    nana()
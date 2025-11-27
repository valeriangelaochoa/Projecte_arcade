from robot import robot
def janken():
    opcions = ["pedra", "paper", "tisora"]
    while True:
        rondes = input("Quantes rondes vols jugar 3 o 5? ")
        puntuacio_usuari = 0
        puntacio_robot = 0
        if rondes not in ["3", "5"]:
            print("Aquesta opcio no surt en les opcions que et donem")
        if rondes == "3":
            while puntuacio_usuari < 4 and puntacio_robot < 4:
                jugada = input("Tria paper, pedra o tisora: ").strip()
                jugada_robot = robot().playing()
                if jugada not in opcions:
                    print("Aquesta elecció no esta entre les opcions per a triar")
                    continue
                if jugada == jugada_robot:
                    print("Han empatat")
                elif (jugada == "pedra" and jugada_robot == "tisora"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
                elif (jugada == "paper" and jugada_robot == "pedra"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
                elif (jugada == "tisora" and jugada_robot == "paper"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
                elif (jugada == "pedra" and jugada_robot == "paper"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
                elif (jugada == "tisora" and jugada_robot == "pedra"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
                elif (jugada == "paper" and jugada_robot == "tisora"):
                    print("ha guanyat el robot")
                    puntacio_robot += 1
                if puntuacio_usuari == 3:
                    print("Has guanyat la partida")
                    return
                if puntacio_robot == 3:
                    print("Ha guanyat el robot")
                    return
        elif rondes == "5":
            while puntuacio_usuari < 6 and puntacio_robot < 6:
                jugada = input("Tria paper, pedra o tisora: ").strip()
                jugada_robot = robot().playing()
                if jugada not in opcions:
                    print("Aquesta elecció no esta entre les opcions per a triar")
                    continue
                if jugada == jugada_robot:
                    print("Han empatat")
                elif (jugada == "pedra" and jugada_robot == "tisora"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
                elif (jugada == "paper" and jugada_robot == "pedra"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
                elif (jugada == "tisora" and jugada_robot == "paper"):
                    print("Has guanyat")
                    puntuacio_usuari += 1
                elif (jugada == "pedra" and jugada_robot == "paper"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
                elif (jugada == "tisora" and jugada_robot == "pedra"):
                    print("Ha guanyat el robot")
                    puntacio_robot += 1
                elif (jugada == "paper" and jugada_robot == "tisora"):
                    print("ha guanyat el robot")
                    puntacio_robot += 1
                if puntuacio_usuari == 5:
                    print("Has guanyat la partida")
                    return
                if puntacio_robot == 5:
                    print("Ha guanyat el robot")
                    return

def nana():
    import random
    numero_endevinant = random.randint(1, 100)
    intents = 0
    while True:
        numero = int(input("Introdueix un numero: "))
        intents +=1
        if numero < numero_endevinant:
            print("Aquest numero es massa baix")
        elif numero > numero_endevinant:
            print(" Aquest numero es massa alt")
        else: 
            print(f"Felicitats, has endevinat el numero en aquests {intents} intents. ")
            break
if __name__ == "__main__":
    janken()
    nana()
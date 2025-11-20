def janken():
    import robot
    j = robot.robot()
    for ronda in range(1,5):
        resultat = input("¿Has guanyat aquesta ronda? (si/no): ")

def nana():
    import random
    numero_endevinant = random.randint(1, 100)
    while True:
        numero = int(input("Introdueix un numero: "))
        intents +=1
        if numero < numero_endevinant:
            print("Aquest numero es massa alt")
        elif numero > numero_endevinant:
            print(" Aquest numero es massa baix")
        else: 
            print(f"Felicitats, has endevinat el numero en aquests{intents} intents. ")
        break

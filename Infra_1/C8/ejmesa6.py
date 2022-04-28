#encoding:UTF-8
import random

frases_victoria = {
    "piedra" : { "lagarto" : ", aplasta lagarto.", "tijera": ", aplasta tijera."},
    "papel" : { "piedra": ", envuelve piedra.", "spock": ", desautoriza spock."},
    "tijera" : { "papel": ", corta papel.", "lagarto": ", decapita lagarto."},
    "lagarto" : {"spock": ", envenena spock", "papel": ", devora papel"},
    "spock" : {"tijera": ", rompe tijera.", "piedra": ", vaporiza piedra"}
    }


while True: 
    aleatorio = random.randrange(0, 5)
    elijePc = ""
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Salir del Programa")
    opcion = int(input("Que eliges: "))
    
    if opcion == 1:
        eligeUsuario = "piedra"
    elif opcion == 2:
        eligeUsuario = "papel"
    elif opcion == 3:
        eligeUsuario = "tijera"
    elif opcion == 4:
        eligeUsuario = "lagarto"
    elif opcion == 5:
        eligeUsuario = "spock"
    elif opcion == 6:
        print ("Nos vemos!")
        break
    else:
        print ("Valor Invalido")
        continue
        
    print("Tu eliges: ", eligeUsuario)   
    if aleatorio == 0:
        eligePc = "piedra"
    elif aleatorio == 1:
        eligePc = "papel"
    elif aleatorio == 2:
        eligePc = "tijera"
    elif aleatorio == 3:
        eligePc = "lagarto"
    elif aleatorio == 4:
        eligePc = "spock"
    print("PC eligio: ", eligePc)
    print("...")
    
    if eligePc == "piedra" and (eligeUsuario == "papel" or eligeUsuario == "spock"):
        print("Ganaste! "+ eligeUsuario.capitalize() + frases_victoria[eligeUsuario][eligePc])
    elif eligePc == "papel" and (eligeUsuario == "tijera" or eligeUsuario == "lagarto"):
        print("Ganaste! "+ eligeUsuario.capitalize() + frases_victoria[eligeUsuario][eligePc])
    elif eligePc == "tijera" and (eligeUsuario == "piedra" or eligeUsuario == "spock"):
        print("Ganaste! "+ eligeUsuario.capitalize() + frases_victoria[eligeUsuario][eligePc])
    elif eligePc == "lagarto" and (eligeUsuario == "piedra" or eligeUsuario == "tijera"):
        print("Ganaste! "+ eligeUsuario.capitalize() + frases_victoria[eligeUsuario][eligePc])
    elif eligePc == "spock" and (eligeUsuario == "lagarto" or eligeUsuario == "papel"):
        print("Ganaste! "+ eligeUsuario.capitalize() + frases_victoria[eligeUsuario][eligePc])
        
    if eligeUsuario == "piedra" and (eligePc == "papel" or eligePc == "spock"):
        print("Perdiste :( " + eligePc.capitalize() + frases_victoria[eligePc][eligeUsuario])
    elif eligeUsuario == "papel" and (eligePc == "tijera" or eligePc =="lagarto"):
        print("Perdiste :( " + eligePc.capitalize() + frases_victoria[eligePc][eligeUsuario])
    elif eligeUsuario == "tijera" and (eligePc == "piedra" or eligePc == "spock"):
        print("Perdiste :( " + eligePc.capitalize() + frases_victoria[eligePc][eligeUsuario])
    elif eligeUsuario == "lagarto" and (eligePc == "tijera" or eligePc =="piedra"):
        print("Perdiste :( " + eligePc.capitalize() + frases_victoria[eligePc][eligeUsuario])
    elif eligeUsuario == "spock" and (eligePc == "papel" or eligePc == "lagarto"):
        print("Perdiste :( " + eligePc.capitalize() + frases_victoria[eligePc][eligeUsuario])
    elif eligePc == eligeUsuario:
        print("Empate")
    again = input("Jugamos de nuevo? Si/No: ")
    if 'si' in again:
        continue
    elif 'no' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")
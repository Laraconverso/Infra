# PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK! (en python)

#encoding:UTF-8
import random
import string

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
        print("Ganaste, destruiste a la piedra!")
    elif eligePc == "papel" and (eligeUsuario == "tijera" or eligeUsuario == "lagarto"):
        print("Ganaste, cortaste el papel")
    elif eligePc == "tijera" and (eligeUsuario == "piedra" or eligeUsuario == "spock"):
        print("Ganaste, la tijera se rompio")
    elif eligePc == "lagarto" and (eligeUsuario == "tijera" or eligeUsuario == "piedra"):
        print("Ganaste, el lagarto murio ;-;")
    elif eligePc == "spock" and (eligeUsuario == "papel" or eligeUsuario == "lagarto"):
        print("Ganaste, spock no tiene poder aqui.")

    if eligeUsuario == "piedra" and (eligePc == "papel" or eligePc == "spock"):
        print("Perdiste")
    elif eligeUsuario == "papel" and (eligePc == "tijera" or eligePc =="lagarto"):
        print("Perdiste")
    elif eligeUsuario == "tijera" and (eligePc == "piedra" or eligePc == "spock"):
        print("Perdiste")
    elif eligeUsuario == "lagarto" and (eligePc == "tijera" or eligePc =="piedra"):
        print("Perdiste")
    elif eligeUsuario == "spock" and (eligePc == "papel" or eligePc == "lagarto"):
        print("Perdiste")
    
    
    elif eligePc == eligeUsuario:
        print("Empate")
    si = 'si'
    no = 'no'
    again = input("Jugamos de nuevo? si/no: ")
    if si == again:
        continue
    elif no == again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")
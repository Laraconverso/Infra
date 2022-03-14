import math
import random


def my1 ():
    contador = 1
    hecho = False
    while contador<=5 and not hecho:
        print("Hola mundo")
        contador= contador+1
        if contador == 6:
            hecho = True 


def my2():
    for item in [1,3,2,6,8,3]:
        print(item)

def my3():
    for item in range(5):
        print(item**2)

def my4():
    n = 9
    if n<0:
        print("Lo siento, el valor es negativo")
    else:
        print(math.sqrt(n))

def my5():
    # puntaje = random.choice([90, 50, 60, 70, 80])
    puntaje = random.choice(range(100))
    print(puntaje)
    print("Su grupo etario es: ")
    if puntaje >= 90: print('A')
    elif puntaje >= 80: print('B')
    elif puntaje >= 70: print('C')
    elif puntaje >= 60: print('D')
    elif puntaje >= 50: print('E')
    elif puntaje >= 40: print('F')
    elif puntaje >= 30: print('G')
    elif puntaje >= 18: print('H')
    else: print('MENOR DE 18')


def superfunction():
    my1()
    my2()
    my3()
    my4()
    my5()

superfunction()
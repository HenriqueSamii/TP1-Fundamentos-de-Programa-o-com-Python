import turtle
import math

N = int(input("Numero de triangulos - "))

def triangulo(n):
    if n==1:
        for target_list in range(3):
            turtle.forward(int(50))
            turtle.left(120)
    else:
        for facePolígono in range(n):
            algulo1 = 360/n
            angulo2E3 =  algulo1/2
            verticeParalela2E3 = 50
            veticeParalelaAo1 = math.sqrt((verticeParalela2E3**2)+(verticeParalela2E3**2)-2*verticeParalela2E3*verticeParalela2E3*math.cos(algulo1))
            turtle.forward(verticeParalela2E3)
            turtle.left(algulo1)
            turtle.forward(veticeParalelaAo1)
            turtle.left(algulo1)
            #turtle.left(180)
            
'''def triangulo(n):
    if n==1:
        for target_list in range(3):
            turtle.forward(int(50))
            turtle.left(120)
    else:
        for facePolígono in range(n):
            algulo1 = 360/n
            angulo2E3 =  algulo1/2
            verticeParalela2E3 = 50
            veticeParalelaAo1 = math.sqrt((verticeParalela2E3**2)+(verticeParalela2E3**2)-2*verticeParalela2E3*verticeParalela2E3*math.cos(algulo1))
            turtle.forward(verticeParalela2E3)
            turtle.left(180-angulo2E3)
            turtle.forward(veticeParalelaAo1)
            turtle.left(180-angulo2E3)
            turtle.forward(verticeParalela2E3)
            #turtle.left(180)'''

triangulo(N)
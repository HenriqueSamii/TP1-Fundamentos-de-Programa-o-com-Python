#18. (desafio) Em jogos antigos era possível ver que os desenhos eram compostos por vários triângulos.
#Como uma maneira de treinar isso,
#a partir do N dado pelo usuário desenhe um polígono de lado N composto somente por triângulos como na figura:

import turtle
import math

N = int(input("Numero de triangulos - "))

def triangulo(n):
    if n==1:
        for target_list in range(3):
            turtle.forward(int(50))
            turtle.left(120)
    else:
        for facePoligono in range(1,n+1):
            algulo1 = 360/n
            angulo2E3 =  (180-algulo1)/2
            '''verticeParalela2E3 = 50
            veticeParalelaAo1 = math.sqrt(verticeParalela2E3**2+verticeParalela2E3**2-2*verticeParalela2E3*verticeParalela2E3*(math.cos(algulo1)))
            #turtle.setheading(algulo1*facePoligono)
            turtle.forward(verticeParalela2E3)
            turtle.left(180-algulo1)
            turtle.forward(verticeParalela2E3)
            turtle.left(180-algulo1)
            turtle.forward(veticeParalelaAo1)
            #turtle.left(180-angulo2E3)
            #turtle.left(180)
            '''
            vetice1 = 50
            vetice2E3 = vetice1**2/(2*vetice1*math.cos(angulo2E3))
            turtle.forward(vetice2E3)
            turtle.left(angulo2E3)
            turtle.forward(vetice1)
            turtle.left(angulo2E3)
            turtle.forward(vetice2E3)
            #turtle.left(180-angulo2E3)
            turtle.left(180)
            
            

triangulo(N)
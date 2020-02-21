#9. Faça uma função que desenhe o triângulo obtido na questão 7
#(o que estou fazendo é do 8) com a ferramenta turtle.
import turtle
import math

x = float(input("comprimentos do lados 1 do triângulo - "))
y = float(input("comprimentos do lados 2 do triângulo - "))
z = float(input("comprimentos do lados 3 do triângulo - "))

thistuple = (x, y, z)

if thistuple[0]==thistuple[1] and thistuple[1]==thistuple[2]:
    print("O Triângulo é Equilátero: os comprimentos dos três lados são iguais.")
elif thistuple[0]!=thistuple[1] and thistuple[0]!=thistuple[2] and thistuple[1]!=thistuple[2]:
    print("O Triângulo é Escaleno: os comprimentos dos três lados são diferentes.")
else:
    print("O Triângulo é Isósceles: os comprimentos dos dois lados são iguais.")
    
anguloXY=180-math.degrees(math.acos((thistuple[0]**2+thistuple[1]**2-thistuple[2]**2)/(2*thistuple[0]*thistuple[1])))
anguloYZ=180-math.degrees(math.acos((thistuple[1]**2+thistuple[2]**2-thistuple[0]**2)/(2*thistuple[1]*thistuple[2])))
#anguloXZ=180-anguloXY-anguloYZ
#print(str(anguloXY))
turtle.forward(thistuple[0])
turtle.left(anguloXY)

turtle.forward(thistuple[1])
turtle.left(anguloYZ)

turtle.forward(thistuple[2])
#turtle.left(anguloXY)




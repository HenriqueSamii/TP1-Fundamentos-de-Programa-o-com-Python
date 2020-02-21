#8. Escreva um programa em Python que receba três valores reais X, Y e Z,
#guarde esses valores numa tupla e verifique se esses valores podem ser os comprimentos
#dos lados de um triângulo e, neste caso, retorne qual o tipo de triângulo formado.

#Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita:
#o comprimento de cada lado de um triângulo deve ser menor do que a soma do
#comprimento dos outros dois lados. Além disso,
#o programa deve identificar o tipo de triângulo formado observando as seguintes definições:

#Triângulo Equilátero: os comprimentos dos três lados são iguais.
#Triângulo Isósceles: os comprimentos de dois lados são iguais.
#Triângulo Escaleno: os comprimentos dos três lados são diferentes.
x = int(input("comprimentos do lados 1 do triângulo - "))
y = int(input("comprimentos do lados 2 do triângulo - "))
z = int(input("comprimentos do lados 3 do triângulo - "))

thistuple = (x, y, z)

if thistuple[0]==thistuple[1] and thistuple[1]==thistuple[2]:
    print("O Triângulo é Equilátero: os comprimentos dos três lados são iguais.")
elif thistuple[0]!=thistuple[1] and thistuple[0]!=thistuple[2] and thistuple[1]!=thistuple[2]:
    print("O Triângulo é Escaleno: os comprimentos dos três lados são diferentes.")
else:
    print("O Triângulo é Isósceles: os comprimentos dos dois lados são iguais.")
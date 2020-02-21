#20. Baseando no código criado na questão anterior, crie uma função na qual dado um N obtido através do usuário,
#sua tartaruga gire 90 + N graus.
#Teste para 1, 4 e 10 para obter as figuras a seguir.
import turtle

n = int(input("Numero de voltas - "))

turtle.color("red", "green")

for volta in range(n*4):
    turtle.forward(5+volta)
    turtle.left(90+volta)
    
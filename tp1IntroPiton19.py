#19. Dado um valor N do usuário, desenhe com a ferramenta turtle a seguinte imagem:
import turtle

n = int(input("Numero de voltas - "))

turtle.color("red", "green")

for volta in range(n*4):
    turtle.forward(5+volta)
    turtle.left(90)
    
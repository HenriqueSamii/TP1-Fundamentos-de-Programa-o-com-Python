#11. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um triângulo de lado N.
import turtle

def triangulo(n):
    for target_list in range(3):
        turtle.forward(int(n))
        turtle.left(120)
        
x = input("Tamanho do triângulo - ")
triangulo(x)
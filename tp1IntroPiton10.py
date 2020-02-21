#10. Faça uma função no Python que, utilizando a ferramenta turtle,desenhe um quadrado de lado N.
import turtle

def quadrado(n):
    for target_list in range(4):
        turtle.forward(int(n))
        turtle.left(90)
        
x = input("Tamanho do quadrado - ")
quadrado(x)
#12. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um círculo de raio N.
import turtle

def circulo(n):
    for target_list in range(360):
        turtle.forward(int(n))
        turtle.left(1)
        
x = input("Tamanho do círculo - ")
circulo(x)
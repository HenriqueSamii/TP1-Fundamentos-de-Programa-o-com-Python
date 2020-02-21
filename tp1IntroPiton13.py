#13. Usando a função obtida na questão 10,
#desenhe n quadrados um dentro de outro como mostrado na figura:
import turtle

def quadrado(n):
    for target_list in range(4):
        turtle.forward(int(n))
        turtle.left(90)
        
x = int(input("Tamanho do quadrado inicial - "))

y=0

while x-y>0:
    quadrado(x-y)
    turtle.pu()
    turtle.left(90)
    turtle.forward(3)
    turtle.right(90)
    turtle.forward(3)
    turtle.pd()
    y += 10
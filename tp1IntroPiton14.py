#14. Utilizando o código 10.1 da Etapa 2,
#onde utilizando a função onkey do turtle associamos valores às setas do teclado,
#para este exercício associe as funções obtidas nas questões 10, 11 e 12
#às teclas ‘q’, ‘t’ e ‘c’ respectivamente.

import turtle


##### Funções obtidas nas questões 10, 11 e 12 ############
def quadrado(n):
    for target_list in range(4):
        turtle.forward(int(n))
        turtle.left(90)
        
def triangulo(n):
    for target_list in range(3):
        turtle.forward(int(n))
        turtle.left(120)
        
def circulo(n):
    for target_list in range(360):
        turtle.forward(int(n))
        turtle.left(1)
        
###############################

##########Prints###############
def quadradoP():
    #from tp1IntroPiton10 import quadrado
    #x = input("Tamanho do quadrado - ")
    quadrado(100)

def trianguloP():
    #from tp1IntroPiton11 import triangulo
    #x = input("Tamanho do triângulo - ")
    triangulo(100)

def circuloP():
    #from tp1IntroPiton12 import circulo
    #x = input("Tamanho do círculo - ")
    circulo(1)

############################

turtle.listen()

turtle.onkey(quadradoP, 'q')
turtle.onkey(trianguloP, 't')
turtle.onkey(circuloP, 'c')
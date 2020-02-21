#7. Utilizando a ferramenta turtle,
#desenhe uma série de quadrados um do lado do outro como indicada na figura a seguir:

import turtle

turtle.shape('turtle')

for x in range(4):
    turtle.forward(50)
    for i in range(4):
        turtle.left(90)
        turtle.forward(50)
        
#quadradoNumero = 0
#quadradoVerti = 0

#while quadradoNumero < 4:
#    turtle.forward(50)
#    while quadradoVerti < 4:
#        turtle.left(90)
#        turtle.forward(50)
#        quadradoVerti += 1
#    quadradoNumero += 1
#    quadradoVerti = 0
    
#6. (Desafío) Utilizando a ferramenta turtle, desenhe os ângulos de um círculo como
#indicado na figura a seguir:
#Utilize as funções da ferramenta turtle setheading e write,
#além de outras que sejam necessárias.
import turtle

rotacaoGrau = 0

while rotacaoGrau < 360:
    turtle.setheading(rotacaoGrau)
    turtle.forward(150)
    turtle.write(str(rotacaoGrau)+"°")
    turtle.setheading(180+rotacaoGrau)
    turtle.forward(150)
    turtle.setheading(180+rotacaoGrau)
    rotacaoGrau += 15
#4. Escreva um programa em Python que calcule o fatorial de um dado número N usando um while.
#Use as mesmas especificações do item anterior.
inputUser = input("Calcular factorial de - ")
inputUser = int(inputUser)

preintFinal=1

if inputUser<0:
    print("Não é possível calcular fatorial de número negativo")
elif inputUser==0:
    pass
else:
    i = 1
    while i < inputUser+1:
        preintFinal=preintFinal*i
        i += 1
        
print(preintFinal)
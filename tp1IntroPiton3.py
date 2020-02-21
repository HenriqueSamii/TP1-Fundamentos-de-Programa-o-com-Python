#3. Escreva uma função em Python que calcule o fatorial de um dado número N usando um for.
#O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1.
#Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120.
#Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.
inputUser = input("Calcular factorial de - ")
inputUser = int(inputUser)

preintFinal=1

if inputUser<0:
    print("Não é possível calcular fatorial de número negativo")
elif inputUser==0:
    pass
else:
    for x in range(1,inputUser+1):
        preintFinal=preintFinal*x
        
print(preintFinal)
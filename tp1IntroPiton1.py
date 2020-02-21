#1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N,
#inclusive. O número N deve ser obtido do usuário.
#Ao final, escreva o valor do resultado desta soma.
inputUser = input("Insira um numero - ")
inputUser = int(inputUser)

for x in range(1,inputUser+1):
    if x%2!=0:
        print(x)
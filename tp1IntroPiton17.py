#17. Escreva uma função que receba uma string e um número inteiro x e
#rotacione a string x posições para a esquerda.
#Assuma que a string tem pelo menos x caracteres.


palavra = input("Palavra - ")
numeroRotacoes = int(input("Numero de rotações para a esquerda - "))

palavra = list(palavra)

if numeroRotacoes < len(palavra):
    for letra in range(numeroRotacoes):
        palavra.append(palavra[0])
        del palavra[0]
elif numeroRotacoes%len(palavra) != 0:
    for letra in range(numeroRotacoes%len(palavra)):
        palavra.append(palavra[0])
        del palavra[0]

palavraFinal = ""

for letra in palavra:
        palavraFinal+=letra

print(palavraFinal)
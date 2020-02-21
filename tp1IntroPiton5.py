#5. Trabalhar com tuplas é muito importante! Crie 4 funções nas quais:
#
# 1.Dada uma tupla e um elemento, verifique se o elemento existe na tupla
#   e retorne o indice do mesmo
# 2.Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
# 3.Dada uma tupla e um elemento, elimine esse elemento da tupla.
# 4.Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

tupleO = ("1","3","Mega", "Odeth", "10","Deth")

def proucura_item(item):
    global tupleO
    if item in tupleO:
        print(item + " esta na posição " + str(tupleO.index(item))+ " da tupla")
    else:
        print(item + " não existe na tupla")
        
def tuple_half():
    half1 = []
    half2 = []
    for items in range(len(tupleO)//2):
        half1.append(tupleO[items])
    for items in range(len(tupleO)-len(tupleO)//2,len(tupleO)):
        half2.append(tupleO[items])
    half1 = tuple(half1)
    half2 = tuple(half2)
    print(str(half1)+" "+str(half2))
    
def delet_item(item):
    global tupleO
    if item in tupleO:
        arrayHolder = []
        #arrayHolder.append(tupleO)
        for items in range(len(tupleO)):
            arrayHolder.append(tupleO[items])
        arrayHolder.remove(item)
        tupleO = tuple(arrayHolder)
        print("Tupla modificada para: " + str(arrayHolder))
    else:
        print(item + " não existe na tupla")
        
def invert_items():
    global tupleO
    arrayHolder = []
    for items in range(len(tupleO)-1,-1,-1):
        arrayHolder.append(tupleO[items])
    arrayHolder = tuple(arrayHolder)
    print(arrayHolder)

N = 6

while N != "5":
    N = input("\nTulpa original: "+str(tupleO)+"\n1.Verificar se o elemento existe na tupla e retornar o indice.\n2.Retornar 2 tuplas com cada metade da tupla original.\n3.De um elemento para ser eliminado da esse tupla.\n4.Retornar uma tupla com todos os elementos invertidos.\n5.Terminar Programa\n")
    if N=="1":
        itemProucura = input("Elemento proucurado - ")
        proucura_item(itemProucura)
    elif N=="2":
        tuple_half()
    elif N=="3":
        itemDelet = input("Elemento a deletar - ")
        delet_item(itemDelet)
    elif N=="4":
        invert_items()
    elif N=="5":
        print("Adeus")
    else:
        print("Essa opção não existe")
    


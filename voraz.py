from funcionesAux import *

# solucion al caso concreto 2 por medio de un algoritmo voraz
def vorazP2(arr):
    aux=arr
    aux = countSort(aux,24,len(aux))
    print(aux)
    # mergeSort(aux)# algoritmo de ordenamiento
    concat=[]
    inicio=0
    for x in aux:
        print(x,inicio)
        if x[1]>=inicio:
            concat.append(x)
            inicio=x[2]
    return concat

def vorazP1(arr,n):
    aux = filtarTam(arr)
    mergeSort(aux,3) # algoritmo de ordenamiento
    aux = aux[::-1]
    concat=[]
    intervalo = [[0,n]]
    for x in aux:
        iaux = [[x[0],x[1]] for x in intervalo]
        interaux = []
        if ingresa(x,iaux,interaux):
            intervalo = interaux
            concat.append(x)
    return concat

# def main():
#     lista=[["a",1,2],["b",1,4],["m",2,5],["c",1,5],["h",6,7],["s",9,10],["s",9,11],["r",12,22]]
#     print(vorazP1(lista,24))
# # main()




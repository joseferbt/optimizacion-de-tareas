from funcionesAux import *
ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())
# solucion al caso concreto 2 por medio de un algoritmo voraz
def vorazP2(arr):
    aux=arr
    aux = countSort(aux,24,len(aux))
    # mergeSort(aux)# algoritmo de ordenamiento
    concat=[]
    inicio=0
    for x in aux:
        if x[1]>=inicio:
            concat.append(x)
            inicio=x[2]
    return concat


"""aux = crearEntrada(10)
print(aux)
for i in aux:
    print(i[0],i[1],i[2])
"""
printAns2(vorazP2(aux),outFile)
ioFile.close()
outFile.close()





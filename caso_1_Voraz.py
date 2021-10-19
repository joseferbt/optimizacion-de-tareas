from funcionesAux import *
ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())

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

printAns1(vorazP1(matriz,24),outFile)
aux = crearEntrada(10)
print(aux)
for i in aux:
    print(i[0],i[1],i[2])
# printAns1(vorazP1(aux,24),outFile)
ioFile.close()
outFile.close()


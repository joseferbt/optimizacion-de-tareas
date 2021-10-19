from funcionesAux import *
horasDisponibles = [0,24]
ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())

def mejor_factibleP1(arr):
    aux_obj=list()
    aux=0
    for x in arr:
        count=0
        for y in x:
            count+=y[2]-y[1]
        if count>=aux:
            aux=count
            aux_obj=x
    return aux_obj

def solucionP1(arr):
    arry=arr
    mergeSort(arry,2)
    ingg=ingenua(arr)
    fac=factibles(ingg)
    sol=mejor_factibleP1(fac)
    return sol

printAns1(solucionP1(matriz,),outFile)
aux = crearEntrada(10)
print(aux)
for i in aux:
    print(i[0],i[1],i[2])
# printAns1(solucionP1(aux),outFile)
ioFile.close()
outFile.close()
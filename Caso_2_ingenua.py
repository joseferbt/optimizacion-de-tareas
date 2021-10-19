from funcionesAux import * 

horasDisponibles = [0,24]
ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())
def mejor_factibleP2(arr):
    aux_obj=list()
    aux=0
    for x in arr:
        if len(x)>=aux:
            aux=len(x)
            aux_obj=x
    return aux_obj

def solucionP2(arr):
    arry=arr
    mergeSort(arry,2)
    ingg=ingenua(arr)
    fac=factibles(ingg)
    sol=mejor_factibleP2(fac)
    return sol
printAns2(solucionP2(matriz,),outFile)
"""aux = crearEntrada(10)
print(aux)
for i in aux:
    print(i[0],i[1],i[2])
# printAns1(solucionP2(aux),outFile)
"""
ioFile.close()
outFile.close()





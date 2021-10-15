from funcionesAux import *
horasDisponibles = 24
ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())
# for x in range(n):
#     print(matriz[x][0]," ",matriz[x][1]," ",matriz[x][2])

matriz = countSort(matriz,horasDisponibles,n)
mostrar(matriz)
def selActi_1(n, arr):
    ben =[[0 for x in range(horasDisponibles+1)] for x in range(n+1)]
    sol = [[0 for x in range(horasDisponibles+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for c in range(horasDisponibles+1):
            if beneficio(arr[i-1])>c:
                ben[i][c]=ben[i-1][c]
                sol[i][c]=0
            else:
                ben[i][c] = max(ben[i-1][c],beneficio(arr[i-1])+ben[i-1][c-beneficio(arr[i-1])])
                sol[i][c] = 1
    return sol

def solActi_1(arr,n,c,mat):
    matriz=[]
    if n == 0 :
        print()
    else:
        if arr[n][c]==1:
            solActi_1(arr,n-1,c-beneficio(mat[n-1]),mat,aux)
            aux.append(mat[n-1])
        else:
            solActi_1(arr,n-1,c,mat,aux)
    return aux
mataux = []
printAns(solActi_1(selActi_1(n,matriz),n,horasDisponibles,matriz,mataux),outFile)
mostrar(selActi_1(n,matriz))

# for x in range(n):
#     print(matriz[x][0]," ",matriz[x][1]," ",matriz[x][2])

ioFile.close()
outFile.close()
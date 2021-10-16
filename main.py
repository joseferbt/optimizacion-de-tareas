from funcionesAux import *

horasDisponibles = [0,24]
ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())


matriz = countSort(matriz, horasDisponibles[1], n)
mostrar(matriz)                        #-------------------------------------


def selActi_1(n, arr):
    ben = [[0 for x in range(horasDisponibles[1] + 1)] for x in range(n + 1)]
    sol = [[0 for x in range(horasDisponibles[1] + 1)] for x in range(n + 1)]
    available=[horasDisponibles]
    for i in range(1, n + 1):
        for c in range(horasDisponibles[1] + 1):
            if beneficio(arr[i - 1]) > c:
                ben[i][c] = ben[i - 1][c]
                sol[i][c] = 0
            else:
                aux=[]
                if ingresa(arr[i-1],[[0,c]],aux):
                    available=aux
                    ben[i][c] = max(ben[i - 1][c], beneficio(arr[i - 1]) + ben[i - 1][c - beneficio(arr[i - 1])])
                    sol[i][c] = 1
                print(c,arr[i-1],available,"[",i,"]");
    return sol


def solActi_1(arr, n, c, mat, aux):
    if n == 0:
        True
    else:
        if arr[n][c] == 1:
            mat[n-1],solActi_1(arr, n - 1, c - beneficio(mat[n - 1]), mat, aux)
            aux.append(mat[n - 1])
        else:
            solActi_1(arr, n - 1, c, mat, aux)
    return aux
"""mataux = []
inter = [[0,24]]
ingresa(["a","2","3"],inter,mataux)
print(mataux)
ingresa(["a","5","8"],mataux,inter)
print(inter)
mataux=[]
ingresa(["a","15","17"],inter,mataux)
print(mataux)
inter=[]
ingresa(["a","8","15"],mataux,inter)
print(inter)"""
mataux=[]
# printAns(solActi_1(selActi_1(n, matriz), n, horasDisponibles[1], matriz, mataux), outFile)
# mostrar(selActi_1(n, matriz))
# for x in range(n):
#     print(matriz[x][0]," ",matriz[x][1]," ",matriz[x][2])

print(newbeneficio([[0,1],[4,8],[11,24]]))
ioFile.close()
outFile.close()

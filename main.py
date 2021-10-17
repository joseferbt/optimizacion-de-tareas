
from funcionesAux import *
import sys
sys.setrecursionlimit(3000)

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
    itera = [[[horasDisponibles]for x in range(horasDisponibles[1] + 1)] for x in range(n + 1)]
    mostrar(itera)
    for i in range(1, n + 1):
        for c in range(horasDisponibles[1] ):
            aux = []
            iaux =[[itera[i][c][x][0],itera[i][c][x][1]] for x in range(len(itera[i][c]))]
            iaux= [[c,24]]
            # print(iaux)
            if not ingresa(arr[i - 1],iaux,aux):
                # print("]1[")
                itera[i][c] = aux
                ben[i][c] = ben[i - 1][c]
                sol[i][c] = 0
            else:
                # mostrar(itera)
                # print(aux)
                aux =[]
                # print(itera[i][c],"[X]")
                # print(iaux,"[Z]")
                iaux = [[itera[i][c][x][0], itera[i][c][x][1]] for x in range(len(itera[i][c]))]
                if ingresa(arr[i-1],iaux,aux):
                    # print("[2]")
                    itera[i][c] = aux    # (False, True)[(ar[1] <= gl[1]) and (gl[1] < ar[2])]
                    print(ben[i - 1][c],"  ",newbeneficio(itera[i][c]) ,"  ",ben[i - 1][c + beneficio(arr[i - 1])],"  ",max(ben[i - 1][c], newbeneficio(itera[i][c]) + ben[i - 1][c + beneficio(arr[i - 1])]),"[",i,",",c,"]")
                    ben[i][c] = max(ben[i - 1][c], newbeneficio(itera[i][c]) + ben[i - 1][c + beneficio(arr[i - 1])])
                    sol[i][c] = 1
            # mostrar(itera)
            print(ben[i],"[B]")
            print(c,arr[i-1],itera[i][c],"[",i,"]");
    return sol


def solActi_1(arr, n, c, mat, aux,i,j):
    if i == c+1 or j== n+1:
        True
    else:
        print(j,"[/]",i)
        print(len(arr))
        if arr[j][i] == 1:
            print(i+beneficio(mat[j-1]),"[Q]")
            solActi_1(arr, n, c , mat, aux,i + beneficio(mat[j-1]),j+1)
            aux.append(mat[j-1])
        else:
            solActi_1(arr, n ,c, mat, aux, i, j+1 )
    print(aux , "[9]")
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
printAns(solActi_1(selActi_1(n, matriz), n, 24, matriz, mataux,0,0), outFile)
mostrar(selActi_1(n, matriz))
# for x in range(n):
#     print(matriz[x][0]," ",matriz[x][1]," ",matriz[x][2])

ioFile.close()
outFile.close()

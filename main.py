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

def countSort(arr):
    output = [["","",""] for x in range(n)]
    count = [0 for i in range(horasDisponibles)]
    ans= [["","",""] for x in range(n)]
    for i in arr:
        count[int(i[2])] += 1
    for i in range(24):
        count[i] += count[i - 1]
    for i in range(n):
        output[count[int(arr[i][2])] - 1] = arr[i]
        count[int(arr[i][2])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

matriz = countSort(matriz)

def printAns(ans):
    aux =0
    for x in ans:
        aux+= int(x[2])-int(x[1])
    outFile.write(str(len(ans)))
    outFile.write("\n"+str(aux))
    for x in ans:
        outFile.write("\n"+x[0])

def beneficio(arr):
    return int(arr[2])-int(arr[1])

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


printAns(matriz)
mostrar(selActi_1(4,matriz))
# for x in range(n):
#     print(matriz[x][0]," ",matriz[x][1]," ",matriz[x][2])

ioFile.close()
outFile.close()
def mostrar(matriz):
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

def printAns(ans,file):
    aux =0
    for x in ans:
        aux+= int(x[2])-int(x[1])
    file.write(str(len(ans)))
    file.write("\n"+str(aux))
    for x in ans:
        file.write("\n"+x[0])

def beneficio(arr):
    return int(arr[2])-int(arr[1])
def countSort(arr,horasD,n):
    output = [["","",""] for a in range(n)]
    count = [0 for b in range(horasD+1)]
    ans= [["","",""] for c in range(n)]
    for i in arr:
        count[int(i[2])] += 1
    for x in range(1,horasD+1):
        count[x] += count[x - 1]
    for y in range(n):
        output[count[int(arr[y][2])] - 1] = arr[y]
        count[int(arr[y][2])] -= 1
    for z in range(len(arr)):
        ans[z] = output[z]
    return ans
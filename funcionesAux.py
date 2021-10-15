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
    output = [["","",""] for x in range(n)]
    count = [0 for i in range(horasD)]
    ans= [["","",""] for x in range(n)]
    for i in arr:
        count[int(i[2])] += 1
    for i in range(horasD):
        count[i] += count[i - 1]
    for i in range(n):
        output[count[int(arr[i][2])] - 1] = arr[i]
        count[int(arr[i][2])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans
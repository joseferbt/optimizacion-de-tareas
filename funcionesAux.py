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
def entre(ar,gl):
    return (False,True)[(ar[1] <= gl[1]) and (gl[1] < ar[2])]
def ingresa(arr,inter,newinter):
    l = len(inter)-1
    aux = bool
    count = 0
    if l ==-1:
        return False
    else:
        if int(arr[1])>=inter[l][0]and int(arr[2])<=inter[l][1]:
            if inter[l][0]==int(arr[1]) and inter[l][1]==int(arr[2]):
                inter.pop()
                newinter.append(inter)
                return True
            else:
                if inter[l][0]==int(arr[1]) and inter[l][1]>int(arr[2]):
                    print([int(arr[2]),inter[l][1]],"here")
                    newinter.append([int(arr[2]),inter[l][1]])
                    print(newinter,"[5]")
                elif inter[l][0]<int(arr[1]) and inter[l][1]>int(arr[2]):
                    newinter.append([inter[l][0], int(arr[1])])
                    newinter.append([int(arr[2]), inter[l][1]])
                elif inter[l][0]<int(arr[1]) and inter[l][1]==int(arr[2]):
                    newinter.append([inter[l][0], int(arr[1])])
            inter.pop()
            print(inter,"[2]")
            for x in range(l):
                # print(x,"[1]")
                newinter.append(inter[x])
            print(newinter,"[6]")
            return True
        else:
            print(newinter,"[4]")
            newinter.append(inter.pop())
            print(newinter,"[3]")
            print(inter, [0])
            return ingresa(arr,inter,newinter)


"""intervalo=[ x for x in range(0,24) ]
def ingresados(arr,  newinter):
    if (arr[1] in intervalo) and (arr[2] in intervalo):
            for y in range (arr[1],arr[2] ):
                newinter.pop(y)
            return True
    else:
        return False
"""


import random


def mostrar(matriz):
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


def printAns(ans, file):
    aux = 0
    for x in ans:
        aux += int(x[2]) - int(x[1])
    file.write(str(len(ans)))
    file.write("\n" + str(aux))
    for x in ans:
        file.write("\n" + x[0])


def beneficio(arr):
    return int(arr[2]) - int(arr[1])


def countSort(arr, horasD, n):
    output = [["", "", ""] for a in range(n)]
    count = [0 for b in range(horasD + 1)]
    ans = [["", "", ""] for c in range(n)]
    for i in arr:
        count[int(i[2])] += 1
    for x in range(1, horasD + 1):
        count[x] += count[x - 1]
    for y in range(n):
        output[count[int(arr[y][2])] - 1] = arr[y]
        count[int(arr[y][2])] -= 1
    for z in range(len(arr)):
        ans[z] = output[z]
    return ans


def entre(ar, gl):
    return (False, True)[(ar[1]<gl[2]) and (gl[2] <= ar[2])]


def ingresa(arr, iter, newinter):
    inter = iter
    l = len(inter) - 1
    if l == -1:
        return False
    else:
        if int(arr[1]) >= inter[l][0] and int(arr[2]) <= inter[l][1]:
            if inter[l][0] == int(arr[1]) and inter[l][1] == int(arr[2]):
                print()
            else:
                if inter[l][0] == int(arr[1]) and inter[l][1] > int(arr[2]):
                    newinter.append([int(arr[2]), inter[l][1]])
                elif inter[l][0] < int(arr[1]) and inter[l][1] > int(arr[2]):
                    newinter.append([inter[l][0], int(arr[1])])
                    newinter.append([int(arr[2]), inter[l][1]])
                elif inter[l][0] < int(arr[1]) and inter[l][1] == int(arr[2]):
                    newinter.append([inter[l][0], int(arr[1])])
            inter.pop()
            for x in range(l):
                newinter.append(inter[x])
            return True
        else:
            newinter.append(inter.pop())
            return ingresa(arr, inter, newinter)
def newbeneficio(intervalos):
    count =0
    for i in intervalos:
        count += i[1]-i[0]
    return 24-count

def mergeSort(array,sol):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L,sol)
        mergeSort(M,sol)
        i = j = k = 0
        while i<len(L) and j<len(M):
            if L[i][sol]<M[j][sol]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i<len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j<len(M):
            array[k] = M[j]
            j += 1
            k += 1

def filtardatos(arr):
    new = []
    for i in arr:
        new.append([i[0],int(i[1]),int(i[2])])
    arr = new
    return arr
def filtarTam(arr):
    new = []
    for i in arr:
        new.append([i[0],int(i[1]),int(i[2]),int(i[2])-int(i[1])])
    arr = new
    return arr
def sobrepon(ar, n, enlazados, ans, estado):
    aux = [[i[0],i[1],i[2]] for i in ar]
    if n == 1:
        enlazados.append(ar[0]) if estado else ans.append(ar[0])
    else:
        arn = aux[n - 1]
        arn_1 = aux[n - 2]
        aux.pop()
        if  entre(arn, arn_1):
            estado = True
            enlazados.append(arn)
        else :
            if estado:
                enlazados.append(arn)
                estado = False
            else :
                ans.append(arn)
        sobrepon(aux,n-1,enlazados,ans,estado)
def imprimir(ax,ay):
    plt.plot(ax,ay,'o')
    plt.xlabel("Tamaño de la entrada")
    plt.ylabel("Tiempo de respuesta")
    plt.show()

def test(ax,ay,algoritmo):
    for n in range(100,100000,1000):
        entrada=crearEntrada(n)
        # print(entrada,"[x]")
        start = time()
        algoritmo
        fin = time()
        result= fin- start
        # ax.append([n,float(" %.10f " % result)])
        ax.append(n)
        ay.append(float(" %.10f " % result))
def crearEntrada(n):
    salida=[]
    for x in range(0,n):
        hora_final=random.randint(1,24)
        hora_inicio=random.randint(0,hora_final-1)
        salida.append([":c",hora_inicio,hora_final])
    return salida

# aux=[]
# new=[]
# prueba =[[0,0,1],['1', 1, 2], ['2', 1, 4],['3', 2, 5], ['4', 1, 5],[5,6,8],[6,7,9],[7,9,10],[8,12,15],[9,14,15],[10,15,18],[10,18,20],[11,19,21]]
# sobrepon(prueba,len(prueba),aux,new,0)
new = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],[17,18],[19,20],[20,21],[21,22],[22,23],[23,24]]
 # new.reverse()
aux = []
# print(new)
# print(aux)



import random


def printAns1(ans, file):
    aux = 0
    for x in ans:
        aux += int(x[2]) - int(x[1])
    file.write(str(len(ans)))
    file.write("\n" + str(aux))
    for x in ans:
        file.write("\n" + x[0])


def printAns2(ans, file):
    file.write(str(len(ans)))
    for x in ans:
        file.write("\n" + x[0])


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
    plt.xlabel("Tama??o de la entrada")
    plt.ylabel("Tiempo de respuesta")
    plt.show()

def test(ax,ay):
    for n in range(100,100000,1000):
        entrada=crearEntrada(n)
        start = time()
        # colocar algoritmo para la entrada
        fin = time()
        result= fin- start
        ax.append(n)
        ay.append(float(" %.10f " % result))
    return float(" %.10f " % result)
def crearEntrada(n):
    salida=[]
    for x in range(0,n):
        hora_final=random.randint(1,24)
        hora_inicio=random.randint(0,hora_final-1)
        salida.append(["A"+str(x),hora_inicio,hora_final])
    return salida

def ingenua(arr=list):
    solucion=[]
    import itertools
    for L in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, L):
           solucion.append(subset)
    return solucion

def factibles(arr=list):
    fac=[]
    for x in arr:
        aux=False
        for y in range(1,len(x)):
            if x[y][2]>x[y-1][2] and x[y][1]>= x[y-1][2]:
                continue
            else:
                aux=True
                break
        if aux:
            continue
        else:
            fac.append(x)
    return fac


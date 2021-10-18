from funcionesAux import * 
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

def mejor_factibleP2(arr):
    aux_obj=list()
    aux=0
    for x in arr: 
        if len(x)>=aux:
            aux=len(x)
            aux_obj=x
    return aux_obj

def mejor_factibleP1(arr):
    aux_obj=list()
    aux=0
    for x in arr:
        count=0
        for y in x:
            count+=y[2]-y[1]
        if count>=aux:
            aux=count
            aux_obj=x
    return aux_obj


def solucionP2(arr):
    arry=arr
    mergeSort(arry,2)
    ingg=ingenua(arr)
    fac=factibles(ingg)
    sol=mejor_factibleP2(fac)
    return sol

def solucionP1(arr):
    arry=arr
    mergeSort(arry,2)
    ingg=ingenua(arr)
    fac=factibles(ingg)
    sol=mejor_factibleP1(fac)
    return sol

def main():
    lista=[["a",20,22],["b",11,14],["m",12,19],["0",0,5],["0",3,5],["0",0,1],["0",7,10],["0",15,17] ]
    (['0', 0, 5], ['0', 7, 10], ['m', 12, 19], ['a', 20, 22])
    print(solucionP1(lista))
main()

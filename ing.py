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

def solucion(arr):
    arry=arr
    mergeSort(arry,2)
    ingg=ingenua(arr)
    fac=factibles(ingg)
    sol=mejor_factibleP2(fac)
    return sol

def main():
    lista=[["a",20,22],["b",11,14],["m",12,19],["c",0,5],["h",6,9],["a",1,2],["b",1,4],["m",2,5],["c",1,5],["h",6,7],["s",9,10],["s",9,11],["r",12,22]]
    print(solucion(lista))
main()

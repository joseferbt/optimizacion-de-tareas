from funcionesAux import *
# se implementa la solución dinamica 

#sort(arr)-> arr
#devuelve un array  con los grupos de actividades que se sobreponen
def sobreponen(arr=list):
    rango_ocupado = 0
    aux = []
    auxno = []
    ya_anadido = False
    aux_inicio = 0
    for x in range(0, len(arr)):
        if arr[x][2] > rango_ocupado and arr[x][1] >= rango_ocupado:
            if ya_anadido:
                aux.append(arr[aux_inicio:x])
                # auxno.append(arr[x])
                ya_anadido = False
            rango_ocupado = arr[x][2]
        else:
            rango_ocupado = arr[x][2]
            if not ya_anadido:
                aux_inicio = x - 1
                ya_anadido = True
    if ya_anadido:
        aux.append(arr[aux_inicio:len(arr)])
        ya_anadido = False
    for x in aux:
       for i in x:
           arr.remove(i)
    auxno= arr
    return list([aux, auxno])

#devueve todas las posibilidades
#arr->arr[arr]
def ingenua(arr=list):
    solucion=[]
    import itertools
    for L in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, L):
           solucion.append(subset) 
    return solucion 

#arr[arr]->arr[arr]
#filtra las soluciones factibles
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

def solucion_ingenuaP2(arr):
    arry=arr
    mergeSort(arry,2)
    sobrepo=sobreponen(arry)
    sp=sobrepo[0]
    #colocar los que no sobreponen
    solu=sobrepo[1]
    for aux in sp:
        ing=ingenua(aux)
        facti=factibles(ing)
        mfacti=list(mejor_factibleP2(facti))
        solu= solu + mfacti
    return solu

def solucion_ingenuaP1(arr):
    arry=arr
    mergeSort(arry,2)
    sobrepo=sobreponen(arry)
    sp=sobrepo[0]
    #colocar los que no sobreponen
    solu=sobrepo[1]
    for aux in sp:
        ing=ingenua(aux)
        facti=factibles(ing)
        mfacti=list(mejor_factibleP1(facti))
        solu= solu + mfacti
    return solu
#funcion main
def main():
    print(sobreponen([['a', 0, 1], ['b', 1, 4], ["x", 0, 5],['m', 2, 5], ['c', 1, 5],[6,6,7],[7,6,8],[1,9,10]]))   # [[[['a', 1, 2], ['b', 1, 4], ['x', 0, 5], ['m', 2, 5]]], [['c', 1, 5]]]
    lista=[["a",20,22],["b",11,14],["m",12,19],["c",0,5],["h",6,9],["a",1,2], ["b",1,4],["m",2,5],["c",1,5],["h",6,7],["s",9,10],["s",9,11],["r",12,22]]
    a = [['a', 0, 1], ['b', 1, 4], ["x", 0, 5],['m', 2, 5], ['c', 1, 5],[6,6,7],[7,6,8],[1,9,10]]
    print(solucion_ingenuaP1(filtarTam(a)))
main()







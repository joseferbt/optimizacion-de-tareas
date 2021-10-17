from ordenar import *
# se implementa la solución dinamica 

#sort(arr)-> arr
#devuelve un array  con los grupos de actividades que se sobreponen
def sobreponen(arr=list):
    rango_ocupado=0
    aux=[]
    auxno=[]
    ya_anadido=False
    aux_inicio=0
    for x in range(len(arr)):
        if  arr[x][1]>=rango_ocupado:
            rango_ocupado=arr[x][2]
            if ya_anadido:
                aux.append(arr[aux_inicio:x])
                auxno.append(arr[x])
                ya_anadido=False
        else:
            rango_ocupado=arr[x][2]
            if not ya_anadido:
                aux_inicio=x-1   
                ya_anadido=True
    return list([aux,auxno])

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

def mejor_factible(arr):
    aux_obj=list()
    aux=0
    for x in arr: 
        if len(x)>=aux:
            aux=len(x)
            aux_obj=x
    return aux_obj


def solucion_ingenua(arr):
    arry=arr
    mergeSort(arry)
    sobrepo=sobreponen(arry)
    sp=sobrepo[0]
    #colocar los que no sobreponen
    solu=sobrepo[1]
    for aux in sp:
        ing=ingenua(aux)
        facti=factibles(ing)
        mfacti=list(mejor_factible(facti))
        solu= solu + mfacti
    return solu
    

#funcion main
def main():
    lista=[["a",1,2],["b",1,4],["m",2,5],["c",1,5],["h",6,7],["s",9,10],["s",9,11],["r",12,22]]
    print(lista)
    print(solucion_ingenua(lista))
main()





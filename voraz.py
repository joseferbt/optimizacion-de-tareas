from ordenar import *


def voraz(arr):
    aux=arr
    mergeSort(aux)# algoritmo de ordenamiento
    concat=[]
    inicio=0
    for x in aux:
        if x[1]>=inicio:
            #print(x,inicio)
            concat.append(x)
            inicio=x[2]
    return concat 

"""def main():
    lista=[["a",1,2],["b",1,4],["m",2,5],["c",1,5],["h",6,7],["s",9,10],["s",9,11],["r",12,22]]
    print(voraz(lista))
    
main()
"""



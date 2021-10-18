import random
import sys 
from  ingenua import *
from voraz import * 

num= 5

def crearEntrada(n):
    salida=[]
    for x in range(0,n):
        hora_final=random.randint(1,24)
        hora_inicio=random.randint(0,hora_final-1)
        salida.append([":c",hora_inicio,hora_final])
    return salida

def test():

    entrada=crearEntrada(num)
    print(entrada,"[x]")
    print(vorazP2([[':c', 17, 23], [':c', 6, 17], [':c', 1, 3], [':c', 16, 18], [':c', 6, 16]]))

test()




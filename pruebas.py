import random
import sys 
from  ingenua import *
from voraz import * 

num=int(sys.argv[1])

def crearEntrada(n):
    salida=[]
    for x in range(0,n):
        hora_final=random.randint(1,24)
        hora_inicio=random.randint(0,hora_final-1)
        salida.append([":c",hora_inicio,hora_final])
    return salida

def main():
    entrada=crearEntrada(num)
    print(vorazP2(entrada))

main()




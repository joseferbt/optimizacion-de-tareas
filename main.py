from funcionesAux import *
import sys
sys.setrecursionlimit(3000)

horasDisponibles = [0,24]
ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())

ioFile.close()
outFile.close()

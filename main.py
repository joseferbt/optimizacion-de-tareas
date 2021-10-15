ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

""" write() : Inserts the string str1 in a single line in the text file.
             File_object.write(str1)
    writelines() : For a list of string elements, each string is inserted in the text file.
    Used to insert multiple strings at a single time.
             File_object.writelines(L) for L = [str1, str2, str3]"""

n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())
# for x in range(n):
#     print(matriz[x][0]," ",matriz[x][1]," ",matriz[x][2])

def countSort(arr):
    output = [["","",""] for x in range(n)]
    count = [0 for i in range(24)]
    ans= [["","",""] for x in range(n)]
    for i in arr:
        count[int(i[2])] += 1
    for i in range(24):
        count[i] += count[i - 1]
    for i in range(n):
        output[count[int(arr[i][2])] - 1] = arr[i]
        count[int(arr[i][2])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans
matOrd = countSort(matriz)
for x in range(n):
    print(matOrd[x][0]," ",matOrd[x][1]," ",matOrd[x][2])

ioFile.close()
outFile.close()
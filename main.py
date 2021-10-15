ioFile = open("entrada.txt", "r")
outFile = open("salida.txt", "w")

   # write() : Inserts the string str1 in a single line in the text file.
            #  File_object.write(str1)
   #  writelines() : For a list of string elements, each string is inserted in the text file.
   #  Used to insert multiple strings at a single time.
            #  File_object.writelines(L) for L = [str1, str2, str3]
n = int(ioFile.readline())
matriz = []
for x in range(n):
    matriz.append(ioFile.readline().split())

ioFile.close()
outFile.close()
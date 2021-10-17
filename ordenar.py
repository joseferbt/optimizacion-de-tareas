def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i][2] < M[j][2]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def countSort(arr, horasD, n):
    output = [["", "", ""] for a in range(n)]
    count = [0 for b in range(horasD + 1)]
    ans = [["", "", ""] for c in range(n)]
    for i in arr:
        count[int(i[2])] += 1
    for x in range(1, horasD + 1):
        count[x] += count[x - 1]
    for y in range(n):
        output[count[int(arr[y][2])] - 1] = arr[y]
        count[int(arr[y][2])] -= 1
    for z in range(len(arr)):
        ans[z] = output[z]
    return ans



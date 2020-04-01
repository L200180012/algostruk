from routineswap import swap
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):        #lakukan operasi gelembung sebanyak n -1
        for j in range(n-i-1):  #dorong elemen terbesar ke ujung kanan
            if A[j] >A [j+1]:   #jika dikiri lebih besar dari dikanannya
                swap(A,j,j+1)   #tukar posisi elemen ke j dengan j+1

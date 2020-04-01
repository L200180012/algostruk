from routineswap import swap, cariPosisiYangTerkecil
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A,i,n)
        if indexKecil != i:
            swap(A,i,indexKecil)

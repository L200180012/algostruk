def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:   #cari posisi yang tepat
            A[pos] = A[pos - 1]                 #dan geser kekanan terus
            pos = pos - 1                       #nilai-nilai yang lebih besar
        A[pos] = nilai      #pada posisi ini tempatkan nilai elemen ke i

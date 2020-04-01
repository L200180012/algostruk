def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini           #anggap ini yang terkecil
    for i in range(dariSini+1, sampaiSini):   #cari di sisa list
        if A[i] < A[posisiYangTerkecil]:    #kalau menemukan yang lebih kecil,
            posisiYangTerkecil = i          #anggapan dirubah
        return posisiYangTerkecil

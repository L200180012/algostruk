def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    daftar = []
    while low <= high:
        if kumpulan[low] == target:
            daftar.append(low)
            low += 1
        else:
            low += 1
    return daftar
